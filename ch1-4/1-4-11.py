def card_to_value(c):
    if c == '2':
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
    
raw_hand = input().split()
hand = [
    card_to_value(raw_hand[0]),
    card_to_value(raw_hand[1]),
    card_to_value(raw_hand[2]),
    card_to_value(raw_hand[3]),
    card_to_value(raw_hand[4]),
]
hand.sort()

print(
    (1 <= hand[1] - hand[0] <= 2) and
    (1 <= hand[2] - hand[1] <= 2) and
    (1 <= hand[3] - hand[2] <= 2) and
    (1 <= hand[4] - hand[3] <= 2)
)