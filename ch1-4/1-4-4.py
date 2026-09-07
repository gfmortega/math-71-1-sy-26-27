def parse_runner(line):
    speed, _ms, direc = line.split()
    if direc == 'east':
        return +speed
    elif direc == 'west':
        return -speed
    else:
        raise RuntimeError(f'Unexpected direction: {dir}')

# SIGNED velocities!!!
va = parse_runner(input())
vb = parse_runner(input())
d = int(input())

shrink_rate = va - vb # pen and paper
if shrink_rate <= 0:
    print('RUNAWAY')
else:
    answer = d/shrink_rate
    print(f'{answer:.2f}')

# if aDir == 'east' and bDir == 'west':
#     answer = d/(a + b)
# elif aDir == 'east' and bDir == 'east':
#     answer = d/(a - b)  # !
# elif aDir == 'west' and bDir == 'west':
#     answer = d/(-a + b) # !
# elif aDir == 'west' and bDir == 'east':
#     answer = 'RUNAWAY'
# else:
#     raise RuntimeError(f'Unexpected case: {aDir} {bDir}')