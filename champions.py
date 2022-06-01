from typing import Iterable
import textwrap
from positions import positions
from roles import roles


def print_wrapped_set(items: Iterable):
    print(textwrap.fill(' '.join(item.capitalize() for item in items), width=30))


def print_set_champions(champions: dict, key: str | None = None):
    if not key:
        for key, value in champions.items():
            print(f"{key.upper()} champions:")
            print_wrapped_set(sorted(value))
            print()
    else:
        print(f"{key.upper()} champions:")
        print_wrapped_set(sorted(champions[key]))
        print()


def position_statistic():
    for pos, champions in positions.items():
        print(f"position: {pos}")
        stats = []
        for role, variants in roles.items():
            result = set(champions).intersection(set(variants))
            stats.append((role, len(result)))

        for role, count in sorted(stats, key=lambda pair: -pair[1]):
            print(f"{count} {role} champions")
        print()


def position_intersections(role, *args):
    print(f"{role.upper()} champions that can play: {' or '.join(x.upper() for x in args)}")
    result = set(positions[args[0]])
    for i in range(1, len(args)):
        result &= set(positions[args[i]])
    if result:
        print(textwrap.fill(' '.join(champion.capitalize() for champion in result), width=30))
    else:
        print('None.')
    print()


# position_intersections('fighter', 'jungle', 'solo')
# position_intersections('tank', 'jungle', 'solo', 'support')