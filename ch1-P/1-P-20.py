n = int(input())

if n % 2 == 0:
    if n < 8:
        print('NO')
    else:
        print('YES')
        print(4, n-4)
else:
    if n < 13:
        print('NO')
    else:
        print('YES')
        print(9, n-9)
