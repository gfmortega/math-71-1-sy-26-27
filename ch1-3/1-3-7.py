n = int(input())
rooms = input().split()
sentence = input().split()

i = int(sentence[3][:-2])
direction = sentence[-1][:-1]

if 1 <= i <= n:
    if direction == 'left':
        answer = rooms[i-1]
    elif direction == 'right':
        answer = rooms[-i]
    else:
        raise RuntimeError("Invalid case")
else:
    answer = -1

print(answer)