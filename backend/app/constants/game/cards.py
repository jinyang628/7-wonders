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
    PAPYRUS = "papyrus"


class Effect(StrEnum):
    GAIN_FIVE_COINS = "Gain five coins"
    BUY_BASIC_RESOURCE_FROM_LEFT_WITH_ONE_COIN = (
        "Buy basic resource from left with one coin"
    )
    BUY_BASIC_RESOURCE_FROM_RIGHT_WITH_ONE_COIN = (
        "Buy basic resource from right with one coin"
    )
    BUY_SPECIAL_RESOURCE_FROM_NEIGHBORS_WITH_ONE_COIN = (
        "Buy special resource from neighbors with one coin"
    )
    GENERATES_ONE_BASIC_RESOURCE_PER_TURN = "Generates one basic resource per turn"
    GENERATES_ONE_SPECIAL_RESOURCE_PER_TURN = "Generates one special resource per turn"
    GAIN_ONE_COIN_FOR_EACH_BROWN_CARD_IN_PLAYER_AND_NEIGHBORS_HANDS = (
        "Gain one coin for each brown card in player and neighbors hands"
    )
    GAIN_TWO_COINS_FOR_EACH_GREY_CARD_IN_PLAYER_AND_NEIGHBORS_HANDS = (
        "Gain two coins for each grey card in player and neighbors hands"
    )
    GAIN_ONE_COIN_AND_ONE_POINT_FOR_EACH_YELLOW_CARD_IN_PLAYER_HAND = (
        "Gain one coin and one point for each yellow card in player hand"
    )
    GAIN_ONE_COIN_AND_ONE_POINT_FOR_EACH_BROWN_CARD_IN_PLAYER_HAND = (
        "Gain one coin and one point for each brown card in player hand"
    )
    GAIN_TWO_COINS_AND_TWO_POINTS_FOR_EACH_GREY_CARD_IN_PLAYER_HAND = (
        "Gain two coins and two points for each grey card in player hand"
    )
    GAIN_THREE_COINS_AND_ONE_POINT_FOR_EACH_WONDER_STAGE = (
        "Gain three coins and one point for each wonder stage"
    )


class Science(StrEnum):
    TABLET = "Tablet"
    COMPASS = "Compass"
    GEAR = "Gear"
