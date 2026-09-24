_n, phi = input().split()
n = int(_n)
words = input().split()

count = 0
for word in words:
    if word[0] == phi:
        count += 1

print(count)