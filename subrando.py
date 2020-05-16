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
