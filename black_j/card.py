import random


MAX_DIGIT_NOMINAL = 10

HEARTS = "^"
DIAMONDS = "/"
CLUBS = "|"
SPADES = "_"


def rand_suit():
    mouth = random.randint(1, 4)
    if mouth == 1:
        return DIAMONDS
    elif mouth == 2:
        return CLUBS
    elif mouth == 3:
        return SPADES
    elif mouth == 4:
        return HEARTS
    else:
        print("недолжно случится")
        return ""


def rand_nominal():
    n = random.randint(1, MAX_DIGIT_NOMINAL+3)
    if n == 1:
        return "A"
    elif n == MAX_DIGIT_NOMINAL+1:
        return "J"
    elif n == MAX_DIGIT_NOMINAL+2:
        return "Q"
    elif n == MAX_DIGIT_NOMINAL+3:
        return "K"
    else:
        return str(n)


def card_nominal(card):
    return card[:-1]


def card_score(card, score=0):
    n = card_nominal(card)
    if n == "A" and score <= 10:
        return 11
    elif n == "A" and score > 10:
        return 1
    elif n == "Q" or n == "K" or n == "J":
        return 10
    else:
        return int(n)


def rand_card():
    nominal = rand_nominal()
    suit = rand_suit()
    return nominal + suit
