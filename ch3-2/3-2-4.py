# READ INPUT
# Each item looks like (price, list of tags)
items = []
n = int(input())
for _ in range(n):
    k, price = [int(x) for x in input().split()]
    tags = input().split()
    items.append((price, tags))

q = int(input())
for _ in range(q):
    query_tag = input()

    total = 0
    for item in items:
        price, tags = item
        if query_tag in tags:
            total += price

    print(total)