def card_to_value(c, ace_is_low=True):
    if c == 'A':
        return 1 if ace_is_low else 14
    elif c == '2':
        return 2
    elif c == '3':
        return 3
    elif c == '4':
        return 4
    elif c == '5':
        return 5
    elif c == '6':
        return 6
    elif c == '7':
        return 7
    elif c == '8':
        return 8
    elif c == '9':
        return 9
    elif c in 'T':
        return 10
    elif c in 'J':
        return 11
    elif c in 'Q':
        return 12
    elif c in 'K':
        return 13
    else:
        raise RuntimeError('Impossible case')
    
def is_straight(raw_hand, ace_is_low=True):
    hand = [
        card_to_value(raw_hand[0], ace_is_low),
        card_to_value(raw_hand[1], ace_is_low),
        card_to_value(raw_hand[2], ace_is_low),
        card_to_value(raw_hand[3], ace_is_low),
        card_to_value(raw_hand[4], ace_is_low),
    ]
    hand.sort()
    return (
        (1 <= hand[1] - hand[0] <= 2) and
        (1 <= hand[2] - hand[1] <= 2) and
        (1 <= hand[3] - hand[2] <= 2) and
        (1 <= hand[4] - hand[3] <= 2)
    )

raw_hand = input().split()
print(is_straight(raw_hand, True) or is_straight(raw_hand, False))
