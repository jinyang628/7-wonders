from app.constants.game.cards import Age, CardName, Effect, Resource, Science
from app.models.cards import (BlueCard, BrownCard, Card, ChoiceResource,
                              FixedResource, GreenCard, GreyCard, RedCard,
                              YellowCard)

# Key is the number of players, value is the list of cards used in each age
DECK: dict[int, dict[Age, list[Card]]] = {
    4: {
        Age.ONE: [
            BrownCard(
                name=CardName.LUMBER_YARD,
                resource_produced=[FixedResource(resource=Resource.WOOD)],
            ),
            BrownCard(
                name=CardName.LUMBER_YARD,
                resource_produced=[FixedResource(resource=Resource.WOOD)],
            ),
            BrownCard(
                name=CardName.ORE_VEIN,
                resource_produced=[FixedResource(resource=Resource.ORE)],
            ),
            BrownCard(
                name=CardName.ORE_VEIN,
                resource_produced=[FixedResource(resource=Resource.ORE)],
            ),
            BrownCard(
                name=CardName.STONE_PIT,
                resource_produced=[FixedResource(resource=Resource.STONE)],
            ),
            BrownCard(
                name=CardName.CLAY_POOL,
                resource_produced=[FixedResource(resource=Resource.CLAY)],
            ),
            BrownCard(
                name=CardName.TIMBER_YARD,
                coin_cost=1,
                resource_produced=[
                    ChoiceResource(resources=[Resource.WOOD, Resource.STONE])
                ],
            ),
            BrownCard(
                name=CardName.CLAY_PIT,
                coin_cost=1,
                resource_produced=[
                    ChoiceResource(resources=[Resource.CLAY, Resource.ORE])
                ],
            ),
            BrownCard(
                name=CardName.EXCAVATION,
                coin_cost=1,
                resource_produced=[
                    ChoiceResource(resources=[Resource.STONE, Resource.CLAY])
                ],
            ),
            GreyCard(
                name=CardName.GLASSWORKS,
                resource_produced=[FixedResource(resource=Resource.GLASS)],
            ),
            GreyCard(
                name=CardName.PRESS,
                resource_produced=[FixedResource(resource=Resource.PAPYRUS)],
            ),
            GreyCard(
                name=CardName.LOOM,
                resource_produced=[FixedResource(resource=Resource.CLOTH)],
            ),
            BlueCard(
                name=CardName.ALTAR,
                victory_points=3,
            ),
            BlueCard(
                name=CardName.THEATER,
                victory_points=3,
            ),
            BlueCard(
                name=CardName.WELL,
                victory_points=3,
            ),
            BlueCard(
                name=CardName.BATHS,
                resource_cost={Resource.STONE: 1},
                victory_points=3,
            ),
            RedCard(
                name=CardName.GUARD_TOWER,
                resource_cost={Resource.CLAY: 1},
                military_strength=1,
            ),
            RedCard(
                name=CardName.GUARD_TOWER,
                resource_cost={Resource.CLAY: 1},
                military_strength=1,
            ),
            RedCard(
                name=CardName.BARRACKS,
                resource_cost={Resource.ORE: 1},
                military_strength=1,
            ),
            RedCard(
                name=CardName.STOCKADE,
                resource_cost={Resource.WOOD: 1},
                military_strength=1,
            ),
            GreenCard(
                name=CardName.SCRIPTORIUM,
                resource_cost={Resource.PAPYRUS: 1},
                science=Science.TABLET,
            ),
            GreenCard(
                name=CardName.SCRIPTORIUM,
                resource_cost={Resource.PAPYRUS: 1},
                science=Science.TABLET,
            ),
            GreenCard(
                name=CardName.APOTHECARY,
                resource_cost={Resource.CLOTH: 1},
                science=Science.COMPASS,
            ),
            GreenCard(
                name=CardName.WORKSHOP,
                resource_cost={Resource.GLASS: 1},
                science=Science.GEAR,
            ),
            YellowCard(
                name=CardName.TAVERN,
                effect=Effect.GAIN_FIVE_COINS,
            ),
            YellowCard(
                name=CardName.WEST_TRADING_POST,
                effect=Effect.BUY_BASIC_RESOURCE_FROM_LEFT_WITH_ONE_COIN,
            ),
            YellowCard(
                name=CardName.EAST_TRADING_POST,
                effect=Effect.BUY_BASIC_RESOURCE_FROM_RIGHT_WITH_ONE_COIN,
            ),
            YellowCard(
                name=CardName.MARKETPLACE,
                effect=Effect.BUY_SPECIAL_RESOURCE_FROM_NEIGHBORS_WITH_ONE_COIN,
            ),
        ],
        Age.TWO: [
            BrownCard(
                name=CardName.SAWMILL,
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.WOOD),
                    FixedResource(resource=Resource.WOOD),
                ],
            ),
            BrownCard(
                name=CardName.SAWMILL,
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.WOOD),
                    FixedResource(resource=Resource.WOOD),
                ],
            ),
            BrownCard(
                name=CardName.FOUNDRY,
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.ORE),
                    FixedResource(resource=Resource.ORE),
                ],
            ),
            BrownCard(
                name=CardName.FOUNDRY,
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.ORE),
                    FixedResource(resource=Resource.ORE),
                ],
            ),
            BrownCard(
                name=CardName.QUARRY,
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.STONE),
                    FixedResource(resource=Resource.STONE),
                ],
            ),
            BrownCard(
                name=CardName.QUARRY,
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.STONE),
                    FixedResource(resource=Resource.STONE),
                ],
            ),
            BrownCard(
                name=CardName.BRICKYARD,
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.CLAY),
                    FixedResource(resource=Resource.CLAY),
                ],
            ),
            BrownCard(
                name=CardName.BRICKYARD,
                coin_cost=1,
                resource_produced=[
                    FixedResource(resource=Resource.CLAY),
                    FixedResource(resource=Resource.CLAY),
                ],
            ),
            GreyCard(
                name=CardName.GLASSWORKS,
                resource_produced=[FixedResource(resource=Resource.GLASS)],
            ),
            GreyCard(
                name=CardName.PRESS,
                resource_produced=[FixedResource(resource=Resource.PAPYRUS)],
            ),
            GreyCard(
                name=CardName.LOOM,
                resource_produced=[FixedResource(resource=Resource.CLOTH)],
            ),
            BlueCard(
                name=CardName.COURTHOUSE,
                resource_cost={Resource.CLAY: 2, Resource.CLOTH: 1},
                victory_points=4,
            ),
            BlueCard(
                name=CardName.TEMPLE,
                resource_cost={Resource.WOOD: 1, Resource.CLAY: 1, Resource.GLASS: 1},
                victory_points=4,
            ),
            BlueCard(
                name=CardName.STATUE,
                resource_cost={Resource.ORE: 2, Resource.WOOD: 1},
                victory_points=4,
            ),
            BlueCard(
                name=CardName.AQUEDUCT,
                resource_cost={Resource.STONE: 3},
                victory_points=5,
            ),
            RedCard(
                name=CardName.STABLES,
                resource_cost={Resource.WOOD: 1, Resource.ORE: 1, Resource.CLAY: 1},
                military_strength=2,
            ),
            RedCard(
                name=CardName.ARCHERY_RANGE,
                resource_cost={Resource.WOOD: 2, Resource.ORE: 1},
                military_strength=2,
            ),
            RedCard(
                name=CardName.WALLS,
                resource_cost={Resource.STONE: 3},
                military_strength=2,
            ),
            RedCard(
                name=CardName.TRAINING_GROUND,
                resource_cost={Resource.ORE: 2, Resource.WOOD: 1},
                military_strength=2,
            ),
            GreenCard(
                name=CardName.DISPENSARY,
                resource_cost={Resource.ORE: 2, Resource.GLASS: 1},
                science=Science.COMPASS,
            ),
            GreenCard(
                name=CardName.DISPENSARY,
                resource_cost={Resource.ORE: 2, Resource.GLASS: 1},
                science=Science.COMPASS,
            ),
            GreenCard(
                name=CardName.LABORATORY,
                resource_cost={Resource.CLAY: 2, Resource.PAPYRUS: 1},
                science=Science.GEAR,
            ),
            GreenCard(
                name=CardName.LIBRARY,
                resource_cost={Resource.STONE: 2, Resource.CLOTH: 1},
                science=Science.TABLET,
            ),
            GreenCard(
                name=CardName.SCHOOL,
                resource_cost={Resource.WOOD: 1, Resource.PAPYRUS: 1},
                science=Science.TABLET,
            ),
            YellowCard(
                name=CardName.CARAVANSERY,
                resource_cost={Resource.WOOD: 2},
                effect=Effect.GENERATES_ONE_BASIC_RESOURCE_PER_TURN,
            ),
            YellowCard(
                name=CardName.FORUM,
                resource_cost={Resource.CLAY: 2},
                effect=Effect.GENERATES_ONE_SPECIAL_RESOURCE_PER_TURN,
            ),
            YellowCard(
                name=CardName.VINEYARD,
                effect=Effect.GAIN_ONE_COIN_FOR_EACH_BROWN_CARD_IN_PLAYER_AND_NEIGHBORS_HANDS,
            ),
            YellowCard(
                name=CardName.VINEYARD,
                effect=Effect.GAIN_ONE_COIN_FOR_EACH_BROWN_CARD_IN_PLAYER_AND_NEIGHBORS_HANDS,
            ),
            YellowCard(
                name=CardName.BAZAAR,
                effect=Effect.GAIN_TWO_COINS_FOR_EACH_GREY_CARD_IN_PLAYER_AND_NEIGHBORS_HANDS,
            ),
        ],
        Age.THREE: [
            BlueCard(
                name=CardName.GARDENS,
                resource_cost={Resource.CLAY: 2, Resource.WOOD: 1},
                victory_points=5,
            ),
            BlueCard(
                name=CardName.GARDENS,
                resource_cost={Resource.CLAY: 2, Resource.WOOD: 1},
                victory_points=5,
            ),
            BlueCard(
                name=CardName.SENATE,
                resource_cost={Resource.WOOD: 2, Resource.STONE: 1, Resource.ORE: 1},
                victory_points=6,
            ),
            BlueCard(
                name=CardName.TOWN_HALL,
                resource_cost={Resource.STONE: 3, Resource.GLASS: 1},
                victory_points=6,
            ),
            BlueCard(
                name=CardName.PANTHEON,
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
                name=CardName.PALACE,
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
                name=CardName.ARSENAL,
                resource_cost={
                    Resource.WOOD: 2,
                    Resource.ORE: 1,
                    Resource.CLOTH: 1,
                },
                military_strength=3,
            ),
            RedCard(
                name=CardName.SIEGE_WORKSHOP,
                resource_cost={Resource.CLAY: 3, Resource.WOOD: 1},
                military_strength=3,
            ),
            RedCard(
                name=CardName.FORTIFICATIONS,
                resource_cost={Resource.ORE: 3, Resource.CLAY: 1},
                military_strength=3,
            ),
            RedCard(
                name=CardName.CIRCUS,
                resource_cost={Resource.CLAY: 3, Resource.ORE: 1},
                military_strength=3,
            ),
            RedCard(
                name=CardName.CASTRUM,
                resource_cost={Resource.CLAY: 2, Resource.WOOD: 1, Resource.PAPYRUS: 1},
                military_strength=3,
            ),
            GreenCard(
                name=CardName.UNIVERSITY,
                resource_cost={
                    Resource.WOOD: 2,
                    Resource.GLASS: 1,
                    Resource.PAPYRUS: 1,
                },
                science=Science.TABLET,
            ),
            GreenCard(
                name=CardName.UNIVERSITY,
                resource_cost={
                    Resource.WOOD: 2,
                    Resource.GLASS: 1,
                    Resource.PAPYRUS: 1,
                },
                science=Science.TABLET,
            ),
            GreenCard(
                name=CardName.STUDY,
                resource_cost={
                    Resource.WOOD: 1,
                    Resource.PAPYRUS: 1,
                    Resource.CLOTH: 1,
                },
                science=Science.GEAR,
            ),
            GreenCard(
                name=CardName.LODGE,
                resource_cost={
                    Resource.CLAY: 2,
                    Resource.PAPYRUS: 1,
                    Resource.CLOTH: 1,
                },
                science=Science.COMPASS,
            ),
            GreenCard(
                name=CardName.ACADEMY,
                resource_cost={Resource.STONE: 3, Resource.GLASS: 1},
                science=Science.COMPASS,
            ),
            GreenCard(
                name=CardName.OBSERVATORY,
                resource_cost={Resource.ORE: 2, Resource.GLASS: 1, Resource.CLOTH: 1},
                science=Science.GEAR,
            ),
            YellowCard(
                name=CardName.LIGHTHOUSE,
                resource_cost={Resource.STONE: 1, Resource.GLASS: 1},
                effect=Effect.GAIN_ONE_COIN_AND_ONE_POINT_FOR_EACH_YELLOW_CARD_IN_PLAYER_HAND,
            ),
            YellowCard(
                name=CardName.HAVEN,
                resource_cost={Resource.WOOD: 1, Resource.ORE: 1, Resource.CLOTH: 1},
                effect=Effect.GAIN_ONE_COIN_AND_ONE_POINT_FOR_EACH_BROWN_CARD_IN_PLAYER_HAND,
            ),
            YellowCard(
                name=CardName.HAVEN,
                resource_cost={Resource.WOOD: 1, Resource.ORE: 1, Resource.CLOTH: 1},
                effect=Effect.GAIN_ONE_COIN_AND_ONE_POINT_FOR_EACH_BROWN_CARD_IN_PLAYER_HAND,
            ),
            YellowCard(
                name=CardName.CHAMBER_OF_COMMERCE,
                resource_cost={Resource.CLAY: 2, Resource.PAPYRUS: 1},
                effect=Effect.GAIN_TWO_COINS_AND_TWO_POINTS_FOR_EACH_GREY_CARD_IN_PLAYER_HAND,
            ),
            YellowCard(
                name=CardName.ARENA,
                resource_cost={Resource.CLAY: 2, Resource.ORE: 1},
                effect=Effect.GAIN_THREE_COINS_AND_ONE_POINT_FOR_EACH_WONDER_STAGE,
            ),
        ],
    }
}
