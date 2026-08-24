P = float(input())
r = float(input())
n = int(input())
t = int(input())

A = P*(1 + r/n)**(n*t)

print(f'{A:.2f}')