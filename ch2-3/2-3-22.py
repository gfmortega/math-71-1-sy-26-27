def faro_shuffle(deck):
    n = len(deck)
    top_half = deck[:n//2]
    bot_half = deck[n//2:]

    shuffled = []
    for i in range(n//2):
        shuffled.append(top_half[i])
        shuffled.append(bot_half[i])

    return shuffled

n = int(input())
deck = list(range(n))
original_order = deck.copy()

ctr = 1
deck = faro_shuffle(deck)
while not (deck == original_order):
    deck = faro_shuffle(deck)
    ctr += 1

print(ctr)