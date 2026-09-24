n = int(input())
a = [int(x) for x in input().split()]

found_idx = None
for idx in reversed(range(n)):
    if a[idx] % 2 == 0:
        found_idx = idx
        break

if found_idx is None:
    print('no even numbers')
else:
    print(found_idx)