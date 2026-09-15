a1, b1 = [int(x) for x in input().split()]
W1 = int(input())
H1 = int(input())
a2, b2 = [int(x) for x in input().split()]
W2 = int(input())
H2 = int(input())

def solve1D(a, b, c, d):
    # WLOG assume a <= c
    if not (a <= c):
        (a, b), (c, d) = (c, d), (a, b)
    return c <= b

print(
    solve1D(a1, a1+W1, a2, a2+W2) and
    solve1D(b1, b1+H1, b2, b2+H2)
)
