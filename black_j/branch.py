from typing import TypeVar

from black_j.card import card_nominal

from black_j.hand import is_hand_disabled
from black_j.hand import select_one_hand
from black_j.hand import split_hand
from black_j.hand import surrender_hand
from black_j.hand import hit_to_hand
from black_j.hand import is_hand_lose


def branches_for_some_hands(hands):
    hand = select_one_hand(hands)
    hands.remove(hand)

    hand_branches = branches_for_one_hand(hand)
    branches = []

    for hand_branch in hand_branches:
        branch_name, branch_hands = hand_branch
        branches += [(branch_name, branch_hands + hands)]

    return branches


def branches_for_one_hand(hand):
    if is_hand_disabled(hand):
        return [("Ничего не делать", [hand])]

    branches = []
    branches += [("Карту", [hit_to_hand(hand)])]
    branches += [("Хватит", [surrender_hand(hand)])]

    if len(hand) == 2 and card_nominal(hand[0]) == card_nominal(hand[1]):
        branches += [("Разбить руку на 2", split_hand(hand))]

    return branches


def select_branch(branches):
    if len(branches) == 1:
        return branches[0]

    i = 1
    for branch in branches:
        print(f" {i}. ", end=" ")
        print(branch[0])
        i +=  1

    print(" --- ")
    q = input("Что делать? ")

    if q == "win":
        print("Уго, поздравляю, вы выиграли!")
        exit()

    action_n = int(q)

    while not 0 < action_n <= len(branches):
        action_n = int(input("Чтоо делать? "))

    return branches[action_n - 1]
