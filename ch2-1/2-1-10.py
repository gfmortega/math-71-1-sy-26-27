n = int(input())
h = [int(x) for x in input().split()]

# condition on what to modify -> 
#   all flowers of minimum height

# the modification ->
#   grew until their height was the same
#   as the maximum height of all the flowers.
mini = min(h)
maxi = max(h)
for i in range(n):
    if h[i] == mini:
        h[i] = maxi

print(*h)
