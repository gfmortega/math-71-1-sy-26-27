s = input()
t = input()

def solve(s, t):
    g = t.count('G') - s.count('G')
    c = t.count('C') - s.count('C')
    a = t.count('A') - s.count('A')
    u = t.count('U') - s.count('U')

    s = g + c + a + u
    if s % 3 != 0:
        return False
    
    w = s//3 - g
    x = s//3 - c
    y = s//3 - a
    z = s//3 - u
    return w >= 0 and x >= 0 and y >= 0 and z >= 0

print(
    'YES'
    if solve(s, t)
    else 'NO'
)

'''
    First, convince yourself that you can get any permutation by just swapping adjacent elements.
     A proof outline would be as follows:
    - You can do "move this element to any other position" by repeatedly using the swap operation
      (Picture that desired element "inching" into place)
    - If you accept that you can move any element to any other position, then you can attain any
      permutation you like by moving the first element to the right position, then the next one,
      then the next one... and so on (like how you would sort a hand of cards while playing poker)

    Therefore, it is necessary and sufficient for us to have the CORRECT number of GCAU by
     using the "insert a codon" operation to add the right amount of each GCAU.
    You can set this up as a linear system of equations (where each variable is how many times to
     insert each codon) which always has a unique solution (and is not too hard to solve).
    If a solution exists, it must be this, so:
     - If any of them is a non-negative integer, then it isn't valid, and no
        other possible valid solutions could exist (so, impossible)
     - If all of them are non-negative integers, then it IS a valid solution!
'''