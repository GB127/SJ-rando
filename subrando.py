import random
from gameclass import planetitems


def planetitem_shuffler(planet,*groups):
    dicto = {}
    if len(groups) != 0:
        for _ in range(len(groups)):
            planetitems[planet].pop(planetitems[planet].index(0x11))  # On enlève un warp qui sera réintroduit dans le groupe
        random.shuffle(planetitems[planet])
        for i in groups:
            dicto.update({str(i) : planetitems[planet][-(i-1):] + [0x11]})
            for _ in range(i):
                planetitems[planet].pop()
        dicto.update({"main" : planetitems[planet]})
    else:
        random.shuffle(planetitems[planet])
        dicto.update(planetitems[planet])
    return dicto

def nescolors():
    liste = list(range(0x1, 0x0D))
    liste += list(range(0x11, 0x1D))
    liste += list(range(0x21, 0x2D))
    liste += list(range(0x31, 0x3D))
    return liste


def getnewcolor(indice, colors):
    if indice < 13 :
        return random.randint(-2,2) + random.randint(1,2) * 12  + indice  % len(colors)
    if indice >= 13:
        return random.randint(-2,2) + 12  + indice  % len(colors)


def getdistributionaccel():
    delta_acceleration = [12,12,11,10,8,6,3,2]
    reversaccel = list(reversed(delta_acceleration))
    linearized = [8,8,8,8,8,8,8,8]
    rando_delta_accel = random.choice([delta_acceleration,reversaccel,linearized])
    liste = []
    for i in range(len(rando_delta_accel)):
        liste.append(sum(rando_delta_accel[:i+1]))
    return liste

def getwarheadaccel():
    liste1 = [0, 20, 32]
    liste2 = [0, 16, 32]
    liste3 = [0, 12, 32]

    randoliste = random.choice([liste1, liste2, liste3])
    return randoliste


