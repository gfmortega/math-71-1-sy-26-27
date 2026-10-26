m = int(input())

masses = dict()
for _ in range(m):
    symbol, _mass = input().split()
    mass = float(_mass)
    masses[symbol] = mass

total = 0

n = int(input())
for _ in range(n):
    _qty, symbol = input().split()
    qty = int(_qty)

    total += qty*masses[symbol]

print(f'{total:.2f}')