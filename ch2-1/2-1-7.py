n = int(input())
numbers = [int(x) for x in input().split()]

odds = []
for num in numbers:
    if num % 2 == 1:
        odds.append(num)

evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(*sorted(odds))
print(*sorted(evens))