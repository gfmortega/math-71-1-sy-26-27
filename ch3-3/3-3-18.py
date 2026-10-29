from collections import defaultdict
from string import ascii_lowercase

n = int(input())
grid = [
    input()
    for _ in range(n)
]

# from collections import Counter
# tally = Counter(
#     c
#     for row in grid
#     for c in row
# )
# print(*tally.items())

tally = defaultdict(int)
for row in grid:
    for c in row:
        tally[c] += 1

# initialized lazily, make empty list only when needed
# by_frequency = {
#     0: [],
#     1: [],
#     2: [],
#     ...
# }
by_frequency = defaultdict(list)
for letter in ascii_lowercase:
    by_frequency[tally[letter]].append(letter)

for f, letters in sorted(by_frequency.items()):
    formatted_letters = ' '.join(letters)
    print(f'{f}: {formatted_letters}')

# POSSIBLE SOLUTION, maybe a bit messy
# # HANDLE 0 SEPARATELY
# for f in [1, 2, 3, ..., max(tally.values())]:
#     # get all letters whose frequency is f
#     letters = []
#     for key, value in tally.items():
#         if value == f:
#             letters.append(key)
#     letters.sort()

#     if letters:
#         formatted_letters = ' '.join(letters)
#         print(f'{f}: {formatted_letters}')