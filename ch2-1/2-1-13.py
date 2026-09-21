n = int(input())
h = [int(x) for x in input().split()]

locally_tall = []
for i in range(n):
    good = True # by default
    # let's look for counterexamples
    # IF I have a left neighbor, and am not taller than it,
    #  I am not good
    if 0 <= i-1 and not (h[i-1] < h[i]):
        good = False
    # IF I have a right neighbor, and am not taller than it,
    #  I am not good
    if i+1 < n and not (h[i] > h[i+1]):
        good = False

    if good:
        locally_tall.append(i+1) # 0 indexed -> 1 indexed

if len(locally_tall) == 0:
    print('none')
else:
    print(*locally_tall)