n, m = [int(x) for x in input().split()]
names = input().split()

friend_count = {
    name: 0
    for name in names
}
for _ in range(m):
    u, v = input().split()
    friend_count[u] += 1
    friend_count[v] += 1

for name, count in sorted(friend_count.items()):
    print(name, count)