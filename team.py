from itertools import product, combinations


roles = 'mage', 'tank', 'fighter', 'slayer', 'marksman'
positions = 'solo', 'jungle', 'mid', 'duo', 'support'

units = product(positions, roles)
variations = combinations(units, len(positions))


def unique_positions_and_roles(s):
    return all(len(set(x[i] for x in s)) == len(positions) for i in range(2))


def constraint(s):
    for x in s:
        position, role = x
        if role == "slayer" and position in ["support", "duo"]:
            return False
        if role == "tank" and position in ["mid", "duo"]:
            return False
        if role == "fighter" and position in ['mid', 'support', "duo"]:
            return False
        if role == "mage" and position in ["jungle", "solo"]:
            return False
        if role == "marksman" and position in ["solo", "jungle", "support"]:
            return False

    return True


strategies = filter(unique_positions_and_roles, variations)

COLUMN = 10
print(''.join(f"{p:<{COLUMN}}" for p in positions))
print()
for s in filter(constraint, strategies):
    print(''.join(f"{role:<{COLUMN}}" for pos, role in s))
