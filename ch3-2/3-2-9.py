n = int(input())
grid = [
    input()
    for _ in range(n)
]

print(''.join(
    grid[i][i]
    for i in range(n)
))