import sys

from black_j.hand import (
    Hand,
    hit_to_hand,
    is_hand_can_be_splitted,
    is_hand_disabled,
    select_one_hand,
    split_hand,
    surrender_hand,
)

Branch = tuple[str, list[Hand]]


def branches_for_some_hands(hands: list[Hand]) -> list[Branch]:
    """Return list of possible branches for given card hands."""
    hand = select_one_hand(hands)
    hands.remove(hand)

    hand_branches = branches_for_one_hand(hand)
    branches = []

    for hand_branch in hand_branches:
        branch_name, branch_hands = hand_branch
        branches.append((branch_name, branch_hands + hands))
        
    return branches


def branches_for_one_hand(hand: Hand) -> list[Branch]:
    """Return branches of possible upgraded hands for a given hand."""
    if is_hand_disabled(hand):
        return [("Ничего не делать", [hand])]

    branches = [("Карту", [hit_to_hand(hand)]), ("Хватит", [surrender_hand(hand)])]

    if is_hand_can_be_splitted(hand):
        branches.append(("Разбить руку на 2", split_hand(hand)))

    return branches


def select_branch(branches: list[Branch]) -> Branch:
    """Select one of given branches asking from the user."""
    if len(branches) == 1:
        return branches[0]

    i = 1
    for branch in branches:
        print(f" {i}. ", end=" ")
        print(branch[0])
        i += 1

    print(" --- ")
    q = input("Что делать? ")

    if q == "win":
        print("Уго, поздравляю, вы выиграли!")
        sys.exit()

    action_n = int(q)

    while not 0 < action_n <= len(branches):
        action_n = int(input("Чтоо делать? "))

    return branches[action_n - 1]
