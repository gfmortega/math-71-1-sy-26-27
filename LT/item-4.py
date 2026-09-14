n, i = [int(x) for x in input().split()]
populations = [int(x) for x in input().split()]
roads = [int(x) for x in input().split()]

capital = populations.index(max(populations))
# inclusive L and R
L = i-1
R = capital-1
if not (L <= R):
    L, R = R, L

print(sum(roads[L : R+1]))