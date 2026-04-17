import pytest

from app.constants.game.cards import Resource
from app.constants.game.utils import (PlayerTradeState, TradeCost,
                                      TradeRelationship)
from app.models.cards import ChoiceResource, FixedResource
from app.utils.game import (_get_trade_combinations_without_cost,
                            _get_trade_options_for_remaining,
                            _resolve_resource_permutations,
                            get_trade_combinations_with_cost)

"""

Tests for _get_trade_combinations_without_cost

"""


@pytest.fixture
def one_neighbor_state():
    return PlayerTradeState(
        player_id="player2",
        trade_costs={"player1": TradeRelationship()},
        available_resources={"player1": {Resource.WOOD: 2}},
    )


@pytest.fixture
def two_neighbor_state():
    return PlayerTradeState(
        player_id="player2",
        trade_costs={
            "player1": TradeRelationship(),
            "player3": TradeRelationship(),
        },
        available_resources={
            "player1": {Resource.WOOD: 2},
            "player3": {Resource.WOOD: 1},
        },
    )


def test_exact_single_source(one_neighbor_state):
    result = _get_trade_combinations_without_cost(one_neighbor_state, Resource.WOOD, 1)
    assert result == [{"player1": {Resource.WOOD: 1}}]


def test_take_multiple_from_single_source(one_neighbor_state):
    result = _get_trade_combinations_without_cost(one_neighbor_state, Resource.WOOD, 2)
    assert result == [{"player1": {Resource.WOOD: 2}}]


def test_split_across_neighbors_multiple(two_neighbor_state):
    result = _get_trade_combinations_without_cost(two_neighbor_state, Resource.WOOD, 2)
    assert {"player1": {Resource.WOOD: 2}} in result
    assert {"player1": {Resource.WOOD: 1}, "player3": {Resource.WOOD: 1}} in result
    assert len(result) == 2


def test_split_across_neighbors_single(two_neighbor_state):
    result = _get_trade_combinations_without_cost(two_neighbor_state, Resource.WOOD, 1)
    assert {"player1": {Resource.WOOD: 1}} in result
    assert {"player3": {Resource.WOOD: 1}} in result
    assert len(result) == 2


# --- Infeasible cases ---


def test_returns_empty_when_resource_unavailable():
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={"player1": TradeRelationship()},
        available_resources={"player1": {Resource.ORE: 2}},
    )
    result = _get_trade_combinations_without_cost(state, Resource.WOOD, 1)
    assert result == []


def test_returns_empty_when_count_exceeds_supply(one_neighbor_state):
    result = _get_trade_combinations_without_cost(one_neighbor_state, Resource.WOOD, 3)
    assert result == []


def test_returns_empty_when_no_neighbors():
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={},
        available_resources={},
    )
    result = _get_trade_combinations_without_cost(state, Resource.WOOD, 1)
    assert result == []


# --- Edge cases ---


def test_count_zero_returns_empty_combination():
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={"player1": TradeRelationship()},
        available_resources={"player1": {Resource.WOOD: 2}},
    )
    result = _get_trade_combinations_without_cost(state, Resource.WOOD, 0)
    assert result == [{}]


def test_neighbor_with_zero_resource_excluded():
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={"player1": TradeRelationship(), "player3": TradeRelationship()},
        available_resources={
            "player1": {Resource.WOOD: 0},
            "player3": {Resource.WOOD: 1},
        },
    )
    result = _get_trade_combinations_without_cost(state, Resource.WOOD, 1)
    assert result == [{"player3": {Resource.WOOD: 1}}]
    assert all("player1" not in combo for combo in result)


def test_no_duplicate_combinations(two_neighbor_state):
    result = _get_trade_combinations_without_cost(two_neighbor_state, Resource.WOOD, 2)
    seen = [
        frozenset((k, v[Resource.WOOD]) for k, v in combo.items()) for combo in result
    ]
    assert len(seen) == len(set(seen))


"""

Tests for get_trade_combinations_with_cost

"""


@pytest.fixture
def no_discount_state():
    return PlayerTradeState(
        player_id="player2",
        trade_costs={
            "player1": TradeRelationship(base_cost=2),
            "player3": TradeRelationship(base_cost=2),
        },
        available_resources={
            "player1": {Resource.WOOD: 2},
            "player3": {Resource.WOOD: 1},
        },
    )


