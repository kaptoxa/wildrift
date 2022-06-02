from positions import positions
from roles import roles


def show_position_statistic():
    for pos, champions in positions.items():
        print(f"position: {pos}")
        stats = []
        for role, variants in roles.items():
            result = set(champions).intersection(set(variants))
            stats.append((role, len(result)))

        for role, count in sorted(stats, key=lambda pair: -pair[1]):
            print(f"{count} {role} champions")
        print()
