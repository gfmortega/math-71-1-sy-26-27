n = int(input())
h = [int(x) for x in input().split()]

Q = int(input())
for _ in range(Q):
    # do something Q times
    # what am I doing Q times?
    # solving a 2.1 problem
    L, R, k = [int(x) for x in input().split()]
    # convert from 1-index in statement, to 0-index for code
    L -= 1
    R -= 1

    for t in range(L, R+1):
        if h[t] <= k:
            h[t] = k
        
        # h[t] = max(h[t], k)

print(*h)