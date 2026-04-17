import uuid

from pydantic import BaseModel, Field

from app.constants.game.cards import Age, Effect, Resource, Science


class Card(BaseModel):
    id: str = Field(
        default_factory=lambda: uuid.uuid4().hex,
        description="The unique identifier of the card",
    )
    name: str
    age: Age
    coin_cost: int = Field(default=0, description="The cost of the card in coins")
    resource_cost: dict[Resource, int] = Field(
        default_factory=dict, description="The cost of the card in resources"
    )


class ResourceProduced(BaseModel):
    pass


class FixedResource(ResourceProduced):
    resource: Resource


class ChoiceResource(ResourceProduced):
    resources: list[Resource]


class BrownCard(Card):
    resource_produced: list[ResourceProduced]


class GreyCard(Card):
    resource_produced: list[ResourceProduced]


class BlueCard(Card):
    victory_points: int = Field(
        description="The number of victory points the card earns"
    )


class YellowCard(Card):
    effect: Effect


class RedCard(Card):
    military_strength: int


class GreenCard(Card):
    science: Science
