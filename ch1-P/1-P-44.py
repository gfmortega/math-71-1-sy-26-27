x, y = [int(x) for x in input().split()]
h, k = [int(x) for x in input().split()]
r = int(input())

print(
    (x - h)**2 + (y - k)**2 <= r**2
)
