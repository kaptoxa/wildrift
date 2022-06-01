from argparse import ArgumentParser
from champions import positions, roles
from champions import print_champions_dict


def create_argument_parser() -> ArgumentParser:
    argument_parser = ArgumentParser()
    argument_parser.add_argument("-position", "-p")
    argument_parser.add_argument("-roles", "-r")
    argument_parser.add_argument("-locale", "-l", default="en")
    return argument_parser


if __name__ == "__main__":
    argument_parser = create_argument_parser()
    namespace = argument_parser.parse_args()

    if namespace.position:
        if namespace.position in positions:
            print_champions_dict(positions, namespace.position)
        elif namespace.position == "all":
            print_champions_dict(positions)

    if namespace.roles:
        if namespace.roles in roles:
            print_champions_dict(roles, namespace.roles)
        elif namespace.roles == "all":
            print_champions_dict(roles)
