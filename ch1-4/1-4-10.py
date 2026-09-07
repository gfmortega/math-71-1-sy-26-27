def card_to_value(c):
    return 'A23456789TJQK'.index(c)

def read_input():
    a, b, c, d, e = input().split()
    return (
        card_to_value(a),
        card_to_value(b),
        card_to_value(c),
        card_to_value(d),
        card_to_value(e),
    )

def solve():
    # assume these are integers
    a, b, c, d, e = sorted(read_input())
    if [a, b, c, d, e] == [0, 9, 10, 11, 12]:
        return True

    return (
        a+1 == b and
        b+1 == c and
        c+1 == d and
        d+1 == e
    )

print(solve())