raw_s = input()
s = list(raw_s)

first_period = None
for idx in range(len(s)):
    if s[idx] == '.':
        first_period = idx
        break
if first_period is None:
    first_period = len(s)

for i in range(first_period):
    s[i] = '*'

print(''.join(s))