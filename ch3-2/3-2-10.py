n = int(input())
grid = [
    [int(x) for x in input().split()]
    for _ in range(n)
]
mode = input()

# fill it with dummies for now
transformed_grid = [
    [None for j in range(n)]
    for i in range(n)
]
for i in range(n):
    for j in range(n):
        if mode == 'horizontal':
            # (i, j) in the original grid should
            # move to (i, n-1-j) in the new grid
            transformed_grid[i][n-1-j] = grid[i][j]
        elif mode == 'vertical':
            transformed_grid[n-1-i][j] = grid[i][j]

for row in grid:
    print(*row)