@pytest.fixture
def left_discount_state():
    """player1 (left) has a discount on raw goods; player3 (right) does not."""
    return PlayerTradeState(
        player_id="player2",
        trade_costs={
            "player1": TradeRelationship(
                base_cost=2,
                discounted_resources={Resource.WOOD, Resource.STONE},
                discount_cost=1,
            ),
            "player3": TradeRelationship(base_cost=2),
        },
        available_resources={
            "player1": {Resource.WOOD: 2},
            "player3": {Resource.WOOD: 1},
        },
    )


# --- Cost calculation ---


def test_base_cost_single_neighbor(no_discount_state):
    result = get_trade_combinations_with_cost(no_discount_state, Resource.WOOD, 1)
    assert {"player1": TradeCost(amount=1, cost=2)} in result
    assert {"player3": TradeCost(amount=1, cost=2)} in result


def test_base_cost_multiple_units_single_neighbor(no_discount_state):
    result = get_trade_combinations_with_cost(no_discount_state, Resource.WOOD, 2)
    assert {"player1": TradeCost(amount=2, cost=4)} in result
    assert {
        "player1": TradeCost(amount=1, cost=2),
        "player3": TradeCost(amount=1, cost=2),
    } in result


def test_discounted_cost_single_neighbor(left_discount_state):
    result = get_trade_combinations_with_cost(left_discount_state, Resource.WOOD, 1)
    assert {"player1": TradeCost(amount=1, cost=1)} in result


def test_discount_does_not_apply_to_right_neighbor(left_discount_state):
    result = get_trade_combinations_with_cost(left_discount_state, Resource.WOOD, 1)
    assert {"player3": TradeCost(amount=1, cost=2)} in result


def test_discount_only_applies_to_discounted_resource(left_discount_state):
    """ORE is not in discounted_resources, so base cost should apply even for player1."""
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={
            "player1": TradeRelationship(
                base_cost=2,
                discounted_resources={Resource.WOOD},
                discount_cost=1,
            ),
        },
        available_resources={"player1": {Resource.ORE: 1}},
    )
    result = get_trade_combinations_with_cost(state, Resource.ORE, 1)
    assert result == [{"player1": TradeCost(amount=1, cost=2)}]


def test_split_combination_costs(left_discount_state):
    """Taking 1 from discounted left (cost=1) and 1 from right (cost=2) = total 3."""
    result = get_trade_combinations_with_cost(left_discount_state, Resource.WOOD, 2)
    split = {
        "player1": TradeCost(amount=1, cost=1),
        "player3": TradeCost(amount=1, cost=2),
    }
    assert split in result


def test_cheapest_combination_prefers_discounted_neighbor(left_discount_state):
    result = get_trade_combinations_with_cost(left_discount_state, Resource.WOOD, 2)
    total_costs = [sum(v.cost for v in combo.values()) for combo in result]
    cheapest = min(total_costs)
    # player1 has 2 wood at cost 1 each = 2 total, cheaper than any split involving player3
    assert cheapest == 2


# --- Infeasible cases ---


def test_returns_empty_when_resource_unavailable():
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={"player1": TradeRelationship()},
        available_resources={"player1": {Resource.ORE: 2}},
    )
    assert get_trade_combinations_with_cost(state, Resource.WOOD, 1) == []


def test_returns_empty_when_count_exceeds_supply(no_discount_state):
    assert get_trade_combinations_with_cost(no_discount_state, Resource.WOOD, 4) == []


# --- TradeCost shape ---


def test_trade_cost_fields():
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={"player1": TradeRelationship(base_cost=2)},
        available_resources={"player1": {Resource.WOOD: 3}},
    )
    result = get_trade_combinations_with_cost(state, Resource.WOOD, 3)
    assert result == [{"player1": TradeCost(amount=3, cost=6)}]


"""

Tests for _resolve_resource_permutations

"""

# --- Only fixed resources ---


def test_single_fixed_resource():
    result = _resolve_resource_permutations([FixedResource(resource=Resource.WOOD)])
    assert result == [{Resource.WOOD: 1}]


def test_multiple_fixed_resources():
    result = _resolve_resource_permutations(
        [
            FixedResource(resource=Resource.WOOD),
            FixedResource(resource=Resource.STONE),
        ]
    )
    assert result == [{Resource.WOOD: 1, Resource.STONE: 1}]


