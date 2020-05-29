from gameclass import ROM, infos
from subrando import nescolors, getnewcolor, getdistributionaccel, getwarheadaccel, planetitem_shuffler
import random

def palette_randomizer(game, seed):
    random.seed(seed)
    colors = nescolors()
    #Create the pool of colors

    # HUD display
    game[0x75E2] = random.choice(colors)  # Score palette
    game[0x753C] = game[0x75E2]  # Score palette too
    game[0x75E3] = random.choice(colors)  # Bars palette
    game[0x75ac] = random.choice(colors)  # Title screen dots
    # Rocket palette
    game[0x75D8] = random.choice(colors[0:27])  # Main color
    game[0x75D7] = colors[getnewcolor(colors.index(game[0x75D8]), colors)]  # secondary color
    game[0x75E1] = game[0x75D8] # Icon color is the same as the main color
    game[0x00753B] = game[0x75D8]
    # game[0x75D6] = random.choice(colors)  # window color

    game[0x0075ad] = random.choice(colors) # C'est le milieu
    game[0x0075aE] = random.choice(colors)  # C'est l'autre

def item_randomizer(game,seed):
    random.seed(seed)

    # Planet 1:
    p1 = planetitem_shuffler("1")
    game[0x11a4F] = p1["main"][0]  # minigame
    game[0x11a54] = p1["main"][1]  # this is the shield
    game[0x11a59] = p1["main"][2]  # Crystal of planet 1
    game[0x11a5E] = p1["main"][3]  # Fuel of planet 1
    game[0x11a63] = p1["main"][4]  # Warp for golden 

    # Planet 2:
    p2 = planetitem_shuffler("2",5)
    game[0x11E46] = p2["main"][0]
    game[0x11E4B] = p2["main"][1]
    game[0x11E50] = p2["main"][2]
    game[0x11E55] = p2["main"][3]
    game[0x11E5A] = p2["main"][4]
    game[0x11E5F] = p2["main"][5]
    game[0x11E64] = p2["main"][6]
    game[0x11E73] = p2["main"][7]
    game[0x11E7D] = p2["main"][8]
    game[0x11E82] = p2["main"][9]
    game[0x11E87] = p2["main"][10]
    game[0x11E91] = p2["main"][11]
    game[0x11E9B] = p2["main"][12]
    game[0x11EAA] = p2["main"][13]
    game[0x11EAF] = p2["main"][14]
    game[0x11EB4] = p2["main"][15]

    game[0x11E8C] = p2["5"][0]
    game[0x11E69] = p2["5"][1]
    game[0x11E6E] = p2["5"][2]
    game[0x11E78] = p2["5"][3]
    game[0x11E96] = p2["5"][4]


    # Planete 4:
    p4 = planetitem_shuffler("2")
    game[0x11a6D] = p4["main"][0]
    game[0x11a72] = p4["main"][1]
    game[0x11a77] = p4["main"][2]
    game[0x11a7c] = p4["main"][3]
    game[0x11a81] = p4["main"][4]
    game[0x11a86] = p4["main"][5]
    game[0x11a8B] = p4["main"][6]
    game[0x11a90] = p4["main"][7]
    game[0x11a95] = p4["main"][8]
    game[0x11a9A] = p4["main"][9]
    game[0x11a9F] = p4["main"][10]
    game[0x11aA4] = p4["main"][11]
    game[0x11aA9] = p4["main"][12]
    game[0x11aAE] = p4["main"][13]
    game[0x11aB3] = p4["main"][14]
    game[0x11aB8] = p4["main"][15]
    game[0x11aBD] = p4["main"][16]
    game[0x11aC2] = p4["main"][17]
    game[0x11aC7] = p4["main"][18]
    game[0x11aCC] = p4["main"][19]






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
    game[0x448f] = random.randint(3,8)  # I'll remove this if the testing case still works
    game[0x3a25] = game[0x448f]  # X speed  can't be lower than 5 or it will mess with the last level
    game[0x3a2E] = game[0x448f]  # X speed

    game[0x3a8f] = 10#random.randint(0,8)  # maxspeed Y up
    game[0x3a98] = game[0x3a8f]  # Fastfall maxspeed Y



def gravity_randomizer(game,seed, test):
    gravity = test# random.randint(0,255)  # FIXME
    game[0x01040D] = 169  # This is the opperation
    game[0x01040E] = gravity # This is the operand. Normally it's F8.
    game[0x0107B3] = 169
    game[0x0107B4] = gravity

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
    game[0x048D3] = random.randint(3,8)  # both speed
    game[0x3b8a3] = game[0x48D3]  # x speed
    game[0x3b8ac] = game[0x48D3]  # x speed
    game[0x3b909] = game[0x48D3]  # y speed
    game[0x3b912] = game[0x48D3]  # y speed


    # Randomize acceleration!
        # Either flip the acceleration table, linearize it or keep it.
        # Then randomize the highest, then keep the same ratio.
    randoaccel = getdistributionaccel()
    game[0x38866] = random.randint(randoaccel[-1], 255)   # This is the max accel.
        # Wrote it ike that in case I change something
    ratio = game[0x38866] / 64
    game[0x38867] = int(randoaccel[-2] * ratio)
    game[0x38868] = int(randoaccel[-3] * ratio)
    game[0x38869] = int(randoaccel[-4] * ratio)
    game[0x3886A] = int(randoaccel[-5] * ratio)
    game[0x3886B] = int(randoaccel[-6] * ratio)
    game[0x3886C] = int(randoaccel[-7] * ratio)
    game[0x3886D] = int(randoaccel[-8] * ratio)
    game[0x3886E] = 0 # I don't change this, but just to "Know that it's considered" I'm writting it down.


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



if __name__ == "__main__" :
    infos = infos()
    infos.listadresses("palette")