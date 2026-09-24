n = int(input())
vals = [int(x) for x in input().split()]
qtys = [int(x) for x in input().split()]

total = 0
for qty, val in zip(qtys, vals):
    total += qty * val

print(total)