def test_duplicate_fixed_resources_are_summed():
    result = _resolve_resource_permutations(
        [
            FixedResource(resource=Resource.WOOD),
            FixedResource(resource=Resource.WOOD),
        ]
    )
    assert result == [{Resource.WOOD: 2}]


def test_empty_input():
    result = _resolve_resource_permutations([])
    assert result == [{}]


# --- Only choice resources ---


def test_single_choice_resource():
    result = _resolve_resource_permutations(
        [
            ChoiceResource(resources=[Resource.WOOD, Resource.STONE]),
        ]
    )
    assert len(result) == 2
    assert {Resource.WOOD: 1} in result
    assert {Resource.STONE: 1} in result


def test_two_choice_resources_produce_cartesian_product():
    result = _resolve_resource_permutations(
        [
            ChoiceResource(resources=[Resource.WOOD, Resource.STONE]),
            ChoiceResource(resources=[Resource.GLASS, Resource.CLOTH]),
        ]
    )
    assert len(result) == 4
    assert {Resource.WOOD: 1, Resource.GLASS: 1} in result
    assert {Resource.WOOD: 1, Resource.CLOTH: 1} in result
    assert {Resource.STONE: 1, Resource.GLASS: 1} in result
    assert {Resource.STONE: 1, Resource.CLOTH: 1} in result


def test_choice_resource_with_same_option_twice():
    """Both slots resolve to the same resource — should sum to 2."""
    result = _resolve_resource_permutations(
        [
            ChoiceResource(resources=[Resource.WOOD, Resource.STONE]),
            ChoiceResource(resources=[Resource.WOOD, Resource.ORE]),
        ]
    )
    assert {Resource.WOOD: 2} in result
    assert {Resource.WOOD: 1, Resource.STONE: 1} in result  # STONE + WOOD (from slot 2)
    assert {Resource.WOOD: 1, Resource.ORE: 1} in result  # WOOD (from slot 1) + ORE
    assert {Resource.STONE: 1, Resource.ORE: 1} in result


# --- Mixed fixed and choice resources ---


def test_fixed_and_single_choice():
    result = _resolve_resource_permutations(
        [
            FixedResource(resource=Resource.ORE),
            ChoiceResource(resources=[Resource.WOOD, Resource.STONE]),
        ]
    )
    assert len(result) == 2
    assert {Resource.ORE: 1, Resource.WOOD: 1} in result
    assert {Resource.ORE: 1, Resource.STONE: 1} in result


def test_fixed_and_choice_overlap():
    """Fixed WOOD + choice WOOD/STONE — one permutation should give WOOD: 2."""
    result = _resolve_resource_permutations(
        [
            FixedResource(resource=Resource.WOOD),
            ChoiceResource(resources=[Resource.WOOD, Resource.STONE]),
        ]
    )
    assert {Resource.WOOD: 2} in result
    assert {Resource.WOOD: 1, Resource.STONE: 1} in result


def test_multiple_fixed_and_multiple_choice():
    result = _resolve_resource_permutations(
        [
            FixedResource(resource=Resource.ORE),
            FixedResource(resource=Resource.CLAY),
            ChoiceResource(resources=[Resource.WOOD, Resource.STONE]),
            ChoiceResource(resources=[Resource.GLASS, Resource.PAPYRUS]),
        ]
    )
    assert len(result) == 4
    base = {Resource.ORE: 1, Resource.CLAY: 1}
    assert {**base, Resource.WOOD: 1, Resource.GLASS: 1} in result
    assert {**base, Resource.WOOD: 1, Resource.PAPYRUS: 1} in result
    assert {**base, Resource.STONE: 1, Resource.GLASS: 1} in result
    assert {**base, Resource.STONE: 1, Resource.PAPYRUS: 1} in result


"""

Tests for _get_trade_options_for_remaining

"""


def test_single_unit_from_left(no_discount_state):
    result = _get_trade_options_for_remaining({Resource.WOOD: 1}, no_discount_state)
    assert {"player1": TradeCost(amount=1, cost=2)} in result
    assert {"player3": TradeCost(amount=1, cost=2)} in result
    assert len(result) == 2


