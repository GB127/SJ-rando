from gameclass import ROM, infos
import random
infos = infos()

infos.listadresses("palettes")


def paletterandomizer(game):
    #Create the pool of colors
        #FIXME : I'm sure it can be improved. But for the time being it will be like that
            # idea 1 : create a for _ ion range 4
            # idea 2 : create the entire palette 90 to EF or somethimg, then remove the colors with a loop
    colors = list(range(0x0, 0x0E))
    colors += list(range(0x10, 0x1E))
    colors += list(range(0x20, 0x2E))
    colors += list(range(0x30, 0x3E))
    colors.remove(0xD)
    colors.remove(0x1D)





    # HUD display
    game[0x75E2] = random.choice(colors)  # Score palette
    game[0x75E3] = random.choice(colors)  # Bars palette

    # Rocket palette
        # It's split into 3 variables since I plan to do operations so the randomized palettes aren't too crazy.
    maincolor = random.choice(colors)
    secondary = random.choice(colors)
    # game[0x75D6] = random.choice(colors)  # window color
    # game[0x75D7] = maincolor  # Main color
    # game[0x75D8] = secondary  # secondary color
    game[0x75E1] = game[0x75D7] # Icon color



with open("ROM.nes", "rb") as original:
    originaldata = original.read()
    randogame = ROM(originaldata)
    paletterandomizer(randogame)
    with open("ROM2.nes", "wb") as newrom:
        newrom.write(randogame.data)