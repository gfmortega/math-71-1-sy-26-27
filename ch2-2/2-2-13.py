n = int(input())
vals = [int(x) for x in input().split()]
qtys = [int(x) for x in input().split()]

total = 0
for i in range(n):
    total += qtys[i] * vals[i]

print(total)