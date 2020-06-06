from gameclass import ROM, infos
from subrando import nescolors, getnewcolor, getdistributionaccel, getwarheadaccel, planetitem_shuffler
import random



def astro_randomizer(game,seed):
    """
        This function will randomize these elements:
        - X Speed max of the astronaut
        - Y speed max of the FAST falling
        - X/Y Acceleration of the astornaut
    """
    random.seed(seed)

    # Randomize Astronaut's speedmaxs:
        # Like the rocket, the original value is 3.
        # One thing to note : down y speed is the same than the rocket)
        # But X max speed is not.
        # And the fast fall is distinct too.
        # So you could have a lower free fall max speed 
        # with this randomizer. But never higher.
    game[0x3a25] = random.randint(3,10)  # X speed
    game[0x3a2E] = game[0x3a25]  # X speed


    # Y up max speed
    game[0x3a8f] = random.randint(3,8)  # up maxspeed Y up
    game[0x3a98] = game[0x3a8f]
        #10 and 9 is too fast

    # X acceleration!
        # I have determined that the difference between these two must be at least 12
        # to offer an enjoyable experience.
    game[0x4497] = random.randint(0,255 -12)
    game[0x44D9] = random.randint(game[0x4497 + 12],255)


    # This is the Y acceleration for going up!
    game[0x00454A] = random.randint(22, 0xFF)  # Default : 20  # Decceleration from going down to up
    game[0x004559] = game[0x454A]  # default : 30  # Acceleration from down to up



def fuel_randomizer(game, seed):
    """ 
        This function will randomize the following stuffs:
            - Fuel related stuffs
            - Invicibility timer
    """
    random.seed(seed)

    # This is for the fuel consumption.
        # On press A
        # Default value is 2, which is abysmal IMO. So let's crank it a big notch :D
        # The possible range is 0 (free fuel!) up to 254
        # The double thruster is always higher by at least one.
    game[0x386B7] = random.randint(0,254)  # Normal
    game[0x386AF] = random.randint(game[0x386B7], 255)  # Thruster

    # This is the starting fuel.
        # Default value is E0 for 224 * 255 unit.
        # In other words, you start with 57 120 fuel!
        # this is a big number. So let's crank it down, shall we?
        # The goal is to have a minimum where you have to not use fuel
        # and use momentum to travel to save on fuel or to find and use fuel tanks.
    game[0x7202] = random.randint(1,255)  # Home
    game[0x8589] = random.randint(game[0x7202], 255)  # Fuel tanks
        # So it will always either give you more health
        # or give the same max health



    # This is for the invicibility timer on wall collision.
        # Default value is 30 (28 in decimal).
        # This game run 30 FPS per seconds I think. So you have 1 second of invicibility.
        # Let's alter this a little bit.
        # 1 being no invicibility at all
        # 255 being the max value of a byte
    game[0x11011] = random.randint(1,255)


def gravity_randomizer(game,seed, test):
    gravity = test# random.randint(0,255)  # FIXME
    game[0x01040D] = 169  # This is the opperation
    game[0x01040E] = gravity # This is the operand. Normally it's F8.
    game[0x0107B3] = 169
    game[0x0107B4] = gravity


def item_randomizer(game,seed):
    random.seed(seed)
    pass


def palette_randomizer(game, seed):
    random.seed(seed)
    colors = nescolors()
    #Create the pool of colors

    # HUD display
    game[0x75E2] = random.choice(colors)  # Score palette
    game[0x753C] = game[0x75E2]  # Score palette too
    game[0x75E3] = random.choice(colors)  # Bars palette
    # Rocket palette
    game[0x75D8] = random.choice(colors[0:27])  # Main color
    game[0x75D7] = colors[getnewcolor(colors.index(game[0x75D8]), colors)]  # secondary color
    game[0x75E1] = game[0x75D8] # Icon color is the same as the main color
    game[0x00753B] = game[0x75D8]
    # game[0x75D6] = random.choice(colors)  # window color

    game[0x75ac] = random.choice(colors)  # Title screen dots + jetpack fire
    #game[0x0075ad] = random.choice(colors) # C'est le milieu
    #game[0x0075aE] = random.choice(colors)  # C'est l'autre


