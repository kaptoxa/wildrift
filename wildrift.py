from typing import Iterable
from argparse import ArgumentParser
from textwrap import fill

from positions import positions
from roles import roles

from champions import leave_only, all_champions

OUTPUT_WIDTH = 30


def wrapped_set(items: Iterable) -> str:
    return fill(' '.join(item.capitalize() for item in items), width=OUTPUT_WIDTH)


def create_argument_parser() -> ArgumentParser:
    argument_parser = ArgumentParser()
    argument_parser.add_argument("-positions", "-p", nargs='+')
    argument_parser.add_argument("-roles", "-r", nargs="+")
    argument_parser.add_argument("-locale", "-l", default="en")
    return argument_parser


if __name__ == "__main__":
    argument_parser = create_argument_parser()
    namespace = argument_parser.parse_args()

    champions = all_champions()
    if namespace.positions:
        for position in namespace.positions:
            champions = leave_only(champions, positions, position)

    if namespace.roles:
        for role in namespace.roles:
            champions = leave_only(champions, roles, role)

    print(wrapped_set(sorted(champions)))
