n = int(input())
locations = set([int(x) for x in input().split()])

q = int(input())
for _ in range(q):
    l, k = [int(x) for x in input().split()]

    # # for each station, is it close to l
    # total = 0
    # for x in xs:
    #     if abs(x - l) <= k:
    #         total += 1
            
    # for each coord close to l,
    #   is there a station there?
    total = 0
    for coord in range(l-k, l+k +1):
        if coord in locations:
            total += 1
    print(total)