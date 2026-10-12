r, c = [int(x) for x in input().split()]
grid = [
    [int(x) for x in input().split()]
    for _ in range(r)
]

totals = []
# For each column labeled j=0 to c-1
for j in range(c):
    # we FIXED j, but let i vary
    column = []
    for i in range(r):
        column.append(grid[i][j])

    totals.append(sum(column))

print(*totals)