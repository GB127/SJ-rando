from gameclass import ROM, infos
import random

infos = infos()

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



def engine_randomizer(game):
    """
        This function will randomize these elements:
            - Acceleration of the rocket
            - Speed max of the rocket
            - Gravity
    """
    # Randomize speedmaxs:
        # The original value is 3, which is slow IMO.
        # So the randomizer will randomize to something higher.
        # The goal is to have a worst case scenario of vanilla feature,
        # and a "best case scenario" where the speed is very high.
        # The middle will be what I consider to be a perfect value for casual play
    game[0x048D3] = random.randint(3,12)  # both speed
    game[0x3b8a3] = game[0x48D3]  # x speed
    game[0x3b8ac] = game[0x48D3]  # x speed
    game[0x3b909] = game[0x48D3]  # y speed
    game[0x3b912] = game[0x48D3]  # y speed

infos.listadresses("timer")
print(0xFF)

def manage_randomizer(game):
    """ 
    This function will randomize the following stuffs:
        - Scoring stuffs
        - Fuel related stuffs
        - Invicibility timer
    """
    # This is for the fuel consumption.
        # On press A
        # Default value is 2, which is abysmal IMO. So let's crank it a big notch :D
        # The possible range is 0 (yes yes, free fuel!) up to 255
    game[0x386B7] = random.randint(0,255)

    # This is the starting fuel.
        # Default value is E0 for 224 * 255 unit.
        # In other words, you start with 57 120 fuel!
        # this is a big number. So let's crank it down, shall we?
        # This is going to be hard to finetune. Help needed.
        # The goal is to have a minimum where you have to not use fuel while traveling
        # to save on fuel or to use fuel tanks.
        # Will have to think on how to finetune this.
    game[0x7202] = random.randint(1,255)

    # This is for the invicibility timer on wall collision.
        # Default value is 30 (28 in decimal).
        # This game run 30 FPS per seconds I think. So you have 1 second of invicibility.
        # Let's alter this a little bit.
        # 1 being no invicibility at all
        # 255 being the max value of a byte
    game[0x11011] = random.randint(1,255)

"""


with open("ROM.nes", "rb") as original:
    originaldata = original.read()
    randogame = ROM(originaldata)
    paletterandomizer(randogame)
    with open("ROM2.nes", "wb") as newrom:
        newrom.write(randogame.data)

"""