def rocket_randomizer(game, seed):
    """
        This function will randomize these elements:
            - X/Y Acceleration of the rocket
            - Speed max of the rocket
    """
    random.seed(seed)

    # Randomize Rocket speedmaxs:
        # The original value is 3, which is slow IMO.
        # So the randomizer will randomize to something higher.
        # The goal is to have a worst case scenario of vanilla feature,
        # and a "best case scenario" where the speed is very high.

        # From my testing, 8 seemed to be a nice max speed. Can see stuffs coming.
        # Can manage to a certain extent with the least powerful rocket. It's hard, but
        # Doable.

        # NOTE : This randomize the max speed of the warhead things too!
    game[0x3b8a3] = 3#random.randint(3,8)  # x speed
    game[0x3b8ac] = game[0x3B8a3]  # x speed
    game[0x3b909] = game[0x3B8a3]  # y speed
    game[0x3b912] = game[0x3B8a3]  # y speed



    # Randomize acceleration!
        # Either flip the acceleration table, linearize it or keep it.
        # Then randomize the highest, then keep the same ratio.
    randoaccel = getdistributionaccel()
    game[0x38866] = random.randint(int(22 * game[0x3b8a3] - 46), 255)   # This is the max accel.
        # MIN accels:
            # 3 = 20
            # 4 = 42
            # 5 = 64
            # 6 = 86
            # 7 = 108
            # 8 = 130
    # Vanilla is 64
    ratio = game[0x38866] / 64
    game[0x38867] = int(randoaccel[-2] * ratio)
    game[0x38868] = int(randoaccel[-3] * ratio)
    game[0x38869] = int(randoaccel[-4] * ratio)
    game[0x3886A] = int(randoaccel[-5] * ratio)
    game[0x3886B] = int(randoaccel[-6] * ratio)
    game[0x3886C] = int(randoaccel[-7] * ratio)
    game[0x3886D] = int(randoaccel[-8] * ratio)
    game[0x3886E] = 0 # I don't change this, but just to "Know that it's considered" I'm writting it down.


def weapon_randomizer(game, seed):
    random.seed(seed)
    # Smart bombs:
        # There isn't much to be done with them. 
        # They instantly remove enemies on screen.
        # Could be potentially broken if really cheap Wusage 
    game[0x4EBC] = random.randint(1,255)

    # Anti Gravity:
        # There isn't much to be done with them. 
        # They simply remove gravity, 
        # at the expense of Wusage per frame
    game[0x3ED7] = random.randint(1,255)

    # Time Bomb
    game[0x4EBE] = random.randint(1,255)  # Time bomb


    # Star Bullet
    game[0x4EC1] = random.randint(1,255)  # Star bullet

    # Warhead / Homing missile:
        # They are the same thing, but the warhead don't leave after one hit
        # The prices are split though.
    game[0x4EBA] = random.randint(1,255)  # Homing Miss
    game[0x4EBF] = random.randint(1,255)  # Multi Warhead
    game[0x004dc1] = random.randint(1,255)  # Timer

    # Randomize the acceleration (So their behaviour aren't always the same :o) )
    distri = getwarheadaccel()
    game[0x03c3c2] = 0
    game[0x03c3c4] = random.randint(1, 255)  #20
    game[0x03c3c3] = int(distri[-2] * (game[0x03c3c4] / distri[-1])) # 14

    game[0x03c3c5] = game[0x03c3c3] # 14
    game[0x03c3c6] = game[0x03c3c2]  # 0
    game[0x03c3c7] = game[0x03c3c3]  # 14
    game[0x03c3c8] = game[0x03c3c4]  # 20
    game[0x03c3c9] = game[0x03c3c3]  # 14
