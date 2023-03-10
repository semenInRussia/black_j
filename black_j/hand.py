from pickle import loads
from typing import Union

from black_j.card import rand_card
from black_j.card import card_score


def rand_start_hands():
    return [[rand_card(), rand_card()]]


def hand_score(hand):
    score = 0
    for card in hand:
        if card != "surrender":
            score += card_score(card, score)
    return score


def hit_to_hand(hand):
    return hand + [rand_card()]


# эта функция не проверяет, можно ли сделать сплит, она просто делает это
def split_hand(hand):
    card1 = hand[0]
    card2 = hand[1]
    return [[card1], [card2]]


def is_hand_win(hand):
    return hand_score(hand) == 21


def is_hand_lose(hand):
    return hand_score(hand) > 21


def print_hand(hand):
    for card in hand:
        if card != "surrender":
            print(card, end=" ")
    print("=", hand_score(hand))


def print_some_hands(hands):
    for i in range(len(hands)):
        print(f" {i+1}. ", end=" ")
        print_hand(hands[i])


def sort_hands(hands):
    enabled = []
    disabled = []
    for hand in hands:
        if is_hand_disabled(hand):
            disabled += [hand]
        else:
            enabled += [hand]
    return enabled + disabled


def select_one_hand(hands):
    if len(hands) == 0:
        return []
    elif len(hands) == 1:
        return hands[0]

    hands = sort_hands(hands)

    i = 1
    for hand in hands:
        if is_hand_disabled(hand):
            print("- ", end="")
            print_hand(hand)
        else:
            print(f"{i}. ", end="")
            print_hand(hand)
            i += 1

    print(" --- ")
    hand_n = int(input("Какую колоду? "))

    while not 0 < hand_n <= len(hands):
        hand_n = int(input("Какую колоду? "))

    hand_n -= 1
    return hands[hand_n]


# чем больше тем лучше
def hand_game_score(hand):
    if is_hand_lose(hand):
        return 21 - hand_score(hand)
    else:
        return hand_score(hand)


def is_hand_better_then(it, other):
    it_score = hand_game_score(it)
    other_score = hand_game_score(other)
    return it_score > other_score


def are_hands_the_same(it, other):
    it_score = hand_game_score(it)
    other_score = hand_game_score(other)
    return it_score == other_score


def surrender_hand(hand):
    return hand + ["surrender"]


def is_surrender_hand(hand):
    return hand[-1] == "surrender"


def is_hand_enabled(hand):
    return not is_hand_disabled(hand)


def is_hand_disabled(hand):
    return is_surrender_hand(hand) or is_hand_lose(hand) or is_hand_win(hand)


def all_hands_disabled(hands):
    for hand in hands:
        if is_hand_enabled(hand):
            return False
    return True
