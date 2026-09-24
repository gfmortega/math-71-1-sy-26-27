n = int(input())
temps = [int(x) for x in input().split()]
L, R = [int(x) for x in input().split()]
# convert from 1-indexed to 0-indexed
L -= 1
R -= 1

found_idx = None
for idx in range(L, R+1):  # <-- not the whole range, just the part the problem wants
    if temps[idx] > 50:
        found_idx = idx
        break

if found_idx is None:
    print('no reaction')
else:
    # convert back to 1-indexing
    print(found_idx+1)