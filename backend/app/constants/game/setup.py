from app.constants.game.cards import Age, Effect, Resource, Science
from app.models.cards import (BlueCard, BrownCard, Card, ChoiceResource,
                              FixedResource, GreenCard, GreyCard, RedCard,
                              YellowCard)

# Key is the number of players, value is the list of cards used in each age
DECK: dict[int, dict[Age, list[Card]]] = {
    4: {
        Age.ONE: [
            BrownCard(
                name="Lumber Yard",
                resource_produced=[FixedResource(resource=Resource.WOOD)],
            ),
            BrownCard(
                name="Lumber Yard",
                resource_produced=[FixedResource(resource=Resource.WOOD)],
            ),
            BrownCard(
                name="Ore Vein",
                resource_produced=[FixedResource(resource=Resource.ORE)],
            ),
            BrownCard(
                name="Ore Vein",
                resource_produced=[FixedResource(resource=Resource.ORE)],
            ),
            BrownCard(
                name="Stone Pit",
                resource_produced=[FixedResource(resource=Resource.STONE)],
            ),
            BrownCard(
                name="Clay Pool",
                resource_produced=[FixedResource(resource=Resource.CLAY)],
            ),
            BrownCard(
                name="Timber Yard",
                coin_cost=1,
                resource_produced=[
                    ChoiceResource(resources=[Resource.WOOD, Resource.STONE])
                ],
            ),
            BrownCard(
                name="Clay Pit",
                coin_cost=1,
                resource_produced=[
                    ChoiceResource(resources=[Resource.CLAY, Resource.ORE])
                ],
            ),
            BrownCard(
                name="Excavation",
                coin_cost=1,
                resource_produced=[
                    ChoiceResource(resources=[Resource.STONE, Resource.CLAY])
                ],
            ),
            GreyCard(
                name="Glassworks",
                resource_produced=[FixedResource(resource=Resource.GLASS)],
            ),
            GreyCard(
                name="Press",
                resource_produced=[FixedResource(resource=Resource.PAPYRUS)],
            ),
            GreyCard(
                name="Loom",
                resource_produced=[FixedResource(resource=Resource.CLOTH)],
            ),
            BlueCard(
                name="Altar",
                victory_points=3,
            ),
            BlueCard(
                name="Theater",
                victory_points=3,
            ),
            BlueCard(
                name="Well",
                victory_points=3,
            ),
            BlueCard(
                name="Baths",
                resource_cost={Resource.STONE: 1},
                victory_points=3,
            ),
            RedCard(
                name="Guard Tower",
                resource_cost={Resource.CLAY: 1},
                military_strength=1,
            ),
            RedCard(
                name="Guard Tower",
                resource_cost={Resource.CLAY: 1},
                military_strength=1,
            ),
            RedCard(
                name="Barracks",
                resource_cost={Resource.ORE: 1},
                military_strength=1,
            ),
            RedCard(
                name="Stockade",
                resource_cost={Resource.WOOD: 1},
                military_strength=1,
            ),
            GreenCard(
                name="Scriptorium",
                resource_cost={Resource.PAPYRUS: 1},
                science=Science.TABLET,
            ),
            GreenCard(
                name="Scriptorium",
                resource_cost={Resource.PAPYRUS: 1},
                science=Science.TABLET,
            ),
            GreenCard(
                name="Apothecary",
                resource_cost={Resource.CLOTH: 1},
                science=Science.COMPASS,
            ),
            GreenCard(
                name="Workshop",
                resource_cost={Resource.GLASS: 1},
                science=Science.GEAR,
            ),
            YellowCard(
                name="Tavern",
                effect=Effect.GAIN_FIVE_COINS,
            ),
            YellowCard(
                name="West Trading Post",
                effect=Effect.BUY_BASIC_RESOURCE_FROM_LEFT_WITH_ONE_COIN,
            ),
            YellowCard(
                name="East Trading Post",
                effect=Effect.BUY_BASIC_RESOURCE_FROM_RIGHT_WITH_ONE_COIN,
            ),
            YellowCard(
                name="Marketplace",
                effect=Effect.BUY_SPECIAL_RESOURCE_FROM_NEIGHBORS_WITH_ONE_COIN,
            ),
        ],
        Age.TWO: [
            BrownCard(
                name="Sawmill",
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.WOOD),
                    FixedResource(resource=Resource.WOOD),
                ],
            ),
            BrownCard(
                name="Sawmill",
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.WOOD),
                    FixedResource(resource=Resource.WOOD),
                ],
            ),
            BrownCard(
                name="Foundry",
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.ORE),
                    FixedResource(resource=Resource.ORE),
                ],
            ),
            BrownCard(
                name="Foundry",
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.ORE),
                    FixedResource(resource=Resource.ORE),
                ],
            ),
            BrownCard(
                name="Quarry",
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.STONE),
                    FixedResource(resource=Resource.STONE),
                ],
            ),
            BrownCard(
                name="Quarry",
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.STONE),
                    FixedResource(resource=Resource.STONE),
                ],
            ),
            BrownCard(
                name="Brickyard",
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.CLAY),
                    FixedResource(resource=Resource.CLAY),
                ],
            ),
            BrownCard(
                name="Brickyard",
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.CLAY),
                    FixedResource(resource=Resource.CLAY),
                ],
            ),
            GreyCard(
                name="Glassworks",
                resource_produced=[FixedResource(resource=Resource.GLASS)],
            ),
            GreyCard(
                name="Press",
                resource_produced=[FixedResource(resource=Resource.PAPYRUS)],
            ),
            GreyCard(
                name="Loom",
                resource_produced=[FixedResource(resource=Resource.CLOTH)],
            ),
            BlueCard(
                name="Courthouse",
                resource_cost={Resource.CLAY: 2, Resource.CLOTH: 1},
                victory_points=4,
            ),
            BlueCard(
                name="Temple",
                resource_cost={Resource.WOOD: 1, Resource.CLAY: 1, Resource.GLASS: 1},
                victory_points=4,
            ),
            BlueCard(
                name="Statue",
                resource_cost={Resource.ORE: 2, Resource.WOOD: 1},
                victory_points=4,
            ),
            BlueCard(
                name="Aqueduct",
                resource_cost={Resource.STONE: 3},
                victory_points=5,
            ),
            RedCard(
                name="Stables",
                resource_cost={Resource.WOOD: 1, Resource.ORE: 1, Resource.CLAY: 1},
                military_strength=2,
            ),
            RedCard(
                name="Archery Range",
                resource_cost={Resource.WOOD: 2, Resource.ORE: 1},
                military_strength=2,
            ),
            RedCard(
                name="Walls",
                resource_cost={Resource.STONE: 3},
                military_strength=2,
            ),
            RedCard(
                name="Training Ground",
                resource_cost={Resource.ORE: 2, Resource.WOOD: 1},
                military_strength=2,
            ),
            GreenCard(
                name="Dispensary",
                resource_cost={Resource.ORE: 2, Resource.GLASS: 1},
                science=Science.COMPASS,
            ),
            GreenCard(
                name="Dispensary",
                resource_cost={Resource.ORE: 2, Resource.GLASS: 1},
                science=Science.COMPASS,
            ),
            GreenCard(
                name="Laboratory",
                resource_cost={Resource.CLAY: 2, Resource.PAPYRUS: 1},
                science=Science.GEAR,
            ),
            GreenCard(
                name="Library",
                resource_cost={Resource.STONE: 2, Resource.CLOTH: 1},
                science=Science.TABLET,
            ),
            GreenCard(
                name="School",
                resource_cost={Resource.WOOD: 1, Resource.PAPYRUS: 1},
                science=Science.TABLET,
            ),
            YellowCard(
                name="Caravansery",
                resource_cost={Resource.WOOD: 2},
                effect=Effect.GENERATES_ONE_BASIC_RESOURCE_PER_TURN,
            ),
            YellowCard(
                name="Forum",
                resource_cost={Resource.CLAY: 2},
                effect=Effect.GENERATES_ONE_SPECIAL_RESOURCE_PER_TURN,
            ),
            YellowCard(
                name="Vineyard",
                effect=Effect.GAIN_ONE_COIN_FOR_EACH_BROWN_CARD_IN_PLAYER_AND_NEIGHBORS_HANDS,
            ),
            YellowCard(
                name="Vineyard",
                effect=Effect.GAIN_ONE_COIN_FOR_EACH_BROWN_CARD_IN_PLAYER_AND_NEIGHBORS_HANDS,
            ),
            YellowCard(
                name="Bazaar",
                effect=Effect.GAIN_TWO_COINS_FOR_EACH_GREY_CARD_IN_PLAYER_AND_NEIGHBORS_HANDS,
            ),
        ],
        Age.THREE: [
            BlueCard(
                name="Gardens",
                resource_cost={Resource.CLAY: 2, Resource.WOOD: 1},
                victory_points=5,
            ),
            BlueCard(
                name="Gardens",
                resource_cost={Resource.CLAY: 2, Resource.WOOD: 1},
                victory_points=5,
            ),
            BlueCard(
                name="Senate",
                resource_cost={Resource.WOOD: 2, Resource.STONE: 1, Resource.ORE: 1},
                victory_points=6,
            ),
            BlueCard(
                name="Town Hall",
                resource_cost={Resource.STONE: 3, Resource.GLASS: 1},
                victory_points=6,
            ),
            BlueCard(
                name="Pantheon",
                resource_cost={
                    Resource.CLAY: 2,
                    Resource.ORE: 1,
                    Resource.GLASS: 1,
                    Resource.PAPYRUS: 1,
                    Resource.CLOTH: 1,
                },
                victory_points=7,
            ),
            BlueCard(
                name="Palace",
                resource_cost={
                    Resource.WOOD: 1,
                    Resource.STONE: 1,
                    Resource.ORE: 1,
                    Resource.CLAY: 1,
                    Resource.GLASS: 1,
                    Resource.PAPYRUS: 1,
                    Resource.CLOTH: 1,
                },
                victory_points=8,
            ),
            RedCard(
                name="Arsenal",
                resource_cost={
                    Resource.WOOD: 2,
                    Resource.ORE: 1,
                    Resource.CLOTH: 1,
                },
                military_strength=3,
            ),
            RedCard(
                name="Siege Workshop",
                resource_cost={Resource.CLAY: 3, Resource.WOOD: 1},
                military_strength=3,
            ),
            RedCard(
                name="Fortifications",
                resource_cost={Resource.ORE: 3, Resource.CLAY: 1},
                military_strength=3,
            ),
            RedCard(
                name="Circus",
                resource_cost={Resource.CLAY: 3, Resource.ORE: 1},
                military_strength=3,
            ),
            RedCard(
                name="Castrum",
                resource_cost={Resource.CLAY: 2, Resource.WOOD: 1, Resource.PAPYRUS: 1},
                military_strength=3,
            ),
            GreenCard(
                name="University",
                resource_cost={
                    Resource.WOOD: 2,
                    Resource.GLASS: 1,
                    Resource.PAPYRUS: 1,
                },
                science=Science.TABLET,
            ),
            GreenCard(
                name="University",
                resource_cost={
                    Resource.WOOD: 2,
                    Resource.GLASS: 1,
                    Resource.PAPYRUS: 1,
                },
                science=Science.TABLET,
            ),
            GreenCard(
                name="Study",
                resource_cost={
                    Resource.WOOD: 1,
                    Resource.PAPYRUS: 1,
                    Resource.CLOTH: 1,
                },
                science=Science.GEAR,
            ),
            GreenCard(
                name="Lodge",
                resource_cost={
                    Resource.CLAY: 2,
                    Resource.PAPYRUS: 1,
                    Resource.CLOTH: 1,
                },
                science=Science.COMPASS,
            ),
            GreenCard(
                name="Academy",
                resource_cost={Resource.STONE: 3, Resource.GLASS: 1},
                science=Science.COMPASS,
            ),
            GreenCard(
                name="Observatory",
                resource_cost={Resource.ORE: 2, Resource.GLASS: 1, Resource.CLOTH: 1},
                science=Science.GEAR,
            ),
            YellowCard(
                name="Lighthouse",
                resource_cost={Resource.STONE: 1, Resource.GLASS: 1},
                effect=Effect.GAIN_ONE_COIN_AND_ONE_POINT_FOR_EACH_YELLOW_CARD_IN_PLAYER_HAND,
            ),
            YellowCard(
                name="Haven",
                resource_cost={Resource.WOOD: 1, Resource.ORE: 1, Resource.CLOTH: 1},
                effect=Effect.GAIN_ONE_COIN_AND_ONE_POINT_FOR_EACH_BROWN_CARD_IN_PLAYER_HAND,
            ),
            YellowCard(
                name="Haven",
                resource_cost={Resource.WOOD: 1, Resource.ORE: 1, Resource.CLOTH: 1},
                effect=Effect.GAIN_ONE_COIN_AND_ONE_POINT_FOR_EACH_BROWN_CARD_IN_PLAYER_HAND,
            ),
            YellowCard(
                name="Chamber of Commerce",
                resource_cost={Resource.CLAY: 2, Resource.PAPYRUS: 1},
                effect=Effect.GAIN_TWO_COINS_AND_TWO_POINTS_FOR_EACH_GREY_CARD_IN_PLAYER_HAND,
            ),
            YellowCard(
                name="Arena",
                resource_cost={Resource.CLAY: 2, Resource.ORE: 1},
                effect=Effect.GAIN_THREE_COINS_AND_ONE_POINT_FOR_EACH_WONDER_STAGE,
            ),
        ],
    }
}
