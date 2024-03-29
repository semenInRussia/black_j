import random
import time

from black_j.branch import branches_for_some_hands, select_branch
from black_j.card import rand_card
from black_j.dealer import dealer_hand_play_out
from black_j.hand import (
    all_hands_disabled,
    are_hands_the_same,
    is_hand_better_then,
    print_hand,
    print_some_hands,
    rand_start_hands,
)


def _sleep():
    time.sleep(random.randint(1, 3))


def play() -> None:
    """Run the game black jack."""
    dealer_hand = [rand_card()]
    _sleep()
    print("> dealer взял пару карт:", end=" ")
    print_hand(dealer_hand)
    hands = rand_start_hands()

    while True:
        if len(hands) == 1:
            _sleep()
            print("> you взял карт:", end=" ")
            print_hand(hands[0])

        if all_hands_disabled(hands):
            _sleep()
            print("> you остановили добор карт")
            break

        possible_actions = branches_for_some_hands(hands)

        _, hands = select_branch(possible_actions)

    _sleep()
    print("> dealer сейчас доберёт пару карт...")
    _sleep()
    dealer_hand = dealer_hand_play_out(dealer_hand)
    print_hand(dealer_hand)

    print("> Считаем очки и выбираем победителя...")
    _sleep()

    user_win_hands = []
    user_lose_hands = []
    draw_hands = []

    for hand in hands:
        if are_hands_the_same(hand, dealer_hand):
            draw_hands.append(hand)
        elif is_hand_better_then(hand, dealer_hand):
            user_win_hands.append(hand)
        else:
            user_lose_hands.append(hand)

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
        print_some_hands(user_lose_hands)

    _sleep()
    if len(user_lose_hands) < len(user_win_hands):
        print("В принципе вы выиграли")
    elif len(user_lose_hands) > len(user_win_hands):
        print("В принципе вы проиграли")
    else:
        print("В принципе ничья")
