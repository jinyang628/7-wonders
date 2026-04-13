from pydantic import BaseModel, Field

from app.constants.game.cards import Age, Effect, Resource, Science


class Card(BaseModel):
    name: str
    age: Age
    coin_cost: int = Field(default=0, description="The cost of the card in coins")
    resource_cost: dict[Resource, int] = Field(
        default=dict, description="The cost of the card in resources"
    )


class BrownCard(Card):
    resource_produced: Resource


class GreyCard(Card):
    resource_produced: Resource


class BlueCard(Card):
    victory_points: int = Field(
        default=0, description="The number of victory points the card earns"
    )


class YellowCard(Card):
    effect: Effect


class RedCard(Card):
    military_strength: int


class GreenCard(Card):
    science: Science
