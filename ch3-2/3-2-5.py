# READ INPUT
# Each item looks like (price, list of tags)
items = []
n = int(input())
for _ in range(n):
    k, price = [int(x) for x in input().split()]
    tags = input().split()
    items.append((price, tags))

def is_good(filter, tags):
    mode = filter[0]
    tag = filter[1:]

    if mode == '+':
        return tag in tags
    elif mode == '-':
        return tag not in tags
    else:
        raise RuntimeError(f'Unexpected mode: {mode}')

q = int(input())
for _ in range(q):
    v = int(input())
    filters = input().split()

    total = 0
    for item in items:
        price, tags = item
        if all(
            is_good(filter, tags)
            for filter in filters
        ):
            total += price

    print(total)