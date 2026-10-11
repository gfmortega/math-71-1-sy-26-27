n = int(input())
a = [int(x) for x in input()]

q = int(input())
for _ in range(q):
    l, r, x = [int(x) for x in input().split()]
    l -= 1
    r -= 1

    ans = -1 # default value
    for i in range(l, r+1):
        if a[i] >= x:
            ans = i+1
            break
    
    print(ans)