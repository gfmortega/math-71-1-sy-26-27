n = int(input())
h = [int(x) for x in input().split()]

Q = int(input())
for _ in range(Q):
    # do something Q times
    # what am I doing Q times?
    # solving a 1.3 problem
    L, R = [int(x) for x in input().split()]
    # convert from 1-index in statement, to 0-index for code
    L -= 1
    R -= 1
    '''
        0 1 (length is 2)
        ^ ^ 

        0 1 2 3 (length is 4)
          ^ ^

        0 1 2 3 4 5 (length is 6)
            ^ ^
    '''
    subrange = sorted(h[L : R+1])
    m = len(subrange)
    if m % 2 == 1:
        median = subrange[m // 2]
    else:
        median = (subrange[m//2 -1] + subrange[m//2])/2

    print(f'{median:.2f}')