from black_j.hand import hand_score
from black_j.hand import hit_to_hand


def dealer_hand_play_out(hand):
    while hand_score(hand) < 17:
        hand = hit_to_hand(hand)
    return hand
