class InfoError(BaseException):
    # We'll see if I need this. But fo rnow I'm not seeing any use
    pass

class infos:
    """
        This class is more of a tool for me. I will store my findings of infos here.
        And if I need to get an info during my coding, I'll simply call this class and then ask it to
        Retrieve the things I need.
    """
    def __init__(self):
        self.infos = {
                        hex(0x0075D6) : "Rocket window palette" ,
                        hex(0x0075D7) : "Rocket main palette",
                        hex(0x0075E1) : "Rocket icon palette",
                        hex(0x0075D8) : "Rocket sec palette",
                        hex(0x0075E2) : "Score palette",
                        hex(0x0075E3) : "Bars palette"
                    }
        self.categories ={"palettes" : [hex(0x0075D6), hex(0x0075D7),hex(0x0075E1), hex(0x0075D8), hex(0x0075E2),hex(0x0075E3)]
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