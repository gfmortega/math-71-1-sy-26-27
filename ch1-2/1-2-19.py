n = int(input())

if n >= 92:
    letter = 'A'
# hidden: and n < 92
elif n >= 87:
    letter = 'B+'
elif n >= 83:
    letter = 'B'
elif n >= 78:
    letter = 'C+'
elif n >= 70:
    letter = 'C'
elif n >= 60:
    letter = 'D'
else:
    letter = 'F'

print(letter)