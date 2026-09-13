x, y = [float(x) for x in input().split()]

'''
    There are many solutions to this problem, such as using trig to get angles, or
    To avoid floating point but stay in HS scope, I will use inequalities.
    (Though if you know vectors, you can choose to think of these as cross products)
'''
def N_or_S(x, y):
    if x - 2*y < 0 and x + 2*y > 0:
        return 'N'
    elif x + 2*y < 0 and x - 2*y > 0:
        return 'S'
    else:
        return ''
    
def E_or_W(x, y):
    if 2*x - y > 0 and 2*x + y > 0:
        return 'E'
    elif 2*x - y < 0 and 2*x + y < 0:
        return 'W'
    else:
        return ''
    
print(N_or_S(x, y) + E_or_W(x, y))