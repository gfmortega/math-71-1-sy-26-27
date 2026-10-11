n = int(input())
prices = [int(x) for x in input().split()]
years = [int(x) for x in input().split()]

good_prices = []
good_years = []
for i in range(n):
    if years[i] > 1960:
        good_prices.append(prices[i])       
        good_years.append(years[i])

final_prices = []
for i in range(len(good_prices)):
    if good_years[i] < 2000:
        final_prices.append(good_prices[i]*1.105**(2024 - good_years[i]))
    else:
        final_prices.append(good_prices[i] / 2)


total = sum(final_prices)
print(f'{total:.2f}')