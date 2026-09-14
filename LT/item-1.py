n = int(input())
rooms = input().split()
start = ... # parse
steps, direction = ... # parse

# change to 0-indexing
start -= 1

if direction == 'clockwise':
    final_destination = (start + steps) % n
elif direction == 'counterclockwise':
    final_destination = (start - steps) % n
else:
    raise RuntimeError(f'Unexpected case: {direction}')

print(rooms[final_destination])