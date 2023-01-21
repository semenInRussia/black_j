from black_j.branch import branches_for_some_hands
from black_j.branch import select_branch
from black_j.dealer import dealer_hand_play_out

from black_j.hand import are_hands_the_same
from black_j.hand import rand_start_hands
from black_j.hand import print_hand
from black_j.hand import print_some_hands
from black_j.hand import is_hand_better_then
from black_j.hand import Hand
from black_j.hand import all_hands_are_surrender

from black_j.card import rand_card


def play():
    dealer_hand = [rand_card()]
    print("> dealer взял пару карт:", end=" ")
    print_hand(dealer_hand)
    hands = rand_start_hands()

    while True:
        if len(hands) == 1:
            print_hand(hands[0])

        if all_hands_are_surrender(hands):
            break

        possible_actions = branches_for_some_hands(hands)

        _, hands = select_branch(possible_actions)

    print("> dealer сейчас доберёт пару карт...")
    dealer_hand = dealer_hand_play_out(dealer_hand)
    print_hand(dealer_hand)

    print("> Считаем очки и выбираем победителя...")

    user_win_hands: list[Hand] = []
    user_lose_hands: list[Hand] = []
    draw_hands: list[Hand] = []

    for hand in hands:
        if are_hands_the_same(hand, dealer_hand):
            draw_hands += [hand]
        elif is_hand_better_then(hand, dealer_hand):
            user_win_hands += [hand]
        else:
            user_lose_hands += [hand]

    if len(user_win_hands) == 1:
        print("Ваша выигрышная колода")
        print_hand(user_win_hands[0])
    elif len(user_win_hands) > 1:
        print("Ваши выигрышные колоды")
        print_some_hands(user_win_hands)

    if len(user_lose_hands) == 1:
        print("Ваша проигранная колода")
        print_hand(user_lose_hands[0])
    elif len(user_lose_hands) > 1:
        print("Ваши проигранные колоды:")
        print_some_hands(user_win_hands)

    if len(user_lose_hands) < len(user_win_hands):
        print("В принципе вы выиграли")
    elif len(user_lose_hands) > len(user_win_hands):
        print("В принципе вы проиграли")
    else:
        print("В принципе ничья")
