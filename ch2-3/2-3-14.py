x = int(input())

F = [0, 1]
while not (F[-1] >= x):
    F.append(F[-1] + F[-2])

print(F[-1])