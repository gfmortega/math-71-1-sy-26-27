def read_input():
    x = input()
    if x != '?':
        return float(x)
    return x

t = read_input()
a = read_input()
d = read_input()
v0 = read_input()
vf = read_input()

if a == '?' and d == '?':
    a = (vf - v0) / t
    d = (1/2) * (v0 + vf) * t
    print(f'{a:.2f}')
    print(f'{d:.2f}')

elif a == '?' and v0 == '?':
    a = (d - vf*t) / (-(1/2)*t**2)
    v0 = 2*d / t - vf
    print(f'{a:.2f}')
    print(f'{v0:.2f}')

elif a == '?' and vf == '?':
    a = (d - v0*t) / ((1/2)*t**2)
    vf = 2*d / t - v0
    print(f'{a:.2f}')
    print(f'{vf:.2f}')

elif d == '?' and v0 == '?':
    d = vf*t - (1/2)*a*t**2
    v0 = vf - a*t
    print(f'{d:.2f}')
    print(f'{v0:.2f}')

elif d == '?' and vf == '?':
    d = v0*t + (1/2)*a*t**2
    vf = v0 + a*t
    print(f'{d:.2f}')
    print(f'{vf:.2f}')

elif v0 == '?' and vf == '?':
    v0 = (d - (1/2)*a*t**2) / t
    vf = (d + (1/2)*a*t**2) / t
    print(f'{v0:.2f}')
    print(f'{vf:.2f}')
