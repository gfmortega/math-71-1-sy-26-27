sentence = input().split()

x = float(sentence[0])
y = float(sentence[-1][:-1])

if sentence[2] == 'less':
    is_correct = x < y
elif sentence[2] == 'greater':
    is_correct = x > y
else:
    raise RuntimeError('Invalid case')

if is_correct:
    print('Correct')
else:
    print('Incorrect')