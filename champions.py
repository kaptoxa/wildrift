from typing import Iterable
from textwrap import fill

from positions import positions
from roles import roles

OUTPUT_WIDTH = 29


def wrapped_set(items: Iterable) -> str:
    return fill(' '.join(item.capitalize() for item in items), width=OUTPUT_WIDTH)


COUNTER_ROLES = {
    "tank": {"fighter", "marksman"},
    "marksman": {"slayer", "mage"},
    "mage": {"tank", "slayer"},
    "fighter": {"mage", "marksman"},
    "slayer": {"tank", "fighter"},
}


class Champions:
    def __init__(self):
        sets = [set(value) for value in positions.values()]
        self.result = set.union(*sets)

    def filter_roles(self, *args):
        sets = [set(roles[role]) for role in args]
        self.result &= set.intersection(*sets)

    def filter_positions(self, *args):
        sets = [set(positions[position]) for position in args]
        self.result &= set.intersection(*sets)

    def counter(self, names: str):
        opp_roles = [set(role for role, values in roles.items() if name in values) for name in names]
        key_roles = set.intersection(*opp_roles)
        counter_him_roles = [COUNTER_ROLES[role] for role in key_roles]
        counter_him_roles = set.intersection(*counter_him_roles)
        for role in counter_him_roles:
            self.filter_roles(role)

    def __str__(self):
        if self.result:
            return wrapped_set(sorted(self.result))
        else:
            return "There is no any champion for these parameters"