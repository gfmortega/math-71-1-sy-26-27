_TURN, _ON, x = input().split()
_TURN, _ON, y = input().split()
input()
_TURN, _OFF, z = input().split()
input()
_LIGHT, r, _IS, _ON = input().split()
_LIGHT, s, _IS, temp = input().split()

ans = [None, None, None]

if z == x:
    still_on = y
    turned_off = x
elif z == y:
    still_on = x
    turned_off = y
else:
    raise RuntimeError(f'Impossible case: {x=} {y=} {z=}')

if x != 'A' and y != 'A':
    never_on = 'A'
elif x != 'B' and y != 'B':
    never_on = 'B'
elif x != 'C' and y != 'C':
    never_on = 'C'
else:
    raise RuntimeError(f'Impossible case: {x=} {y=}')

if r != '1' and s != '1':
    last_light = '1'
elif r != '2' and s != '2':
    last_light = '2'
elif r != '3' and s != '3':
    last_light = '3'
else:
    raise RuntimeError(f'Impossible case: {r=} {s=}')

'''
    Actual solution starts here.
    I started writing this first, then puzzled out which variables
     were missing that I needed.
    Then, I filled in the logic (above) for how to compute them.
'''

ans[int(r) - 1] = still_on

if temp == 'HOT':
    ans[int(s) - 1] = turned_off
    ans[int(last_light) - 1] = never_on

elif temp == 'COOL':
    ans[int(last_light) - 1] = turned_off
    ans[int(s) - 1] = never_on

else:
    raise RuntimeError(f'Impossible case: {temp=}')

print(*ans)