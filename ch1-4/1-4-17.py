from math import sin, radians

a = float(input())
b = float(input())
C = float(input())

area = 0.5*a*b*sin(radians(C))
print(f'{area:.2f}')
