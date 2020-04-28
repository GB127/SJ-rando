from gameclass import ROM, infos
import random
infos = infos()

"""
with open("ROM.nes", "rb") as original:
    originaldata = original.read()
    game = ROM(originaldata)
"""
infos.listadresses("palettes")


def paletterandomizer():
    colors = list(range(0x0, 0x0E))
    colors += list(range(0x10, 0x1E))
    colors += list(range(0x20, 0x2E))
    colors += list(range(0x30, 0x3E))
    colors.remove(0xD)
    colors.remove(0x1D)

    # Rocket palette
    maincolor = random.choice(colors)
    secondary = random.choice(colors)
    window = random.choice(colors)

    print(maincolor, secondary,window)


paletterandomizer()
