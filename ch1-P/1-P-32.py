def is_vowel(c):
    return (
        c == 'a' or
        c == 'i' or
        c == 'u' or
        c == 'e' or
        c == 'o'
    )

def is_consonant(c):
    return not is_vowel(c)

s = input()    
if len(s) >= 3 and is_consonant(s[-3]) and s[-2:] == 'ay':
    print(s[-3] + s[:-3])
else:
    print('UNTRANSLATABLE')

'''
    (Python doesn't have multi-line comments; this is a multi-line STRING
     that just doesn't do anything because it's not assigned to a variable
     But technically this is NOT A COMMENT)

    We note some necessary conditions for it to be translatable.
    Whether it starts with a vowel or a consonant, the result ALWAYS:
    - Has at least 3 letter
    - Has a consonant as its third-to-last letter ('w' if vowel, that consonant if consonant)
    - Ends in 'ay'

    On the other hand, if it satisfies these conditions, then it always IS translatable.
    The proof is constructive, as shown above (s[-3] is known to be a consonant in this case)
'''