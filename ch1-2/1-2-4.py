a = float(input())
b = float(input())

both_tall = a >= 150.0 and b >= 150.0
different = (
    (a > 180.0 and b < 140.0) or
    (a < 140.0 and b > 180.0)
)

print(both_tall or different)