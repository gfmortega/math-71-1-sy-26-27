n = int(input())
salts = [int(x) for x in input().split()]
L, R = [int(x) for x in input().split()]
# convert to 0-indexing
L -= 1
R -= 1

# keep ONLY everything before L, and after R
subrange = salts[:L] + salts[R+1:]

subrange.sort()
k = len(subrange)
if k % 2 == 1:
    median = subrange[k // 2]
else:
    median = (subrange[k//2 - 1] + subrange[k//2]) / 2.0

print(f'{median:.2f}')