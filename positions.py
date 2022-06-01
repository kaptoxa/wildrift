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
