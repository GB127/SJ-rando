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
            # Rocket
            # speed
            # max
            # fuel
            # points
        self.infos = {
                        hex(0x03b919): "opcode Gravity Y speed",
                        hex(0x03b91A) : "operande Yspeed - gravity, low byte  Yspeed",
                        hex(0x03b91B): "operange Yspeed - gravity hight byte, Yspeed",

                        hex(0x03b922): "opcode Gravity Y speed, H",
                        hex(0x03b923) : "operande Yspeed - gravity, low byte  Yspeed H",
                        hex(0x03b924): "operange Yspeed - gravity hight byte, Yspeed H",


                        hex(0x0049f0) : "opcode Decrement 1st byte of shield usage",
                        hex(0x0049f1) : "opcode Decrement 2nd byte of shield usage",
                        hex(0x00454A) : "Astronaut Yacceleration",
                        hex(0x004559) : "Astronaut Yacceleration",
                        hex(0x008403) : "Fuel STA on enemy bullet hit",
                        hex(0x01040D) : "Gravity AND for display",
                        hex(0x01040E) : "Gravity operand for AND for display",
                        hex(0x0107B3) : "Gravity AND for actual gravity",
                        hex(0x0107B4) : "Gravity operand for actual AND gravity",
                        hex(0x008404) : "Operand for 0x008403",
                        hex(0x008405) : "Fuel STA on enemy bullet hit",
                        hex(0x008406) : "Operand for 0x008403",
                        hex(0x75D6)  : "Rocket window palette" ,
                        hex(0x0022AD) : "Green points 25pts",
                        hex(0x75D7)  : "Rocket main palette",  # DONE
                        hex(0x75E1)  : "Rocket icon palette",  # DONE
                        hex(0x75D8)  : "Rocket sec palette",  # DONE
                        hex(0x75E2)  : "Score palette",  # DONE
                        hex(0x75E3)  : "Bars palette",  # DONE
                        hex(0x11030) : "Wall Collision substract fuel opcode",
                        hex(0x11031) : "Wall Collision suubstract fuel opcode",
                        hex(0x11036) : "Wall Collision substract fuel opcode",
                        hex(0x11037) : "Wall Collision substract fuel opcode",
                        hex(0x753C)  : "score palette intro level",  # DONE
                        hex(0x75AC)  : "palette of dot Title screen",  # DONE
                        hex(0x99)    : "Current Wall invicibility timer",  # INFO
                        hex(0x011011): "Wall Invicibility timer Duration, default value = 30",  # Done
                        hex(0x0386B7): "Rocket fuel consumption on press A, default value = 2",  # DONE
                        hex(0xC6)    : "Rocket Current fuel (2B)",  # INFO
                        hex(0x0374)  : "Direction of the Rocket",  # INFO
                        hex(0x4C)    : "Camera Xpos",  # INFO
                        hex(0x007202) : "Starting fuel and weapon, Default value = E0(224)",  # DONE
                        hex(0x4E)    : "Camera Ypos",  # INFO
                        hex(0x5D)    : "Level timer",  # INFO
                        hex(0x0200)  : "Rocket Xpos",  # INFO
                        hex(0x021F)  : "Rocket Xpos * 256",  # INFO
                        hex(0x0197)  : "Rocket subXpos",  # INFO
                        hex(0x029B)  : "Rocket Xspeed",  # INFO
                        hex(0x02BA)  : "Rocket Xspeed *256",  # INFO
                        hex(0x025D) : "Rocket Ypos",  # INFO
                        hex(0x0386AF) : "fuel usage thruster Default value = 10",  # DONE
                        hex(0x027C) : "Rocket Ypos*256",  # INFO
                        hex(0x023E) : "Rockey subYpos",  # INFO
                        hex(0x02D9) : "Rocket Yspeed",  # INFO
                        hex(0x02F8) : "Rocket Yspeed * 256",  # INFO
                        hex(0x03B8A3) : "Rocket Xspeed * 256 max compare",  # INFO
                        hex(0x03B8AC) : "Rocket Xspeed * 256 max set if max",  # INFO
                        hex(0x03B909) : "Rocket & Astronaut max Yspeed * 256 compare",  #  DONE
                        hex(0x03B912) : "Rocket & Astronaut max Yspeed * 256 set if max", # DONE
                        hex(0x0048D3) : "Rocket Xspeed Yspeed 256 max speed 2",  # Done
                        hex(0x38866) : "Rocket accelerationx dir = 8, Default= 40",  #DONE
                        hex(0x38867) : "Rocket accelerationx dir = 9, Default = 3E",  #DONE
                        hex(0x38868) : "Rocket accelerationx dir = 10, Default = 3B",  #DONE
                        hex(0x38869) : "Rocket accelerationx dir = 11, Default = 35",  #DONE
                        hex(0x3886A) : "Rocket accelerationx dir = 12, Default = 2D",  #DONE
                        hex(0x3886B) : "Rocket accelerationx dir = 13, Default = 23",  #DONE
                        hex(0x3886C) : "Rocket accelerationx dir = 14, Default = 18",  #DONE
                        hex(0x3886D) : "Rocket accelerationx dir = 15, Default = 0C",  #DONE
                        hex(0x3886E) : "Rocket accelerationx dir = 16, Default = 00",  #DONE
                        hex(0x3886F) : "Rocket accelerationx dir = 17, Default = 0C",  #DONE
                        hex(0x38870) : "Rocket accelerationx dir = 18 Default = 18",  #DONE
                        hex(0x38871) : "Rocket accelerationx dir = 19, Default = 23",  #DONE
                        hex(0x38872) : "Rocket accelerationx dir = 20, Default = 2D",  #DONE
                        hex(0x38873) : "Rocket accelerationx dir = 21, Default = 35",  #DONE
                        hex(0x38874) : "Rocket accelerationx dir = 22, Default = 3B",  #DONE
                        hex(0x38875) : "Rocket accelerationx dir = 23, Default = 3E",  #DONE
                        hex(0x8589) :  "Fuel tank refill amount",  # DONE
                        hex(0x00448F) : "Astronaut Xspeed max",  # DONE
                        hex(0x003a25) : "Astronaut Xspeed max2",  # DONE
                        hex(0x003a2e) : "Astronaut Xspeed max3",  # DONE
                        hex(0x003a98) : "Astronaut fastfall Yspeed max",  # DONE
                        hex(0x3a8f) : "Astronaut fastfall Yspeed max",  # DONE
                        hex(0x0075ad): "Astronaut fire palette intro",
                        hex(0x0075aE): "Astronaut fire palette intro 2",
                        hex(0x00753B) : "Icon Rocket Intro palette",  # Done

                        # Weapons
                        #Smart bomb
                        hex(0x004EBC) : "Smart Bomb Wusage",  # DONE

                        # Anti-Gravity
                        hex(0x003eD7) : "Anti-Gravity Wusage",  # DONE

                        # Homing missile:
                        hex(0x004eba) : "Homing missile Wusage",  # DONE

                        # Time bomb:
                        hex(0x004ebe): "Time bomb Wusage",  # DONE

                        #Star Bullet:
                        hex(0x004EC1) : "Star Bullet Wusage",  # DONE

                        # Multi Warhead
                        hex(0x004ebf) : "Multi Warhead Wusage",  # DONE
                        hex(0x004dc1) : "Multi Warhead Timer",  # DONE
                        hex(0x03c3c2) : "Warhead accel def = 0",  # DONE
                        hex(0x03c3c3) : "Warhead accel def = 14",  # DONE
                        hex(0x03c3c4) : "Warhead accel def = 20",  # DONME
                        hex(0x03c3c5) : "Warhead accel def = 14",  # DONE
                        hex(0x03c3c6) : "Warhead accel def = 0",  # DONE
                        hex(0x03c3c7) : "Warhead accel def = 14",  # DOne
                        hex(0x03c3c8) : "Warhead accel def = 20",  # DONE
                        hex(0x03c3c9) : "Warhead accel def = 14",  # DONe
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