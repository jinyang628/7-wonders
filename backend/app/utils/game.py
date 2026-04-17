from itertools import product

from app.constants.game.cards import Resource
from app.constants.game.utils import (CardPurchaseOptions, PlayerTradeState,
                                      PurchaseOption, TradeCost,
                                      TradeRelationship)
from app.models.cards import (Card, ChoiceResource, FixedResource,
                              ResourceProduced)


def _get_trade_combinations_without_cost(
    state: PlayerTradeState, resource: Resource, count: int
) -> list[dict[str, dict[Resource, int]]]:
    """
    Returns all ways to obtain `count` copies of `resource` from neighbors.
    Each result is:
        [
            { left_neighbor_id: { resource: amount_taken }, right_neighbor_id: { resource: amount_taken } },
            { left_neighbor_id: { resource: amount_taken }, right_neighbor_id: { resource: amount_taken } },
            ...
        ]
    Only includes neighbors that actually have the resource.
    """
    # Build list of (neighbor_id, available_amount) for neighbors who have the resource
    sources = [
        (neighbor_id, resources.get(resource, 0))
        for neighbor_id, resources in state.available_resources.items()
        if resources.get(resource, 0) > 0
    ]

    combinations = []

    def backtrack(
        source_idx: int, remaining: int, current: dict[str, dict[Resource, int]]
    ):
        if remaining == 0:
            combinations.append({k: dict(v) for k, v in current.items()})
            return
        if source_idx == len(sources):
            return  # ran out of sources but still need more

        neighbor_id, available = sources[source_idx]

        # Try taking `amount` from this neighbor (0 = skip)
        for amount in range(min(available, remaining) + 1):
            if amount > 0:
                current[neighbor_id] = {resource: amount}
            backtrack(source_idx + 1, remaining - amount, current)
            if amount > 0:
                del current[neighbor_id]

    backtrack(0, count, {})
    return combinations


def get_trade_combinations_with_cost(
    state: PlayerTradeState, resource: Resource, count: int
) -> list[dict[str, dict[str, int]]]:
    """
    Returns all ways to obtain `count` copies of `resource` from neighbors, with cost.
    Each result is:
        [
            {
                left_neighbor_id:  TradeCost(amount=2, cost=2),
                right_neighbor_id: TradeCost(amount=1, cost=1),
            },
            ...
        ]
    """
    raw_combinations = _get_trade_combinations_without_cost(state, resource, count)

    result = []
    for combo in raw_combinations:
        costed = {}
        for neighbor_id, resources in combo.items():
            amount = resources[resource]
            relationship: TradeRelationship = state.trade_costs[neighbor_id]
            unit_cost = (
                relationship.discount_cost
                if resource in relationship.discounted_resources
                else relationship.base_cost
            )
            costed[neighbor_id] = TradeCost(
                amount=amount,
                cost=amount * unit_cost,
            )
        result.append(costed)

    return result


def _resolve_resource_permutations(
    produced: list[ResourceProduced],
) -> list[dict[Resource, int]]:
    """
    Expands all choice resources into every possible fixed resource pool.
    e.g. [FixedResource(WOOD), ChoiceResource([STONE, ORE])]
      -> [{WOOD:1, STONE:1}, {WOOD:1, ORE:1}]
    """
    fixed: dict[Resource, int] = {}
    choice_slots: list[list[Resource]] = []

    for p in produced:
        if isinstance(p, FixedResource):
            fixed[p.resource] = fixed.get(p.resource, 0) + 1
        elif isinstance(p, ChoiceResource):
            choice_slots.append(p.resources)

    if not choice_slots:
        return [fixed]

    permutations = []
    for combo in product(*choice_slots):
        pool = dict(fixed)
        for resource in combo:
            pool[resource] = pool.get(resource, 0) + 1
        permutations.append(pool)

    return permutations


def _can_cover_cost_with_pool(
    resource_cost: dict[Resource, int],
    pool: dict[Resource, int],
) -> bool:
    return all(pool.get(r, 0) >= amt for r, amt in resource_cost.items())


def _get_trade_options_for_remaining(
    remaining_cost: dict[Resource, int],
    trade_state: PlayerTradeState,
) -> list[dict[str, TradeCost]]:
    """
    Returns all trade combinations that together cover the remaining_cost.
    Handles multiple resources by taking the cartesian product of per-resource options.
    """
    per_resource_options: list[list[dict[str, TradeCost]]] = []

    for resource, count in remaining_cost.items():
        options = get_trade_combinations_with_cost(trade_state, resource, count)
        if not options:
            return []  # this resource can't be sourced at all
        per_resource_options.append(options)

    # Merge one option per resource into a single trade plan
    merged_options = []
    for combo in product(*per_resource_options):
        merged: dict[str, TradeCost] = {}
        for trade in combo:
            for neighbor_id, trade_cost in trade.items():
                if neighbor_id in merged:
                    merged[neighbor_id] = TradeCost(
                        amount=merged[neighbor_id].amount + trade_cost.amount,
                        cost=merged[neighbor_id].cost + trade_cost.cost,
                    )
                else:
                    merged[neighbor_id] = trade_cost
        merged_options.append(merged)

    return merged_options


