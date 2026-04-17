import pytest

from app.constants.game.cards import Resource
from app.constants.game.utils import PlayerTradeState, TradeRelationship
from app.utils.game import get_trade_combinations


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
    result = get_trade_combinations(one_neighbor_state, Resource.WOOD, 1)
    assert result == [{"player1": {Resource.WOOD: 1}}]


def test_take_multiple_from_single_source(one_neighbor_state):
    result = get_trade_combinations(one_neighbor_state, Resource.WOOD, 2)
    assert result == [{"player1": {Resource.WOOD: 2}}]


def test_split_across_neighbors_multiple(two_neighbor_state):
    result = get_trade_combinations(two_neighbor_state, Resource.WOOD, 2)
    assert {"player1": {Resource.WOOD: 2}} in result
    assert {"player1": {Resource.WOOD: 1}, "player3": {Resource.WOOD: 1}} in result
    assert len(result) == 2


def test_split_across_neighbors_single(two_neighbor_state):
    result = get_trade_combinations(two_neighbor_state, Resource.WOOD, 1)
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
    result = get_trade_combinations(state, Resource.WOOD, 1)
    assert result == []


def test_returns_empty_when_count_exceeds_supply(one_neighbor_state):
    result = get_trade_combinations(one_neighbor_state, Resource.WOOD, 3)
    assert result == []


def test_returns_empty_when_no_neighbors():
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={},
        available_resources={},
    )
    result = get_trade_combinations(state, Resource.WOOD, 1)
    assert result == []


# --- Edge cases ---


def test_count_zero_returns_empty_combination():
    state = PlayerTradeState(
        player_id="player2",
        trade_costs={"player1": TradeRelationship()},
        available_resources={"player1": {Resource.WOOD: 2}},
    )
    result = get_trade_combinations(state, Resource.WOOD, 0)
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
    result = get_trade_combinations(state, Resource.WOOD, 1)
    assert result == [{"player3": {Resource.WOOD: 1}}]
    assert all("player1" not in combo for combo in result)


def test_no_duplicate_combinations(two_neighbor_state):
    result = get_trade_combinations(two_neighbor_state, Resource.WOOD, 2)
    seen = [
        frozenset((k, v[Resource.WOOD]) for k, v in combo.items()) for combo in result
    ]
    assert len(seen) == len(set(seen))
