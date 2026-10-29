n = 8
grid = [
    list(input())
    for _ in range(n)
]

steps = [
    (-2, -1),
    (-2, +1),
    (-1, -2),
    (-1, +2),
    (+1, -2),
    (+1, +2),
    (+2, -1),
    (+2, +1),
]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'N':
            for di, dj in steps:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    grid[ni][nj] = '*'

for row in grid:
    print(''.join(row))