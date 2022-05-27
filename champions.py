from itertools import combinations
import textwrap

positions = {
    "support": """
mundo lulu lux senna nami
pantheon shen galio morgana alistar
annie seraphine brand braum teemo
thresh soraka amumu blitzcrank janna
karma leona malphite orianna rakan
sona yuumi""",
    "duo": """
jhin senna jinx ashe corki
tristana kaisa lucian caitlyn fortune
xayah akshan draven ezreal varus
vayne
""",
    "mid": """
twisted lulu ahri diana lux
yasuo zed galio morgana annie
ekko seraphine brand corki kennen
teemo lucian veigar akali akshan
aurelion fizz irelia jayce karma
katarina kayle orianna sona ziggs
""",
    "jungle" : """
mundo tryndamere gragas camille jax
rengar pantheon shen morgana ekko
yi olaf wukong evelynn amumu
graves jarvan khazix leesin nunu
rammus shyvana vi xinzhao
""",
    "solo" : """
mundo tryndamere gragas camille nasus
jax diana yasuo zed pantheon
shen ekko garen kennen olaf
teemo wukong lucian fiora akali
amumu darius fizz iralia jarvan
jayce kayle malphite renekton riven
sett shyvanna"""
}

for key, values in positions.items():
    positions[key] = values.split()

roles = {
    "fighter": """
    mundo tryndamere camille nasus jax diana
    yasuo rengar pantheon garen yi olaf
    wukong fiora kayle shyvana vi darius
    graves irelia jarvan jayce leesin renekton
    riven sett xinzhao
    """,
    "tank": """
    mundo gragas nasus shen galio alistar
    garen braum wukong thresh amumu rakan
    shyvana blitzcrank jarvan leona malphite
    nunu rammus sett singed xinzhao
    """,
    "mage": """
    jhin gragas twisted lulu ahri diana
    lux nami galio morgana annie ekko
    seraphine brand corki kennen teemo veigar
    fortune soraka yuumi aurelion ezreal fizz
    janna karma katarina nunu orianna singed
    sone varus ziggs
    """,
    "slayer": """
    ahri yasuo zed rengar pantheon ekko,
    yi evelynn kaisa fiora vayne akali,
    akshan fizz irelia katakina khazix leesin,
    riven
    """,
    "controller": """
    lulu lux senna nami shen margana
    alistar annie seraphine braum thresh soraka
    rakan yuumi blitzcrank janna karma leona
    orianna sona
    """,
    "marksman": """
    jhin twisted senna jinx ashe corki
    kennen teemo tristana kaisa lucian caitlyn
    fortune xayah vayne akshan draven ezreal
    graves jayce varus"""
}

for key, values in roles.items():
    roles[key] = values.split()


def position_roles():
    for pos, champions in positions.items():
        print(f"position: {pos}")
        stats = []
        for role, variants in roles.items():
            result = set(champions).intersection(set(variants))
            stats.append((role, len(result)))

        for role, count in sorted(stats, key=lambda pair: -pair[1]):
            if count > 2:
                print(f"{count} {role} champions")
        print()


def position_champions():
    for pos, champions in positions.items():
        print(f"position: {pos}")
        for role, variants in roles.items():
            result = set(champions).intersection(set(variants))
            print(f"{role}: ", end='')
            print(' '.join(x for x in result))
        print()


def roles_champions():
    for role, variants in roles.items():
        print(f"role: {role}")
        for pos, champions in positions.items():
            result = set(champions).intersection(set(variants))
            print(f"{pos}: ", end='')
            print(' '.join(x for x in result))
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


# print('----------statistic--------------')
# position_roles()
#
# print('----------position champions--------------')
# position_champions()
# print('----------roles champions--------------')
# roles_champions()

position_intersections('fighter', 'jungle', 'solo')
position_intersections('tank', 'jungle', 'solo', 'support')
position_intersections('mage', 'support', 'mid')
position_intersections('slayer', 'solo', 'mid')
position_intersections('marksman', 'duo', 'mid')

#
# position_roles_with_champions()
# print('----------positions intersections--------------')
# position_intersections()
# print('----------roles intersections--------------')
# roles_intersections()
