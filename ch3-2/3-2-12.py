n = int(input())
grid = [
    [int(x) for x in input().split()]
    for _ in range(n)
]

print(
    'YES'
    if all(
        grid[i][j] == grid[j][i]
        for i in range(n)
        for j in range(n)
    )
    else 'NO'
)