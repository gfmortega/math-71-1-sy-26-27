s = int(input())
e = int(input())
t = int(input())
d = int(input())

dist = abs(s - e)
print(
    "Yes"
    if (
        dist % d == 0 and
        dist // d <= t and
        (t - dist//d) % 2 == 0
    )
    else "No"
)