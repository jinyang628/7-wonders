from app.constants.game.cards import Resource
from app.constants.game.utils import (PlayerTradeState, TradeCost,
                                      TradeRelationship)


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


# from app.models.cards import Card, FixedResource, ResourceProduced
# from app.constants.game.cards import CHAINING, Resource

# """
# Returns a dictionary of purchase options for each card.
# Key is the card id, value is the purchase options illustrated in get_purchase_options.
# """


# def get_purchase_options_for_each_card(
#     cards: list[Card],
#     existing_resources: dict[ResourceProduced, int],
#     neighbor_existing_resources: dict[str, dict[ResourceProduced, int]],
#     existing_coins: int,
# ) -> dict[str, list[dict[str, int]]]:
#     result: dict[str, list[dict[str, int]]] = {}
#     for card in cards:
#         result[card.id] = get_purchase_options(
#             existing_resources,
#             neighbor_existing_resources,
#             existing_coins,
#             card,
#         )
#     return result


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
