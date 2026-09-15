from math import acos, degrees

def d(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def included_angle(a, b, c):
    cosC = (a**2 + b**2 - c**2)/(2*a*b)
    return degrees(acos(cosC))

pt1 = [int(x) for x in input().split()]
pt2 = [int(x) for x in input().split()]
pt3 = [int(x) for x in input().split()]

a = d(pt1, pt2)
b = d(pt2, pt3)
c = d(pt3, pt1)

angles = [
    included_angle(a, b, c),
    included_angle(b, c, a),
    included_angle(c, a, b),
]
angles.sort()

print(f'{angles[0]:.2f}')
print(f'{angles[1]:.2f}')
print(f'{angles[2]:.2f}')