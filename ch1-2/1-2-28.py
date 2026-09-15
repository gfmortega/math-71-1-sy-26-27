time = input()

h = int(time[:2])
m = int(time[-2:])

m += 30
if m >= 60:
    m -= 60
    h += 1

if h >= 24:
    h -= 24

# there are more elegant and idiomatic ways to do this, using the standard library
#  (see f-string formatting)
# I am showing that it can be done w/ elementary methods easily
hh = str(h)
if len(hh) == 1:
    hh = '0' + hh

mm = str(m)
if len(mm) == 1:
    mm = '0' + mm

print(f'{hh}:{mm}')