from subrando import nescolors, getnewcolor, getdistributionaccel, getwarheadaccel
import random
from items import *
    # Thank to this items module, items have their correct value 
    # (fuel = 0xA for example) and I have 
    # 2 giant dicto with all items offsets and their 
    # value seperated by planets

class ROM:
    def __init__(self,data):
        """
        This constructor convert the game (that is only in bytes)
        into a byte array that is a mutable form.

        data should be in bytes
        """
        self.data = bytearray(data)
    def __getitem__(self,offset):
        return self.data[offset]
    def __setitem__(self,offset, value):
        self.data[offset] = value
        
    def setmulti(self,offset1,offset2,value):
        for i in range(offset1, offset2+1):
            self.data[i] = value
class Rando(ROM):
    def __init__(self,data):
        self.seed = None
        self.flags = ""
        self.mode = "normal"
        super().__init__(data)
        self.disable_max4()
        self.lastlevel_rocks_lessdamage()

########################Randomizer##################################
    def astro_randomizer(self):
        """
            This function will randomize these elements:
            - X Speed max of the astronaut
            - Y speed max of the FAST falling
            - X/Y Acceleration of the astornaut
        """
        random.seed(self.seed)
        self.flags += "a"

        # Randomize Astronaut's speedmaxs:
            # Like the rocket, the original value is 3.
            # One thing to note : down y speed is the same than the rocket)
            # But X max speed is not.
            # And the fast fall is distinct too.
            # So you could have a lower free fall max speed 
            # with this randomizer. But never higher.
        self[0x3a25] = random.randint(3,10)  # X speed
        self[0x3a2E] = self[0x3a25]  # X speed


        # Y up max speed
        self[0x3a8f] = random.randint(3,8)  # up maxspeed Y up
        self[0x3a98] = self[0x3a8f]
            #10 and 9 is too fast

        # X acceleration!
            # I have determined that the difference between these two must be at least 12
            # to offer an enjoyable experience.
        self[0x4497] = random.randint(0,255 -12)
        self[0x44D9] = random.randint(self[0x4497 + 12],255)


        # This is the Y acceleration for going up!
        self[0x00454A] = random.randint(22, 0xFF)  # Default : 20  # Decceleration from going down to up
        self[0x004559] = self[0x454A]  # default : 30  # Acceleration from down to up

    def fuel_randomizer(self):
        """ 
            This function will randomize the following stuffs:
                - Fuel related stuffs
                - Invicibility timer
        """
        random.seed(self.seed)

        # This is for the fuel consumption.
            # On press A
            # Default value is 2, which is abysmal IMO. So let's crank it a big notch :D
            # The possible range is 0 (free fuel!) up to 254
            # The double thruster is always higher by at least one.
        self[0x386B7] = random.randint(0,254)  # Normal
        self[0x386AF] = random.randint(self[0x386B7], 255)  # Thruster

        # This is the starting fuel.
            # Default value is E0 for 224 * 255 unit.
            # In other words, you start with 57 120 fuel!
            # this is a big number. So let's crank it down, shall we?
            # The goal is to have a minimum where you have to not use fuel
            # and use momentum to travel to save on fuel or to find and use fuel tanks.
        self[0x7202] = random.randint(1,255)  # Home
        self[0x8589] = random.randint(self[0x7202], 255)  # Fuel tanks
            # So it will always either give you more health
            # or give the same max health



        # This is for the invicibility timer on wall collision.
            # Default value is 30 (28 in decimal).
            # This self run 30 FPS per seconds I think. So you have 1 second of invicibility.
            # Let's alter this a little bit.
            # 1 being no invicibility at all
            # 255 being the max value of a byte
        self[0x11011] = random.randint(1,255)

    def gravity_randomizer(self, seed, test):
        gravity = test# random.randint(0,255)  # FIXME
        self[0x01040D] = 169  # This is the operation
        self[0x01040E] = gravity # This is the operand. Normally it's F8.
        self[0x0107B3] = 169
        self[0x0107B4] = gravity

    def items_randomizer(self, logic=True):
        self.disable_p2_timeditem()
        if logic is False:
            self.flags += "i"
            for planet in planetitems.keys():
                random.shuffle(planetitems[planet])
                for no,offset in enumerate(planetad[planet]):
                    self[offset] = planetitems[planet][no]

            # Do something for planet 2!


    def palette_randomizer(self):
        random.seed(self.seed)
        colors = nescolors()
        #Create the pool of colors

        # HUD display
        self[0x75E2] = random.choice(colors)  # Score palette
        self[0x753C] = self[0x75E2]  # Score palette too
        self[0x75E3] = random.choice(colors)  # Bars palette
        # Rocket palette
        self[0x75D8] = random.choice(colors[0:27])  # Main color
        self[0x75D7] = colors[getnewcolor(colors.index(self[0x75D8]), colors)]  # secondary color
        self[0x75E1] = self[0x75D8] # Icon color is the same as the main color
        self[0x00753B] = self[0x75D8]
        # self[0x75D6] = random.choice(colors)  # window color

        self[0x75ac] = random.choice(colors)  # Title screen dots + jetpack fire
        #self[0x0075ad] = random.choice(colors) # C'est le milieu
        #self[0x0075aE] = random.choice(colors)  # C'est l'autre

    def rocket_randomizer(self):
        """
            This function will randomize these elements:
                - X/Y Acceleration of the rocket
                - Speed max of the rocket
        """
        random.seed(self.seed)
        self.flags += "r"
        # Randomize Rocket speedmaxs:
            # The original value is 3, which is slow IMO.
            # So the randomizer will randomize to something higher.
            # The goal is to have a worst case scenario of vanilla feature,
            # and a "best case scenario" where the speed is very high.

            # From my testing, 8 seemed to be a nice max speed. Can see stuffs coming.
            # Can manage to a certain extent with the least powerful rocket. It's hard, but
            # Doable.

            # NOTE : This randomize the max speed of the warhead things too!
        self[0x3b8a3] = random.randint(3,8)  # x speed
        self[0x3b8ac] = self[0x3B8a3]  # x speed
        self[0x3b909] = self[0x3B8a3]  # y speed
        self[0x3b912] = self[0x3B8a3]  # y speed



        # Randomize acceleration!
            # Either flip the acceleration table, linearize it or keep it.
            # Then randomize the highest, then keep the same ratio.
        randoaccel = getdistributionaccel()
        self[0x38866] = random.randint(int(22 * self[0x3b8a3] - 46), 255)   # This is the max accel.
            # MIN accels:
                # 3 = 20
                # 4 = 42
                # 5 = 64
                # 6 = 86
                # 7 = 108
                # 8 = 130
        # Vanilla is 64
        ratio = self[0x38866] / 64
        self[0x38867] = int(randoaccel[-2] * ratio)
        self[0x38868] = int(randoaccel[-3] * ratio)
        self[0x38869] = int(randoaccel[-4] * ratio)
        self[0x3886A] = int(randoaccel[-5] * ratio)
        self[0x3886B] = int(randoaccel[-6] * ratio)
        self[0x3886C] = int(randoaccel[-7] * ratio)
        self[0x3886D] = int(randoaccel[-8] * ratio)
        self[0x3886E] = 0 # I don't change this, but just to "Know that it's considered" I'm writting it down.

    def weapon_randomizer(self):
        random.seed(self.seed)
        # Smart bombs:
            # There isn't much to be done with them.
            # They instantly remove enemies on screen.
            # Could be potentially broken if really cheap Wusage
        self[0x4EBC] = random.randint(1,255)  # Weapon usage
            #TODO: Finetune this randomizer so it's not broken all the time

        # Anti Gravity:
            # There isn't much to be done with them. 
            # They simply remove gravity, 
            # at the expense of Wusage per frame
        self[0x3ED7] = random.randint(1,255) # Wusage

        # Time Bomb
        self[0x4EBE] = random.randint(1,255)  # Wusage


        # Star Bullet
        self[0x4EC1] = random.randint(1,255)  # Star bullet

        # Warhead / Homing missile:
            # They are the same thing, but the warhead don't leave after one hit
            # The prices are split though.
        self[0x4EBA] = random.randint(1,255)  # Homing Missile Wusage
        self[0x4EBF] = random.randint(1,255)  # Multi Warhead Wusage
        self[0x004dc1] = random.randint(1,255)  # Timer for Warhead stay
            #TODO: Make sure they stay long enough to be bearable.

        # Randomize the acceleration (So their behaviour aren't always the same :o) )
        distri = getwarheadaccel()
        self[0x03c3c2] = 0
        self[0x03c3c4] = random.randint(1, 255)  #20
        self[0x03c3c3] = int(distri[-2] * (self[0x03c3c4] / distri[-1])) # 14

        self[0x03c3c5] = self[0x03c3c3] # 14
        self[0x03c3c6] = self[0x03c3c2]  # 0
        self[0x03c3c7] = self[0x03c3c3]  # 14
        self[0x03c3c8] = self[0x03c3c4]  # 20
        self[0x03c3c9] = self[0x03c3c3]  # 14
