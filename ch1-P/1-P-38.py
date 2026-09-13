t = float(input())
a = float(input())
d = float(input())
v0 = float(input())
vf = float(input())

EPS = 1e-2
def close_enough(x, y):
    return abs(x - y) < EPS

print(
    'Consistent'
    if (
        close_enough(vf, v0 + a*t) and
        close_enough(d, 0.5*(v0 + vf)*t) and
        close_enough(d, vf*t - 0.5*a*t**2) and
        close_enough(d, v0*t + 0.5*a*t**2) and
        close_enough(vf**2, v0**2 + 2*a*d)
    )
    else 'Inconsistent'
)

'''
    Just directly encode the kinematic equations and following instructions
    (use close_enough instead of == because of floating point)
'''