def parse_point(line):
    return [int(x) for x in line.split()]

def radius_squared(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return (x1 - x2)**2 + (y1 - y2)**2

h, k = parse_point(input())
a, b = parse_point(input())
x, y = parse_point(input())

r2 = radius_squared((h, k), (a, b))
print(f'(x-{h})^2 + (y-{k})^2 = {r2}')

if (x - h)**2 + (y - k)**2 < r2:
    answer = 'INSIDE'
elif (x - h)**2 + (y - k)**2 == r2:
    answer = 'ON THE CIRCLE'
else:
    answer = 'OUTSIDE'
print(answer)