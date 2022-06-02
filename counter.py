from argparse import ArgumentParser
from champions import Champions


champions = Champions()


def create_argument_parser() -> ArgumentParser:
    argument_parser = ArgumentParser()
    argument_parser.add_argument("name", nargs="+", help="name of the champion")
    argument_parser.add_argument(
        "-positions", "-p", nargs='+', choices=[
            "solo",
            "jungle",
            "mid",
            "duo",
            "support"
        ],
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

    champions.counter(namespace.name)
    if namespace.positions:
        champions.filter_positions(*namespace.positions)
    if namespace.roles:
        champions.filter_roles(*namespace.roles)

    print(champions)
