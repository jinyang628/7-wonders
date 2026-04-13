from app.constants.game.cards import Age
from app.models.cards import Card

# Key is the number of players, value is the list of cards used in each age
DECK: dict[int, dict[Age, list[Card]]] = {
    4: {
        Age.ONE: [],
        Age.TWO: [],
        Age.THREE: [],
    }
}
