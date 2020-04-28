from gameclass import ROM, infos
import random
infos = infos()

infos.listadresses("palettes")


def paletterandomizer(game):
    #Create the pool of colors
        #FIXME : I'm sure it can be improved. But for the time being it will be like that
    colors = list(range(0x0, 0x0E))
    colors += list(range(0x10, 0x1E))
    colors += list(range(0x20, 0x2E))
    colors += list(range(0x30, 0x3E))
    colors.remove(0xD)
    colors.remove(0x1D)

    # Rocket palette
        # It's split into 3 variables since I plan to do operations so the randomized palettes aren't too crazy.
    maincolor = random.choice(colors)
    secondary = random.choice(colors)
    window = random.choice(colors)
    print(hex(maincolor), hex(secondary),hex(window))
    game[0x75D7] = maincolor
    game[0x75E1] = maincolor
    game[0x75D8] = secondary
    game[0x75D6] = window


with open("ROM.nes", "rb") as original:
    originaldata = original.read()
    randogame = ROM(originaldata)
    paletterandomizer(randogame)
    with open("ROM2.nes", "wb") as newrom:
        newrom.write(randogame.data)