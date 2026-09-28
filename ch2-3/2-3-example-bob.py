n = int(input())
board = input().split()
# each individual square has an "is_visited" flag
visited = [False for _ in range(n)]

impossible = False
pos = 0
turn_count = 0
while board[pos] != 'END':
    if visited[pos]:
        impossible = True
        break
    visited[pos] = True

    space = board[pos]
    if space[-1] == 'R':
        pos += int(space[:-1])
    elif space[-1] == 'L':
        pos -= int(space[:-1])

    turn_count += 1

if impossible:
    print('impossible')
else:
    print(turn_count)