def test_single_unit_discounted_from_left(left_discount_state):
    result = _get_trade_options_for_remaining({Resource.WOOD: 1}, left_discount_state)
    assert {"player1": TradeCost(amount=1, cost=1)} in result
    assert {"player3": TradeCost(amount=1, cost=2)} in result


def test_two_units_from_left_only(no_discount_state):
    """player3 only has 1 WOOD, so taking 2 must come entirely from player1."""
    result = _get_trade_options_for_remaining({Resource.WOOD: 2}, no_discount_state)
    assert {"player1": TradeCost(amount=2, cost=4)} in result
    assert {
        "player1": TradeCost(amount=1, cost=2),
        "player3": TradeCost(amount=1, cost=2),
    } in result
    assert len(result) == 2


def test_two_units_discounted_split(left_discount_state):
    """Taking 1 from discounted left (cost=1) + 1 from right (cost=2) = total 3."""
    result = _get_trade_options_for_remaining({Resource.WOOD: 2}, left_discount_state)
    assert {
        "player1": TradeCost(amount=1, cost=1),
        "player3": TradeCost(amount=1, cost=2),
    } in result
    assert {
        "player1": TradeCost(amount=2, cost=2)
    } in result  # both from discounted left


# --- Multiple resources remaining ---


def test_two_resources_merged_on_same_neighbor(no_discount_state):
    """
    Add ORE to player1 so both WOOD and ORE come from player1.
    Costs should be merged into a single TradeCost, not two entries.
    """
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={
            "player1": TradeRelationship(base_cost=2),
            "player3": TradeRelationship(base_cost=2),
        },
        available_resources={
            "player1": {Resource.WOOD: 2, Resource.ORE: 1},
            "player3": {Resource.WOOD: 1},
        },
    )
    result = _get_trade_options_for_remaining(
        {Resource.WOOD: 1, Resource.ORE: 1}, state
    )
    merged = next(
        (
            r
            for r in result
            if set(r.keys()) == {"player1"} and r["player1"].amount == 2
        ),
        None,
    )
    assert merged is not None
    assert merged["player1"].cost == 4


def test_two_resources_from_different_neighbors(no_discount_state):
    """WOOD from player3, ORE only available at player1."""
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={
            "player1": TradeRelationship(base_cost=2),
            "player3": TradeRelationship(base_cost=2),
        },
        available_resources={
            "player1": {Resource.WOOD: 2, Resource.ORE: 1},
            "player3": {Resource.WOOD: 1},
        },
    )
    result = _get_trade_options_for_remaining(
        {Resource.WOOD: 1, Resource.ORE: 1}, state
    )
    assert {
        "player1": TradeCost(amount=1, cost=2),
        "player3": TradeCost(amount=1, cost=2),
    } in result


# --- Infeasible cases ---


def test_returns_empty_when_resource_unavailable(no_discount_state):
    result = _get_trade_options_for_remaining({Resource.GLASS: 1}, no_discount_state)
    assert result == []


def test_returns_empty_when_count_exceeds_total_supply(no_discount_state):
    """player1 has 2 WOOD, player3 has 1 — asking for 4 is impossible."""
    result = _get_trade_options_for_remaining({Resource.WOOD: 4}, no_discount_state)
    assert result == []


def test_returns_empty_when_one_resource_of_two_unavailable(no_discount_state):
    """WOOD is available but GLASS is not — entire result should be empty."""
    result = _get_trade_options_for_remaining(
        {Resource.WOOD: 1, Resource.GLASS: 1}, no_discount_state
    )
    assert result == []


# --- Edge cases ---


def test_empty_remaining_cost_returns_empty_trade(no_discount_state):
    result = _get_trade_options_for_remaining({}, no_discount_state)
    assert result == [{}]


def test_discount_does_not_apply_to_non_discounted_resource(left_discount_state):
    """GLASS is not in discounted_resources — player1 should charge base_cost."""
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={
            "player1": TradeRelationship(
                base_cost=2,
                discounted_resources={Resource.WOOD},
                discount_cost=1,
            ),
        },
        available_resources={"player1": {Resource.GLASS: 1}},
    )
    result = _get_trade_options_for_remaining({Resource.GLASS: 1}, state)
    assert result == [{"player1": TradeCost(amount=1, cost=2)}]
