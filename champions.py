from positions import positions
from roles import roles


def all_champions() -> set:
    result = set()
    for value in positions.values():
        for x in value:
            result.add(x)
    return result


def leave_only(source: set, champions: dict, *args) -> set:
    champions_sets = [set(champions[args[i]]) for i in range(len(args))]
    return source.intersection(set.intersection(*champions_sets))


counter_roles = {
    "tank": {"fighter", "marksman"},
    "marksman": {"slayer", "mage"},
    "mage": {"tank", "slayer"},
    "fighter": {"mage", "marksman"},
    "slayer": {"tank", "fighter"},
}


def counter_pick(names: str):
    opp_roles = [set(role for role, values in roles.items() if name in values) for name in names]
    key_roles = set.intersection(*opp_roles)
    counter_him_roles = [counter_roles[role] for role in key_roles]
    counter_him_roles = set.intersection(*counter_him_roles)
    champions = all_champions()
    for role in counter_him_roles:
        champions = leave_only(champions, roles, role)
    return champions

