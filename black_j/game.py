from black_j.branch import branches_for_some_hands, select_branch
from .hand import rand_start_hands
from .hand import print_hand

def play():
    hands = rand_start_hands()

    while True:
        if len(hands) == 1:
            print_hand(hands[0])
        possible_actions = branches_for_some_hands(hands)

        # проиграл или выиграл
        if possible_actions == []:
            break

        branch_name, hands = select_branch(possible_actions)
