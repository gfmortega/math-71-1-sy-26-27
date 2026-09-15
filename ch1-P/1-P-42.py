x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
x3, y3 = [int(x) for x in input().split()]
x4, y4 = [int(x) for x in input().split()]

print(
    (y2 - y1)*(y4 - y3) == -(x4 - x3)*(x2 - x1)
)

'''
    Uses the fact from HS precalc that the line
     perpendicular to a given one has a slope
     that is the negative reciprocal.

    Does some algebraic rearranging to avoid
     floating point operations.
     (This is also basically usin the cross product, if you know that)
'''