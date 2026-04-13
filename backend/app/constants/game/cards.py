from enum import IntEnum, StrEnum


class CardType(StrEnum):
    BROWN = "brown"
    BLUE = "blue"
    YELLOW = "yellow"
    RED = "red"
    GREEN = "green"
    PURPLE = "purple"


class Age(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


class Resource(StrEnum):
    CLAY = "clay"
    STONE = "stone"
    ORE = "ore"
    WOOD = "wood"
    GLASS = "glass"
    CLOTH = "cloth"
    Papyrus = "papyrus"


class Effect(StrEnum):
    GAIN_5_COINS = "Gain 5 coins"
    # TODO: Fill up everything according to list and case on cost accordingly


class Science(StrEnum):
    TABLET = "Tablet"
    COMPASS = "Compass"
    GEAR = "Gear"