##########################CHANGES###################################
    def disable_max4(self):
        self.setmulti(0x0048D4, 0x0048D6, 0xEA)  # For the pod
        self.setmulti(0x4490,0x4492, 0xEA)  # For the astronaut
        self.setmulti(0x4c47,0x004c6a,0xEA)  # Ceci semble fonctionner

        # This is the new "vanilla max speed"
        self[0x3a25] = 3
        self[0x3a2E] = self[0x3a25]  # X speed
        self[0x3a8f] = 3  # up maxspeed Y up
        self[0x3a98] = self[0x3a8f]

    def lastlevel_rocks_lessdamage(self):
        self[0x83F7] = 0x25

    def disable_p2_timeditem(self):
        self.setmulti(0x2A69, 0x2A8E, 0xEA)

    def disable_ohko(self):
        self[0x008403] = 234
        self[0x008404] = 234
        self[0x008405] = 234
        self[0x008406] = 234

    def disable_fuelloss_collisions(self):
        self[0x11030] = 234
        self[0x11031] = 234
        self[0x11036] = 234
        self[0x11037] = 234

    def disable_shield_fuelusage(self):
        self[0x0049f0] = 0
        self[0x0049f1] = 0

    def disable_fuelusage(self):
        self[0x386B7] = 0  # Normal
        self[0x386AF] = 0

    def disable_springeffect(self):
        self[0x48A1] = 0xEA
        self[0x48A2] = 0xEA
        self[0x48A3] = 0xEA
        self[0x48A4] = 0xEA
        self[0x48A5] = 0xEA
        self[0x48A6] = 0xEA
        self[0x48A7] = 0xEA
        self[0x48A8] = 0xEA
        self[0x48A9] = 0xEA
