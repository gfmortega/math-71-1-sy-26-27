n = int(input())
problems = input().split()

k = int(input())
achievements = []
for _ in range(k):
    name = input()
    conditions = input().split()
    achievements.append((name, conditions))

m = int(input())
for _ in range(m):
    # process each user
    solved = input().split()
    
    earned = []
    for name, conditions in achievements:
        if set(conditions) <= set(solved):
            earned.append(name)

    # solved = input().split()

    # earned = []
    # for name, conditions in achievements:
    #     if all(
    #         condition in solved
    #         for condition in conditions
    #     ):
    #         earned.append(name)
    if len(earned) == 0:
        print(':(')
    else:
        print(*earned)