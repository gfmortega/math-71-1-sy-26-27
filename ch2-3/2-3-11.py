n, m = [int(x) for x in input().split()]

# what I want is n counters, initialized to 0, one for each user
friend_count = [0 for _ in range(n)]

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    u -= 1
    v -= 1

    friend_count[u] += 1
    friend_count[v] += 1

print(*friend_count)