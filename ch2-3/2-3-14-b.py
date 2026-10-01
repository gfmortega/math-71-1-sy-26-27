'''
    We only need to output the last Fibonacci number, not ALL of them
    And computing each next one only requires the previous two
'''

x = int(input())

# These are the two most recent Fibonacci numbers,
#  initialized to F[0] = 0 and F[1] = 1
Fn_1 = 0
Fn = 1

while not (Fn >= x):
    # increment from n -> n+1 (and when you do, n-1 -> n)
    Fn_1, Fn = (Fn, (Fn_1 + Fn))

print(Fn)
