s = input()
t = input()

def solve(s, t):
    g = t.count('G') - s.count('G')
    c = t.count('C') - s.count('C')
    a = t.count('A') - s.count('A')
    t_= t.count('T') - s.count('T')

    return (
        g >= 0 and g % 2 == 0 and
        c >= 0 and c % 2 == 0 and 
        a >= 0 and a % 2 == 0 and
        t_>= 0 and t_% 2 == 0
    )

print(
    'YES'
    if solve(s, t)
    else 'NO'
)
