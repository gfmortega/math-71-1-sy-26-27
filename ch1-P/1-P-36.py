def solve(x, y):
    if (x, y) == (0, 0):
        return 0
    elif abs(x) == abs(y):
        return 1
    elif (x + y) % 2 == 0:
        return 2
    else:
        return 'IMPOSSIBLE'

a, b = [int(x) for x in input().split()]
c, d = [int(x) for x in input().split()]
print(solve(a - c, b - d))

'''
    Note that whenever you take a diagonal step,
     the value of x+y changes by -2, +0, or +2
    The parity is INVARIANT.

    So, if the parity of (a, b) isn't the same as
     the parity of (c, d), IMPOSSIBLE
     (or, as in this soln, look at the parity of the
      desired displacement; you can prove these
      are equivalent conditions)

    Otherwise, clearly always possible in <= 2 moves.
'''