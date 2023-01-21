from .card import Card
from .card import rand_card
from .card import card_score

Hand = list[Card]


def rand_start_hands() -> list[Hand]:
    return [[rand_card(), rand_card()]]


def hand_score(hand: Hand) -> int:
    score = 0
    for card in hand:
        score += card_score(card, score)
    return score


def hit_to_hand(hand: Hand) -> Hand:
    return hand + [rand_card()]


# эта функция не проверяет, можно ли сделать сплит, она просто делает это
def split_hand(hand: Hand) -> list[Hand]:
    card1 = hand[0]
    card2 = hand[1]
    return [[card1], [card2]]


def is_win(hand: Hand) -> bool:
    return hand_score(hand) == 21


def is_hand_lose(hand: Hand) -> bool:
    return hand_score(hand) > 21


def print_hand(hand: Hand):
    for card in hand:
        print(card, end=" ")
    print("=", hand_score(hand))


def select_one_hand(hands: list[Hand]) -> Hand:
    if not hands:
        surrender()

    i = 1
    for hand in hands:
        print(f"{i}. ", end=" ")
        print_hand(hand)
        i += 1

    print(" --- ")
    hand_n = int(input("Какую колоду? "))

    while not 0 < hand_n <= len(hands):
        hand_n = int(input("Какую колоду? "))

    hand_n -= 1
    return hands[hand_n]

def surrender():
    print("Пока, вы проиграли!")
    exit()
