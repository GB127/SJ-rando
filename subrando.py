import random

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


