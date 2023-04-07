import random

Card = str

MAX_DIGIT_NOMINAL = 10

HEARTS = "^"
DIAMONDS = "/"
CLUBS = "|"
SPADES = "_"

Suit = HEARTS | DIAMONDS | CLUBS | SPADES
Nominal = ("1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10"
           | "A" | "Q" | "K")

def rand_suit() -> Suit:
    """Return a random card suit (either Heart, Diamonds, Clubs or Spadeds)."""
    mouth = random.randint(0, 3)
    return [HEARTS, DIAMONDS, CLUBS, SPADES][mouth]


def rand_nominal() -> Nominal:
    """Return a random card nominal."""
    n = random.randint(1, MAX_DIGIT_NOMINAL + 3)
    if n == 1:
        return "A"
    if n == MAX_DIGIT_NOMINAL + 1:
        return "J"
    if n == MAX_DIGIT_NOMINAL + 2:
        return "Q"
    if n == MAX_DIGIT_NOMINAL + 3:
        return "K"
    return str(n)


def card_nominal(card: Card) -> Nominal:
    """Return the nominal of a given card."""
    return card[:-1]


def card_score(card: Card, score: int = 0) -> int:
    """Return the score of a given card.

    You should pass the already scored score
    """
    n = card_nominal(card)
    if n == "A" and score <= 10:
        return 11
    if n == "A" and score > 10:
        return 1
    if n == "Q" or n == "K" or n == "J":
        return 10
    return int(n)


def rand_card() -> Card:
    """Return a random card."""
    nominal = rand_nominal()
    suit = rand_suit()
    return nominal + suit
