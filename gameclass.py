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

        self.infos = {
                        hex(0x75D6)  : "Rocket window palette" ,
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
                        hex(0x011011): "Wall Invicibility timer Duration",
                        hex(0x0386B7): "Rocket fuel consumption on press A",
                        hex(0xC6)    : "Rocket Current fuel (2B)",
                        hex(0x0374)  : "Direction of the Rocket",
                        hex(0x4C)    : "Camera Xpos",
                        hex(0x4E)    : "Camera Ypos",
                        hex(0x5D)    : "Level timer",
                        hex(0x0200)  : "Rocket Xpos",
                        hex(0x021F)  : "Rocket Xpos * 256",
                        hex(0x0197)  : "Rocket subXpos",
                        hex(0x029B)  : "Rocket Xpos speed",
                        hex(0x02BA)  : "Rocket Xpos speed *256"
                    }
    def check(self,adress):
        if isinstance(adress,str):
            return self.infos[adress]
        else:
            return self.infos[hex(adress)]

    def listadresses(self,*seeked):
        print("------------------------------")
        for i in list(self.infos):
            for key in seeked:
                if self.infos[i].count(key) > 0:
                    print(i, " : ", self.check(i))
        print("------------------------------")


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