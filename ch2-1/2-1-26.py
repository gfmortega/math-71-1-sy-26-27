n = int(input())
a = [int(x) for x in input().split()]

ans = []
for i in range(1, n):
    # do something with a[i] - a[i-1]
    diff = a[i] - a[i-1]
    if diff > 0:
        ans.append(f'+{diff}')
    else:
        ans.append(f'{diff}')
print(*ans)