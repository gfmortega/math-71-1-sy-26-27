n = int(input())
a = [int(x) for x in input().split()]

d = a[1] - a[0]
is_arithmetic = True
for i in range(1, n):
    if not (a[i] - a[i-1] == d):
        is_arithmetic = False
        break

if is_arithmetic:
    print('YES')
    print(f'initial term: {a[0]}')
    print(f'common differnece: {d}')
else:
    print('NO')