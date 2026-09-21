Q = int(input())
nums = [int(input()) for _ in range(Q)]

parities = []
for x in nums:
    transformed = (
        'ODD'
        if x % 2 == 1
        else 'EVEN'
    )
    parities.append(transformed)

for ans in parities:
    print(ans)
