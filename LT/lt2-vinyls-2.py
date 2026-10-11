n = int(input())
prices = [int(x) for x in input().split()]
years = [int(x) for x in input().split()]

total = 0
for i in range(n):
    if not (years[i] > 1960):
        continue

    if years[i] < 2000:
        total += prices[i]*1.105**(2024-years[i])
    else:
        total += prices[i]/2 

print(f'{total:.2f}')