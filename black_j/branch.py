from typing import TypeVar

from .card import card_nominal

from .hand import Hand
from .hand import select_one_hand
from .hand import split_hand
from .hand import hit_to_hand
from .hand import is_hand_lose


T = TypeVar("T")
Branch = tuple[str, list[Hand]]

def branches_for_some_hands(hands: list[Hand]) -> list[Branch]:
    if len(hands) == 1:
        hand = hands[0]
    else:
        hand = select_one_hand(hands)
    hands.remove(hand)
    hand_branches = branches_for_one_hand(hand)
    branches = []

    for hand_branch in hand_branches:
        branch_name, branch_hands = hand_branch
        branches.append((branch_name, branch_hands + hands))

    return branches


def branches_for_one_hand(hand: Hand) -> list[Branch]:
    if is_hand_lose(hand):
        return [("Убрать руку", [])]

    branches: list[Branch] = []
    branches += [("Карту", [hit_to_hand(hand)])]
    branches += [("Хватит", [])]

    if len(hand) == 2 and card_nominal(hand[0]) == card_nominal(hand[1]):
        branches += [("Разбить руку на 2", split_hand(hand))]

    return branches


def select_branch(branches: list[Branch]) -> Branch:
    if len(branches) == 1:
        return branches[0]

    i = 1
    for branch in branches:
        print(f" {i}. ", end=" ")
        print(branch[0])        # name
        i +=  1

    print(" --- ")
    q = input("Что делать? ")

    if q == "win":
        print("Уго, поздравляю, вы выиграли!")

    action_n = int(q)

    while not 0 < action_n <= len(branches):
        action_n = int(input("Что делать? "))

    return branches[action_n - 1]
