from enum import IntEnum, StrEnum


class CardType(StrEnum):
    BROWN = "brown"
    BLUE = "blue"
    YELLOW = "yellow"
    RED = "red"
    GREEN = "green"
    PURPLE = "purple"


class CardName(StrEnum):
    LUMBER_YARD = "Lumber Yard"
    ORE_VEIN = "Ore Vein"
    STONE_PIT = "Stone Pit"
    CLAY_POOL = "Clay Pool"
    TIMBER_YARD = "Timber Yard"
    CLAY_PIT = "Clay Pit"
    EXCAVATION = "Excavation"
    GLASSWORKS = "Glassworks"
    PRESS = "Press"
    LOOM = "Loom"
    ALTAR = "Altar"
    THEATER = "Theater"
    WELL = "Well"
    BATHS = "Baths"
    GUARD_TOWER = "Guard Tower"
    BARRACKS = "Barracks"
    STOCKADE = "Stockade"
    SCRIPTORIUM = "Scriptorium"
    APOTHECARY = "Apothecary"
    WORKSHOP = "Workshop"
    TAVERN = "Tavern"
    WEST_TRADING_POST = "West Trading Post"
    EAST_TRADING_POST = "East Trading Post"
    MARKETPLACE = "Marketplace"
    SAWMILL = "Sawmill"
    FOUNDRY = "Foundry"
    QUARRY = "Quarry"
    BRICKYARD = "Brickyard"
    COURTHOUSE = "Courthouse"
    TEMPLE = "Temple"
    STATUE = "Statue"
    AQUEDUCT = "Aqueduct"
    STABLES = "Stables"
    ARCHERY_RANGE = "Archery Range"
    WALLS = "Walls"
    TRAINING_GROUND = "Training Ground"
    DISPENSARY = "Dispensary"
    LABORATORY = "Laboratory"
    LIBRARY = "Library"
    SCHOOL = "School"
    CARAVANSERY = "Caravansery"
    FORUM = "Forum"
    VINEYARD = "Vineyard"
    BAZAAR = "Bazaar"
    GARDENS = "Gardens"
    SENATE = "Senate"
    TOWN_HALL = "Town Hall"
    PANTHEON = "Pantheon"
    PALACE = "Palace"
    ARSENAL = "Arsenal"
    SIEGE_WORKSHOP = "Siege Workshop"
    FORTIFICATIONS = "Fortifications"
    CIRCUS = "Circus"
    CASTRUM = "Castrum"
    UNIVERSITY = "University"
    STUDY = "Study"
    LODGE = "Lodge"
    ACADEMY = "Academy"
    OBSERVATORY = "Observatory"
    LIGHTHOUSE = "Lighthouse"
    HAVEN = "Haven"
    CHAMBER_OF_COMMERCE = "Chamber of Commerce"
    ARENA = "Arena"


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


CHAINING: dict[CardName, list[CardName]] = {
    CardName.WELL: [CardName.STATUE],
    CardName.BATHS: [CardName.AQUEDUCT],
    CardName.ALTAR: [CardName.PANTHEON],
    CardName.THEATER: [CardName.GARDENS],
    CardName.MARKETPLACE: [CardName.CARAVANSERY],
    CardName.CARAVANSERY: [CardName.LIGHTHOUSE],
    CardName.EAST_TRADING_POST: [CardName.FORUM],
    CardName.WEST_TRADING_POST: [CardName.FORUM],
    CardName.FORUM: [CardName.HAVEN],
    CardName.APOTHECARY: [CardName.DISPENSARY, CardName.STABLES],
    CardName.DISPENSARY: [CardName.ARENA, CardName.LODGE],
    CardName.WORKSHOP: [CardName.ARCHERY_RANGE, CardName.LABORATORY],
    CardName.LABORATORY: [CardName.SIEGE_WORKSHOP, CardName.OBSERVATORY],
    CardName.SCRIPTORIUM: [CardName.COURTHOUSE, CardName.LIBRARY],
    CardName.LIBRARY: [CardName.UNIVERSITY, CardName.SENATE],
    CardName.SCHOOL: [CardName.ACADEMY, CardName.STUDY],
    CardName.WALLS: [CardName.FORTIFICATIONS],
    CardName.TRAINING_GROUND: [CardName.CIRCUS],
}
