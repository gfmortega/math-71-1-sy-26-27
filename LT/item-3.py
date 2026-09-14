def parse_sentence(line):
    words = line.split()

    if words[5] == 'today,':
        a = int(words[4][1:])
        b = int(words[7][1:])
        c = int(words[-2])
        return a, b, c

    elif words[5] == 'every':
        a = int(words[-2][1:])
        b = int(words[4][1:])
        c = int(words[8])
        return a, b, c
    
    else:
        raise RuntimeError(f'Unexpected case: {words[5]}')

a, b, c = parse_sentence(input())

# Alice
if a >= b*c:
    print('TODAY')
else:
    print('EVERY DAY')

# Bob
# a today or b everyday for at most 7 days
if c >= 7:
    bob_days = 7
else: # c < 7
    bob_days = c

if a >= b*min(7, c):
# if a >= b*bob_days:
    print('TODAY')
else:
    print('EVERY DAY')
