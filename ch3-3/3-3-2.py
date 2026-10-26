sentence = input().split()

n = int(input())
bad_words = set([input() for _ in range(n)])

for i, word in enumerate(sentence):
    if word in bad_words:
        sentence[i] = '*'*len(word)

print(' '.join(sentence))