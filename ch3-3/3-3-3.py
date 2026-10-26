n = int(input())

tallies = dict()
for _ in range(n):
    color = input()
    if color not in tallies:
        tallies[color] = 0
    tallies[color] += 1

total = sum(tallies.values())

# iterates over the key-value pairs
for color, tally in sorted(tallies.items()):
    percentage = 100*tally/total
    print(f'{percentage:.2f}% {color}')