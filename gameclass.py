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
                        hex(0x00454A) : "Astronaut Yacceleration",
                        hex(0x004559) : "Astronaut Yacceleration",
                        hex(0x008403) : "Fuel STA on enemy bullet hit",
                        hex(0x008404) : "Operand for 0x008403",
                        hex(0x008405) : "Fuel STA on enemy bullet hit",
                        hex(0x008406) : "Operand for 0x008403",
                        hex(0x75D6)  : "Rocket window palette" ,
                        hex(0x0022AD) : "Green points 25pts",
                        hex(0x75D7)  : "Rocket main palette",
                        hex(0x75E1)  : "Rocket icon palette",
                        hex(0x75D8)  : "Rocket sec palette",
                        hex(0x75E2)  : "Score palette",
                        hex(0x75E3)  : "Bars palette",
                        hex(0x11030) : "Wall Collision substract fuel opcode",
                        hex(0x11031) : "Wall Collision suubstract fuel opcode",
                        hex(0x11036) : "Wall Collision substract fuel opcode",
                        hex(0x11037) : "Wall Collision substract fuel opcode",
                        hex(0x753C)  : "score palette intro level",
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
                        hex(0x03B909) : "Rocket & Astronaut max Yspeed * 256 compare",
                        hex(0x03B912) : "Rocket & Astronaut max Yspeed * 256 set if max",
                        hex(0x0048D3) : "Rocket Xspeed Yspeed 256 max speed 2",
                        hex(0x38866) : "Rocket accelerationx dir = 8, Default= 40",
                        hex(0x38867) : "Rocket accelerationx dir = 9, Default = 3E",
                        hex(0x38868) : "Rocket accelerationx dir = 10, Default = 3B",
                        hex(0x38869) : "Rocket accelerationx dir = 11, Default = 35",
                        hex(0x3886A) : "Rocket accelerationx dir = 12, Default = 2D",
                        hex(0x3886B) : "Rocket accelerationx dir = 13, Default = 23",
                        hex(0x3886C) : "Rocket accelerationx dir = 14, Default = 18",
                        hex(0x3886D) : "Rocket accelerationx dir = 15, Default = 0C",
                        hex(0x3886E) : "Rocket accelerationx dir = 16, Default = 00",
                        hex(0x3886F) : "Rocket accelerationx dir = 17, Default = 0C",
                        hex(0x38870) : "Rocket accelerationx dir = 18 Default = 18",
                        hex(0x38871) : "Rocket accelerationx dir = 19, Default = 23",
                        hex(0x38872) : "Rocket accelerationx dir = 20, Default = 2D",
                        hex(0x38873) : "Rocket accelerationx dir = 21, Default = 35",
                        hex(0x38874) : "Rocket accelerationx dir = 22, Default = 3B",
                        hex(0x38875) : "Rocket accelerationx dir = 23, Default = 3E",
                        hex(0x8589) :  "Fuel tank refill amount",
                        hex(0x00448F) : "Astronaut Xspeed max",
                        hex(0x003a25) : "Astronaut Xspeed max2",
                        hex(0x003a2e) : "Astronaut Xspeed max3",
                        hex(0x003a98) : "Astronaut fastfall Yspeed max",
                        hex(0x3a8f) : "Astronaut fastfall Yspeed max"
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
        self.data[offset] = value

    def checkchange(self,adress):
        print(self[adress-2: adress +2])