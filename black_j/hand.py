from black_j.card import Card, card_nominal, card_score, rand_card

Hand = list[Card]

def rand_start_hands() -> list[Hand]:
    """Return card hands to start randomly."""
    return [[rand_card(), rand_card()]]


def hand_score(hand: Hand) -> int:
    """Return score of a hand of cards."""
    score = 0
    for card in hand:
        if card != "surrender":
            score += card_score(card, score)
    return score


def hit_to_hand(hand: Hand) -> Hand:
    """Hit a random card to a card hand."""
    return [*hand, rand_card()]


# эта функция не проверяет, можно ли сделать сплит, она просто делает это
def split_hand(hand: Hand) -> list[Hand]:
    """Split a hand into 2 hands.

    Notice that a hand isn't checked with this function, you should ensure that
    hand can be splitted with function `hand.is_hand_can_be_splitted()`
    """
    card1 = hand[0]
    card2 = hand[1]
    return [[card1], [card2]]


def is_hand_win(hand: Hand) -> bool:
    """Return True, if a given hand is winning 100%."""
    return hand_score(hand) == 21


def is_hand_lose(hand: Hand) -> bool:
    """Return True, if a card hand is lose (score greater than 21)."""
    return hand_score(hand) > 21


def print_hand(hand: Hand) -> None:
    """Print a card hand pretty."""
    for card in hand:
        if card != "surrender":
            print(card, end=" ")
    print("=", hand_score(hand))


def print_some_hands(hands: list[Hand]) -> None:
    """Print some card hands pretty."""
    for i in range(len(hands)):
        print(f" {i+1}. ", end=" ")
        print_hand(hands[i])


def sort_hands(hands: list[Hand]) -> list[Hand]:
    """Sort card hands.

    Add awesome hands to front, add bad hands to back.
    """
    enabled = []
    disabled = []
    for hand in hands:
        if is_hand_disabled(hand):
            disabled += [hand]
        else:
            enabled += [hand]
    return enabled + disabled


def select_one_hand(hands: list[Hand]) -> Hand:
    """Ask a hand to return from the user."""
    if len(hands) == 0:
        return []
    if len(hands) == 1:
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
def _hand_game_score(hand: Hand) -> int:
    """Return the game score of a hand.

    Game score means a score which than greater, than better
    """
    if is_hand_lose(hand):
        return 21 - hand_score(hand)
    return hand_score(hand)


def is_hand_better_then(it: Hand, other: Hand) -> bool:
    """Return True if the first card hand is better than second."""
    it_score = _hand_game_score(it)
    other_score = _hand_game_score(other)
    return it_score > other_score


def are_hands_the_same(it: Hand, other: Hand) -> bool:
    """Return True, if two given card hands has the same score."""
    it_score = _hand_game_score(it)
    other_score = _hand_game_score(other)
    return it_score == other_score


def surrender_hand(hand: Hand) -> Hand:
    """Mark a card hand as surrender."""
    return [*hand, "surrender"]


def is_surrender_hand(hand: Hand) -> bool:
    """Return True, if a given card hand is marked as surrender."""
    return hand[-1] == "surrender"


def is_hand_enabled(hand: Hand) -> bool:
    """Return True, if a given card hand can be in the game further.

    It means surrender and isn't lose and isn't win
    """
    return not is_hand_disabled(hand)


def is_hand_disabled(hand: Hand) -> bool:
    """Return True, if a given card hand can't be played further.

    It means that the hand is either win, lose or surrender
    """
    return is_surrender_hand(hand) or is_hand_lose(hand) or is_hand_win(hand)


def all_hands_disabled(hands: Hand) -> bool:
    """Return True, if each of given hands can't be played further."""
    return all(not is_hand_enabled(hand) for hand in hands)


REQUIRED_SAME_NOMINALS_TO_SPLIT = 2


def is_hand_can_be_splitted(hand: Hand) -> bool:
    """Return True, if a given card hand can be splitted."""
    return (
        len(hand) == REQUIRED_SAME_NOMINALS_TO_SPLIT
        and
        card_nominal(hand[0]) == card_nominal(hand[1])
    )
