Q = int(input())
nums = [int(input()) for _ in range(Q)]

# for each in nums... call each thing "x"
for x in nums:
    # do something with x
    # what something? ODD/EVEN
    if x % 2 == 1:
        print('ODD')
    else:
        print('EVEN')
