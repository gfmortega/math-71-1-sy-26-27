name = input()
color = input()
age = int(input())
height = int(input())

counter = 0
if len(name) <= 5:
    counter += 1
if color[0] == 'B' or color[0] == 'b':
    counter += 1
if 20 <= age <= 25:
    counter += 1
if height >= 150:
    counter += 1

print(counter)