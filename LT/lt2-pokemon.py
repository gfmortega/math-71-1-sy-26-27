n = int(input())
skills = [int(x) for x in input().split()]

pokemon = list(range(n))  # can recover the skill of pkmn i, as skill[i]
eliminated_at = [None for _ in range(n)]


round_no = 1
while len(pokemon) > 1:
    next_round = []
    # run one round of the single elim tournament
    for i in range(0, len(pokemon), 2):
        # i and i+1 will fight
        if skills[i] > skills[i+1]:
            winner = i
            loser = i+1
        else:
            winner = i+1
            loser = i

        next_round.append(winner)
        eliminated_at[loser] = round_no
    
    round_no += 1
    pokemon = next_round

eliminated_at[pokemon[0]] = 'CHAMP'

print(*eliminated_at)