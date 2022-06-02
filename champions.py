from positions import positions


def all_champions() -> set:
    result = set()
    for value in positions.values():
        for x in value:
            result.add(x)
    return result


def leave_only(source: set, champions: dict, *args) -> set:
    result = set(champions[args[0]])
    for i in range(1, len(args)):
        result &= set(champions[args[i]])
    return source.intersection(result)