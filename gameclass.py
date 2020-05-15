class InfoError(BaseException):
    # We'll see if I need this. But for now I'm not seeing any use
    pass

class infos:
    """
        This class is more of a tool for me. I will store my findings of infos here.
        And if I need to get an info during my coding, I'll simply call this class and then ask it to
        Retrieve the things I need.
    """
    def __init__(self):
        # List of infos:
            # palette
            # pos
                # Xpos
                # Ypos
            # timer
            # Rocket¸
            # speed
            # max
            # fuel
            # points
        self.PC = {"?? : CC37" : "Something with Spx",
                   "0E : B886": "Add Xspeed",
                   "0E : B907" : "Decrease Yspeed",
                   "OE : B8EC" : "Increase Yspeed"}
        self.infos = {
                        hex(0x75D6)  : "Rocket window palette" ,
                        hex(0x0022AD) : "Green points 25pts",
                        hex(0x75D7)  : "Rocket main palette",
                        hex(0x75E1)  : "Rocket icon palette",
                        hex(0x75D8)  : "Rocket sec palette",
                        hex(0x75E2)  : "Score palette",
                        hex(0x75E3)  : "Bars palette",
                        hex(0x753C)  : "palette intro level",  # FIXME
                        hex(0x753D)  : "palette intro level", # FIXME
                        hex(0x753E)  : "palette intro level", # FIXME
                        hex(0x75AC)  : "palette of dot Title screen",
                        hex(0x99)    : "Current Wall invicibility timer",
                        hex(0x011011): "Wall Invicibility timer Duration, default value = 30",
                        hex(0x0386B7): "Rocket fuel consumption on press A, default value = 2",
                        hex(0xC6)    : "Rocket Current fuel (2B)",
                        hex(0x0374)  : "Direction of the Rocket",
                        hex(0x4C)    : "Camera Xpos",
                        hex(0x007202) : "Starting fuel and weapon, Default value = E0(224)",
                        hex(0x4E)    : "Camera Ypos",
                        hex(0x5D)    : "Level timer",
                        hex(0x0200)  : "Rocket Xpos",
                        hex(0x021F)  : "Rocket Xpos * 256",
                        hex(0x0197)  : "Rocket subXpos",
                        hex(0x029B)  : "Rocket Xspeed",
                        hex(0x02BA)  : "Rocket Xspeed *256",
                        hex(0x025D) : "Rocket Ypos",
                        hex(0x0386AF) : "fuel usage thruster Default value = 10",
                        hex(0x027C) : "Rocket Ypos*256",
                        hex(0x023E) : "Rockey subYpos",
                        hex(0x02D9) : "Rocket Yspeed",
                        hex(0x02F8) : "Rocket Yspeed * 256",
                        hex(0x03B8A3) : "Rocket Xspeed * 256 max compare",
                        hex(0x03B8AC) : "Rocket Xspeed * 256 max set if max",
                        hex(0x03B909) : "Rocket max Yspeed * 256 compare",
                        hex(0x03B912) : "Rocket max Yspeed * 256 set if max",
                        hex(0x0048D3) : "Rocket Xspeed Yspeed 256 max speed 2"

                    }
    def check(self,adress):
        if isinstance(adress,str):
            return adress + " : " + self.infos[adress]
        else:
            return hex(adress) + " : " + self.infos[hex(adress)]

    def listadresses(self,*seeked):
        print("-----------LIST OF ADRESSES-------------------")
        for i in list(self.infos):
            for key in seeked:
                if self.infos[i].count(key) > 0:
                    print(self.check(i))
        print("-----------END OF ADRESSES--------------------")


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
        print(f'{hex(offset)} has been set to {hex(value)}')  # FIXME
        self.data[offset] = value

    def checkchange(self,adress):
        print(self[adress-2: adress +2])