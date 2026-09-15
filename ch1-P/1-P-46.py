a, b = [int(x) for x in input().split()]
c, d = [int(x) for x in input().split()]

def solve(a, b, c, d):
    # WLOG assume a <= c
    if not (a <= c):
        (a, b), (c, d) = (c, d), (a, b)
    return c <= b

print(
    solve(a, b, c, d)
)
