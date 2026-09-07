def other(castle):
    if castle == 'A':
        return 'B'
    elif castle == 'B':
        return 'A'
    else:
        raise RuntimeError(f'Unexpected castle: {castle}')
    # return 'B' if castle == 'A' else 'A'

def locate_ogre_by_pig(line):
    words = line.split()

    castle = words[-1][:-1]
    if len(words) == 5:       # the "is" case
        return castle
    elif len(words) == 6:     # the "is not" case
        return other(castle)
    else:
        raise RuntimeError(f'Unexpected sentence: {line}')

def locate_ogre(a, b, c):
    Asays = locate_ogre_by_pig(a)
    Bsays = locate_ogre_by_pig(b)
    Csays = locate_ogre_by_pig(c)

    # answer = Asays
    # if Asays == Bsays == Csays:
    #     answer = Asays
    # else:
    #     answer = 'INCONSISTENT'

    # return Asays if Asays == Bsays == Csays else 'INCONSISTENT'
    
    return (
        Asays
        if Asays == Bsays == Csays
        else 'INCONSISTENT'
    )