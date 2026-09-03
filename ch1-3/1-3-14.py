n = int(input())
salts = [int(x) for x in input().split()]
L, R = [int(x) for x in input().split()]
# convert to 0-indexing
L -= 1
R -= 1

subrange = salts[L:R+1]
average = sum(subrange)/len(subrange)

print(f'{average:.2f}')