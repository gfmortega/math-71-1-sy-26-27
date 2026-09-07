def shift_in_place(L):
    L.insert(0, L[-1])
    L.pop()

def shifted(L):
    return [L[-1]] + L[:-1]

# L = [1, 2, 3, 4, 5]
# print(shifted(L))
# print(L)
