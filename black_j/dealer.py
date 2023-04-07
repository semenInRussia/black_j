from black_j.hand import Hand, hand_score, hit_to_hand

DEALER_HAND_LIMIT = 17

def dealer_hand_play_out(hand: Hand) -> Hand:
    """Hand out a given hand to the end.

    Where the end means that the hand score is greater or equal than/to 17
    """
    while hand_score(hand) < DEALER_HAND_LIMIT:
        hand = hit_to_hand(hand)
    return hand
