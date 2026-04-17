from dataclasses import dataclass, field
from enum import StrEnum

from app.constants.game.cards import Resource


class Direction(StrEnum):
    LEFT = "left"
    RIGHT = "right"


@dataclass
class TradeRelationship:
    base_cost: int = 2
    discounted_resources: set[Resource] = field(default_factory=set)
    discount_cost: int = 1


"""
player2_trade = PlayerTradeState(
    player_id="player2",
    trade_costs={
        "player1": TradeRelationship(
            base_cost=2,
            discounted_resources={Resource.WOOD, Resource.STONE},  # e.g. West Trading Post
            discount_cost=1
        ),
        "player3": TradeRelationship(base_cost=2)
    },
    available_resources={
        "player1":  {Resource.WOOD: 2, Resource.CLAY: 1},
        "player3": {Resource.ORE: 1, Resource.GLASS: 1}
    }
)
"""


@dataclass
class PlayerTradeState:
    player_id: str
    trade_costs: dict[str, TradeRelationship]
    available_resources: dict[str, dict[Resource, int]]


@dataclass
class PlayerPositionState:
    player_id: str
    neighbors: dict[Direction, str]
