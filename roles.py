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
    ahri yasuo zed rengar pantheon ekko
    yi evelynn kaisa fiora vayne akali
    akshan fizz irelia katakina khazix leesin
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