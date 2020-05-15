from gameclass import ROM, infos
import random

def paletterandomizer(game):
    #Create the pool of colors
    colors = list(range(0x1, 0x0D))
    colors += list(range(0x11, 0x1D))
    colors += list(range(0x21, 0x2D))
    colors += list(range(0x31, 0x3D))

    # HUD display
    game[0x75E2] = random.choice(colors)  # Score palette
    game[0x75E3] = random.choice(colors)  # Bars palette

    # Rocket palette
    game[0x75D8] = random.choice(colors[0:31])  # Main color
    game[0x75D7] = colors[(random.randint(-2,2) + random.randint(0,3) * 12 + colors.index(game[0x75D8])) % len(colors)]  # secondary color
    game[0x75E1] = game[0x75D7] # Icon color is the same as the main color
    # game[0x75D6] = random.choice(colors)  # window color


def engine_randomizer(game):
    """
        This function will randomize these elements:
            - Acceleration of the rocket
            - Speed max of the rocket
            - Gravity
    """
    print("Speed rando!")
    # Randomize speedmaxs:
        # The original value is 3, which is slow IMO.
        # So the randomizer will randomize to something higher.
        # The goal is to have a worst case scenario of vanilla feature,
        # and a "best case scenario" where the speed is very high.
    game[0x048D3] = random.randint(3,12)  # both speed
    game[0x3b8a3] = game[0x48D3]  # x speed
    game[0x3b8ac] = game[0x48D3]  # x speed
    game[0x3b909] = game[0x48D3]  # y speed
    game[0x3b912] = game[0x48D3]  # y speed
    print("Accelrando!")
    # Randomize acceleration!
        # The acceleration depends on the rocket direction and each
        # rocket's acceleration are stored independently.
        # So I'm going to alter all of them.
        # Approach:
            # First, Either flip the acceleration table, linearize it or keep it.
    delta_acceleration = [12,12,11,10,8,6,3,2]
    reversaccel = list(reversed(delta_acceleration))
    linearized = [8,8,8,8,8,8,8,8]
    rando_delta_accel = random.choice([delta_acceleration,reversaccel,linearized])
    randoaccel = []
    for i in range(len(rando_delta_accel)):
        randoaccel.append(sum(rando_delta_accel[:i+1]))
    game[0x38866] = random.randint(randoaccel[-1], 255)   # This is the max accel. Wrote it ike that in case I change something
    ratio = game[0x38866] / 64
    game[0x38867] = int(randoaccel[-2] * ratio)
    game[0x38868] = int(randoaccel[-3] * ratio)
    game[0x38869] = int(randoaccel[-4] * ratio)
    game[0x3886A] = int(randoaccel[-5] * ratio)
    game[0x3886B] = int(randoaccel[-6] * ratio)
    game[0x3886C] = int(randoaccel[-7] * ratio)
    game[0x3886D] = int(randoaccel[-8] * ratio)
    game[0x3886E] = 0 # I don't change this, but just to "Know that it's considered" I'm writting it down.


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
        # The possible range is 0 (yes yes, free fuel!) up to 254
        # The double thruster is always higher by at least one.
    game[0x386B7] = random.randint(0,254)  # Normal
    game[0x386AF] = random.randint(game[0x386B7] +1, 255)  # Thruster : I'll have to think on this.

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

if __name__ == "__main__" :
    infos = infos()
    infos.listadresses("acceleration")