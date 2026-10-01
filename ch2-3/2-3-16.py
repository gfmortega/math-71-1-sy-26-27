n, s, k = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

pos = s
for _ in range(k):
    # "Do a jump" k time
    pos = d[pos-1]

print(f'Location: {pos}')
