n, m = [int(x) for x in input().split()]
A = set([int(x) for x in input().split()])
B = set([int(x) for x in input().split()])

intersection = set()
for x in A:
    if x in B:
        intersection.add(x)

if intersection:
    print(*sorted(intersection))
else:
    print('empty set')