def get_purchase_options_for_card(
    card: Card,
    own_resources: list[ResourceProduced],
    trade_state: PlayerTradeState,
    coins: int,
    chain_cards: set[str],  # card names that grant a free build
) -> CardPurchaseOptions:
    options: list[PurchaseOption] = []

    # 1. Chain / free build
    if card.name in chain_cards:
        options.append(PurchaseOption(coin_cost=0, trade={}, method="chain"))

    # 2. Coin-only cost (no resource cost)
    if not card.resource_cost and card.coin_cost > 0 and coins >= card.coin_cost:
        options.append(
            PurchaseOption(coin_cost=card.coin_cost, trade={}, method="coin")
        )

    # 3. Free (own resources cover everything, card.coin_cost still applies)
    if card.resource_cost and coins >= card.coin_cost:
        for pool in _resolve_resource_permutations(own_resources):
            if _can_cover_cost_with_pool(card.resource_cost, pool):
                options.append(
                    PurchaseOption(coin_cost=card.coin_cost, trade={}, method="free")
                )
                break  # one free option is enough — permutations are interchangeable

    # 4. Trade (own resources cover part, buy the rest from neighbors)
    if card.resource_cost and coins >= card.coin_cost:
        for pool in _resolve_resource_permutations(own_resources):
            remaining = {
                r: max(0, amt - pool.get(r, 0))
                for r, amt in card.resource_cost.items()
                if amt - pool.get(r, 0) > 0
            }
            if not remaining:
                continue  # already handled by "free" branch

            trade_options = _get_trade_options_for_remaining(remaining, trade_state)
            for trade in trade_options:
                trade_total = sum(tc.cost for tc in trade.values())
                total_coins = card.coin_cost + trade_total
                if coins >= total_coins:
                    options.append(
                        PurchaseOption(
                            coin_cost=total_coins,
                            trade=trade,
                            method="trade",
                        )
                    )

    # Deduplicate — same trade plan can appear from different choice resource permutations
    seen = set()
    unique_options = []
    for opt in options:
        key = (
            opt.method,
            opt.coin_cost,
            frozenset((n, tc.amount, tc.cost) for n, tc in opt.trade.items()),
        )
        if key not in seen:
            seen.add(key)
            unique_options.append(opt)

    return CardPurchaseOptions(
        card=card,
        options=unique_options,
        is_purchasable=bool(unique_options),
    )


def get_purchase_options_for_each_card(
    cards: list[Card],
    own_resources: list[ResourceProduced],
    trade_state: PlayerTradeState,
    coins: int,
    chain_cards: set[str],
) -> list[CardPurchaseOptions]:
    return [
        get_purchase_options_for_card(
            card, own_resources, trade_state, coins, chain_cards
        )
        for card in cards
    ]


# """

# Possible purchase options:

# # Can buy without paying anyone
# [{
#     "left_neighbor_id": 0,
#     "right_neighbor_id": 0,
# }]

# # Cannot buy even if you pay neighbors
# [{
#     "left_neighbor_id": -1,
#     "right_neighbor_id": -1,
# }]

# # Can buy with neighbors' resources (list all possible combinations of coins to pay)
# [
#     {
#         "left_neighbor_id": 0,
#         "right_neighbor_id": 2,
#     },
#     {
#         "left_neighbor_id": 1,
#         "right_neighbor_id": 0,
#     },
# """


# def get_purchase_options(
#     existing_resources: dict[ResourceProduced, int],
#     neighbor_existing_resources: dict[str, dict[ResourceProduced, int]],
#     trade_discount: dict[str, bool],
#     existing_coins: int,
#     target_card: Card,
# ) -> list[dict[str, int]]:
#     resource_cost: dict[Resource, int] = target_card.resource_cost
#     self_resource_combinations: list[dict[Resource, int]] = get_available_resource_combinations(
#         existing_resources
#     )
#     neighbor_ids = neighbor_existing_resources.keys()
#     neighbor_resource_combinations: dict[str, list[dict[Resource, int]]] = {
#         neighbor_id: get_available_resource_combinations(neighbor_existing_resources[neighbor_id])
#         for neighbor_id in neighbor_ids
#     }
#     for resource_combination in self_resource_combinations:
#         # Can buy without paying anyone
#         if all(resource_combination[key] >= freq for key, freq in resource_cost.items()):
#             res = {}
#             for neighbor_id in neighbor_ids:
#                 res[neighbor_id] = 0
#             return res

#         lacked_resources = dict[Resource, int] = {}
#         for key, freq in resource_cost.items():
#             if key not in existing_resources or existing_resources[key] < freq:
#                 lacked_resources[key] = freq - existing_resources[key]
#         for neighbor_id in neighbor_ids:
#             if trade_discount[neighbor_id]:
#                 for resource in lacked_resources:
#                     if resource in neighbor_resource_combinations[neighbor_id]:
#                         neighbor_resource_combinations[neighbor_id][resource] -= 1

#     # for card in existing_cards:
#     #     resource_cost: dict[Resource, int] = target_card.resource_cost
#     #
#     #     for resource_combination in self_resource_combinations:
#     #         if all(resource_combination[key] >= freq for key, freq in resource_cost.items()):
#     #             return True

#     #     lacked_resources = dict[ResourceProduced, int] = {}
#     #     for key, freq in resource_cost.items():
#     #         if key not in existing_resources or existing_resources[key] < freq:
#     #             can_purchase_with_own_resources = False


# def get_available_resource_combinations(
#     resources_produced: dict[ResourceProduced, int],
# ) -> list[dict[Resource, int]]:
#     resources_produced_lst: list[(ResourceProduced, int)] = [
#         (key, freq) for key, freq in resources_produced.items()
#     ]
#     result: list[dict[Resource, int]] = []

#     def backtrack(idx: int, path: dict[Resource, int]) -> None:
#         if idx == len(resources_produced_lst):
#             path_copy = path.copy()
#             result.append(path_copy)
#             return

#         if resources_produced_lst[idx] is FixedResource:
#             path[resources_produced_lst[idx].resource] += 1
#             backtrack(idx + 1, path)
#         else:
#             for resource in resources_produced_lst[idx].resources:
#                 path[resource] += 1
#                 backtrack(idx + 1, path)
#                 path[resource] -= 1

#     return result