###########################MODES####################################
    def mode_reckless(self):  # COMPLETE
        self.mode = "reckless"
        self.disable_ohko()
        self.disable_fuelloss_collisions()

    def mode_lateral(self):  # COMPLETE
        self.mode = "lateral"
        self.disable_springeffect()

        # These codes will change the code so that gravity 
        # will affect X speed instead of Y speed
        self[0x388A6] = 0x36
        self[0x388BE] = 0x86
        self[0x388BF] = 0xB8  
        self[0x388AD] = 0xA1
        self[0x388AE] = 0xB8
        self[0x388b2] = 0x36
        self[0x388B7] = 0x36

    def mode_improved(self):
        self.disable_springeffect()
        self.disable_p2_timeditem()

        # What I want to add:
            # fixed damage instead of OHKO from enemies bullet
            # Easier to transport golden warship
            # No planet 13 labyrinth
            # last level no ohko walls please

    def mode_goldhunt(self):  # COMPLETE
        self.mode = "goldhunt"

        # With these codes, the fuel is no longer needed
        # to complete the planets
        self[0x11a4a] = 0x19
        self[0x11E41] = 0x19
        self[0x11C93] = 0x19
        self[0x11a68] = 0x19
        self[0x11c2f] = 0x19
        self[0x11dc4] = 0x19
        self[0x11ad1] = 0x19
        self[0x11ce8] = 0x19
        self[0x11eb9] = 0x19
        self[0x11d5b] = 0x19
        self[0x11f2c] = 0x19
        self[0x11b4e] = 0x19
        self[0x11bcb] = 0x19


        planetads = items_offsets_all()
        for offset in planetads:
            if self[offset] == fuel:
                self[offset] = fueltank
