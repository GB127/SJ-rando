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
        self.infos = {
                        hex(0x75D6) : "Rocket window palette" ,
                        hex(0x75D7) : "Rocket main palette",
                        hex(0x75E1) : "Rocket icon palette",
                        hex(0x75D8) : "Rocket sec palette",
                        hex(0x75E2) : "Score palette",
                        hex(0x75E3) : "Bars palette",
                        hex(0x753C) : "Palette intro level",  # FIXME
                        hex(0x753D) : "Palette intro level", # FIXME
                        hex(0x753E) : "Palette intro level", # FIXME
                        hex(0x75AC) : "Dot palette of Title screen",
                        hex(0x99) : "Wall invicibility timer"
                    }
        self.categories ={"palettes" : [hex(0x75D6), hex(0x75D7),hex(0x75E1),
                                        hex(0x75D8), hex(0x75E2),hex(0x75E3),
                                        hex(0x75AC), hex(0x753C),hex(0x753D),hex(0x753E)]
                        }

    def check(self,adress):
        if isinstance(adress,str):
            return self.infos[adress]
        else:
            return self.infos[hex(adress)]


    def pcheck(self,adress):
        print(self.check(adress))

    def listadresses(self,key):
        print("------------------------------")
        for adress in self.categories[key]:
            print(adress, " : ",  self.check(adress))
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