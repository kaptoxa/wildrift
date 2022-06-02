from typing import Iterable
from argparse import ArgumentParser
from textwrap import fill

from positions import positions
from roles import roles
from champions import leave_only, all_champions, counter_pick

OUTPUT_WIDTH = 30


def wrapped_set(items: Iterable) -> str:
    return fill(' '.join(item.capitalize() for item in items), width=OUTPUT_WIDTH)


def create_argument_parser() -> ArgumentParser:
    argument_parser = ArgumentParser()
    argument_parser.add_argument("names", nargs="+")
    argument_parser.add_argument(
        "-positions", "-p", nargs='+', choices=[
            "solo",
            "jungle",
            "mid",
            "duo",
            "support"
        ]
    )
    argument_parser.add_argument(
        "-roles", "-r", nargs="+", choices=[
            "tank",
            "mage",
            "marksman",
            "fighter",
            "slayer"]
    )
    argument_parser.add_argument("-locale", "-l", default="en")
    return argument_parser


if __name__ == "__main__":
    argument_parser = create_argument_parser()
    namespace = argument_parser.parse_args()

    if namespace.names:
        champions = counter_pick(namespace.names)
    else:
        champions = all_champions()

    if namespace.positions:
        for position in namespace.positions:
            champions = leave_only(champions, positions, position)

    if namespace.roles:
        for role in namespace.roles:
            champions = leave_only(champions, roles, role)

    if champions:
        print(wrapped_set(sorted(champions)))
    else:
        print("There is no any champion for these parameters")
