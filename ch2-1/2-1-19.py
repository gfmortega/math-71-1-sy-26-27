n = int(input())
cards = []
# do something n times
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

filtered = []
top_value, top_suit = cards[0]
for value, suit in cards:
    if not(value == top_value or suit == top_suit):
        filtered.append((value, suit))

if len(filtered) == 0:
    print('empty deck')
else:
    for card in filtered:
        value, suit = card
        print(f'{value} of {suit}')


# RED FLAG: DON'T MODIFY THE LIST AS YOU ITERATE OVER IT
# SKETCHY THINGS WILL HAPPEN
# for i in range(n):
#     print(cards)
#     card = cards[i]
#     value, suit = card
#     if value == cards[0][0] or suit == cards[0][1]:
#         cards.pop(i)

# for card in cards:
#     value, suit = card
#     print(f'{value} of {suit}')
