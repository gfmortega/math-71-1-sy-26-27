n = int(input())
raw_locations = [int(x) for x in input().split()]
locations = dict()
for x in raw_locations:
    if x not in locations:
        locations[x] = 0
    locations[x] += 1

q = int(input())
for _ in range(q):
    l, k = [int(x) for x in input().split()]

    # for each coord close to l,
    #   is there a station there?
    total = 0
    for coord in range(l-k, l+k +1):
        if coord in locations:
            total += locations[coord]
    print(total)