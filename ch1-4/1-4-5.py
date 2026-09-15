def parse_implication(stmt):
    words = stmt.split()
    if words[0] == 'A':
        return words[1], words[-1][:-1]
    elif words[0] == 'If':
        return words[4], words[-1][:-1]
    elif words[0] == 'One':
        return words[-1][:-1], words[3]
    else:
        raise RuntimeError(f'Unexpected case: {words[0]}')
    
# Checks SPECIFICALLY if it has the form: (a -> b) and (b -> c) implies (a -> c); (in that order)
def verify(x1, y1, x2, y2, x3, y3):
    return (
        x1 == x3 and
        y1 == x2 and
        y2 == y3
    )

def is_sound(stmt1, stmt2, stmt3):
    x1, y1 = parse_implication(stmt1)
    x2, y2 = parse_implication(stmt2)
    x3, y3 = parse_implication(stmt3)
    return (
        verify(x1, y1, x2, y2, x3, y3) or
        verify(x2, y2, x1, y1, x3, y3) or # the other way around
        (x1, y1) == (x3, y3)           or # conclusion is exactly premise1
        (x2, y2) == (x3, y3)           or # conclusion is exactly premise2
        x3 == y3                          # conclusion is trivially true
    )