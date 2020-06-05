class infos:
    """
        This class is more of a tool for me. I will store my findings of infos here.
        And if I need to get an info during my coding, I'll simply call this class and then ask it to
        Retrieve the things I need.
    """
    def __init__(self):
        self.infos = {
                        # Infos
                            hex(0x99)    : "Current Wall invicibility timer",  # INFO
                            hex(0xC6)    : "Rocket Current fuel (2B)",  # INFO
                            hex(0x4C)    : "Camera Xpos",  # INFO
                            hex(0x4E)    : "Camera Ypos",  # INFO
                            hex(0x5D)    : "Level timer",  # INFO
                            hex(0x0200)  : "Rocket Xpos",  # INFO
                            hex(0x021F)  : "Rocket Xpos * 256",  # INFO
                            hex(0x0197)  : "Rocket subXpos",  # INFO
                            hex(0x029B)  : "Rocket Xspeed",  # INFO
                            hex(0x02BA)  : "Rocket Xspeed *256",  # INFO
                            hex(0x025D) : "Rocket Ypos",  # INFO
                            hex(0x027C) : "Rocket Ypos*256",  # INFO
                            hex(0x023E) : "Rockey subYpos",  # INFO
                            hex(0x02D9) : "Rocket Yspeed",  # INFO
                            hex(0x02F8) : "Rocket Yspeed * 256",  # INFO
                        # REMOVED STUFFS
                            hex(0x0048D3) : "Rocket Xspeed Yspeed 256 max speed 2? (REMOVED FROM THE BASE GAME)",  # Done
                            hex(0x00448F) : "Astronaut Xspeed max? (REMOVED FROM THE BASE GAME)",


                        # To verify and test


                        # Astronaut



                            hex(0x4497) : "Astronaut 'Horizontal gravity'",
                            hex(0x44D9) : "Astronaut X acceleration",
                            hex(0x03B909) : "Rocket & Astronaut max Yspeed * 256 compare",  #  DONE
                            hex(0x03B912) : "Rocket & Astronaut max Yspeed * 256 set if max", # DONE
                            hex(0x003a98) : "Astronaut up Yspeed max",  # DONE
                            hex(0x3a8f) : "Astronaut up Yspeed max",  # DONE
                            hex(0x003a2e) : "Astronaut Xspeed max",  # DONE
                            hex(0x003a25) : "Astronaut Xspeed max",  # DONE
                            hex(0x00454A) : "Astronaut Yacceleration",  # DONE
                            hex(0x004559) : "Astronaut Yacceleration",  # DONE




                        # Fuel:
                            hex(0x8589) :  "Fuel tank refill amount",  # DONE
                            hex(0x0386B7): "Rocket fuel consumption on press A, default value = 2",  # DONE
                            hex(0x0386AF) : "fuel usage thruster Default value = 10",  # DONE

                            hex(0x0049f0) : "opcode Decrement 1st byte of shield usage",
                            hex(0x0049f1) : "opcode Decrement 2nd byte of shield usage",

                            hex(0x008403) : "Fuel STA on enemy bullet hit",
                            hex(0x008404) : "Operand for 0x008403",
                            hex(0x008405) : "Fuel STA on enemy bullet hit",
                            hex(0x008406) : "Operand for 0x008403",

                            hex(0x11030) : "Wall Collision substract fuel opcode",
                            hex(0x11031) : "Wall Collision suubstract fuel opcode",
                            hex(0x11036) : "Wall Collision substract fuel opcode",
                            hex(0x11037) : "Wall Collision substract fuel opcode",

                            hex(0x011011): "Wall Invicibility timer Duration, default value = 30",  # Done
                            hex(0x007202) : "Starting fuel and weapon, Default value = E0(224)",  # DONE


                        # Palettes:
                            hex(0x00753B) : "Icon Rocket Intro palette",  # Done
                            hex(0x0075ad): "Astronaut fire palette intro",
                            hex(0x0075aE): "Astronaut fire palette intro 2",
                            hex(0x75D7)  : "Rocket main palette",  # DONE
                            hex(0x75E1)  : "Rocket icon palette",  # DONE
                            hex(0x75D8)  : "Rocket sec palette",  # DONE
                            hex(0x75E2)  : "Score palette",  # DONE
                            hex(0x75E3)  : "Bars palette",  # DONE
                            hex(0x753C)  : "score palette intro level",  # DONE
                            hex(0x75AC)  : "palette of dot Title screen",  # DONE
                            hex(0x75D6)  : "Rocket window palette" ,


                        # Rocket:
                            hex(0x03B8A3) : "Rocket max Xspeed * 256",
                            hex(0x03B8AC) : "Rocket max Xspeed * 256",
                            hex(0x03B909) : "Rocket & Astronaut max Yspeed * 256 compare",  #  DONE
                            hex(0x03B912) : "Rocket & Astronaut max Yspeed * 256 set if max", # DONE


                            hex(0x0374)  : "Direction of the Rocket",  # INFO

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
                            hex(0x38870) : "Rocket accelerationx dir = 18, Default = 18",  #DONE
                            hex(0x38871) : "Rocket accelerationx dir = 19, Default = 23",  #DONE
                            hex(0x38872) : "Rocket accelerationx dir = 20, Default = 2D",  #DONE
                            hex(0x38873) : "Rocket accelerationx dir = 21, Default = 35",  #DONE
                            hex(0x38874) : "Rocket accelerationx dir = 22, Default = 3B",  #DONE
                            hex(0x38875) : "Rocket accelerationx dir = 23, Default = 3E",  #DONE


                        # Gravity:
                            hex(0x01040D) : "Gravity AND for display",
                            hex(0x01040E) : "Gravity operand for AND for display",
                            hex(0x0107B3) : "Gravity AND for actual gravity",
                            hex(0x0107B4) : "Gravity operand for actual AND gravity",

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

                        # Items:
                            hex(0x510) : "Planet's items are stored in this range, starting from here",
                            hex(0x37F) : "Item sprite display?",
                            hex(0x3BD) : "Item ID! or pointer....",
                                # 1 : Extra life
                                # 2 : Crash (Nice visual crash)
                                # 3 : shield
                                # 4 : Booster
                                # 5 : Pts
                                # 6 : Map¸
                                # 7 : Garbled sprite?
                                # 8 : Garbled
                                # 9 : Points item
                                # A : Fuel
                                # B : Fuel Tank
                                # C : Points item (Radioactive item)
                                # F : Crystal
                                # 10 : Crystal
                                # 11 : Warp for item transported too
                                # 12 : Warp for golden ship
                                # 13 : Golden part!
                                # 18 : Fuel (I'm sure there is a range for this)
                                # 1A : Warp for planet 2 middle section
                                # 1B : Minigame Warp

                                # Planet 1:
                                    hex(0x11a4a) : "Fuel bar planet 1 (Default = 0x18)",  # Do not change
                                    hex(0x11a4F) : "Minigame warp planet 1 left mother ship",  # Warp left of mother ship
                                    hex(0x11a54) : "Shield planet 1",  # Shield (Down left of mother ship)
                                    hex(0x11a59) : "Crystal planet 1",  # Crystal of planet 1
                                    hex(0x11a5E) : "Fuel planet 1",  # Fuel of planet 1
                                    hex(0x11a63) : "Warp for golden ship planet 1",  # Warp for golden ship


                                # Planet 2 :
                                        hex(0x11E41) : "Planet 2 (Default : 0x16)",  # Fuel sprite
 
                                        hex(0x11E46) : "Planet 2 (Default : 0x1A",  # It's the warp to the center
                                        hex(0x11E4B) : "Planet 2 (Default : 0x12",  # It's the warp to the golden ship
                                        hex(0x11E50) : "Planet 2 (Default : 0x4",  # Booster
                                        hex(0x11E55) : "Planet 2 (Default : 0x6",  # Map
                                        hex(0x11E5A) : "Planet 2 (Default : 0xA",  # Fuel on the right of mother ship

                                        hex(0x11E5F) : "Planet 2 (Default : 0xF",  # Crystal in the left tunnel
                                        hex(0x11E64) : "Planet 2 (Default : 0xA",  # Bottom fuel
                                        hex(0x11E69) : "Planet 2 (Default : 0x9",  # Middle section bottom points
                                        hex(0x11E6E) : "Planet 2 (Default : 0xF",  # Middle section crystal
                                        hex(0x11E73) : "Planet 2 (Default : 0xA",  # Fuel on the left of mother ship

                                        hex(0x11E78) : "Planet 2 (Default : 0xC",  # Middle section radioactive item (Upper left section)
                                        hex(0x11E7D) : "Planet 2 (Default : 0x9",  # Points on the far right of mother ship
                                        hex(0x11E82) : "Planet 2 (Default : 0xA",  # Fuel left tunnel
                                        hex(0x11E87) : "Planet 2 (Default : 0x11", # Astro warp left tunnel
                                        hex(0x11E8C) : "Planet 2 (Default : 0x9", # Middle section points item upper section

                                        hex(0x11E91) : "Planet 2 (Default : 0xB",  # Fuel tank bottom section
                                        hex(0x11E96) : "Planet 2 (Default : 0x11",  # Middle section astro warp
                                        hex(0x11E9B) : "Planet 2 (Default : 0x11",  # Astro warp right tunnel
                                        hex(0x11EA0) : "Planet 2 (Default : 0xB",  # Unused item?
                                        hex(0x11EA5) : "Planet 2 (Default : 0x11",  # Unused item?

                                        hex(0x11EAA) : "Planet 2 (Default : 0x1",  # One of the lives on the bottom area
                                        hex(0x11EAF) : "Planet 2 (Default : 0x1",  # One of the lives on the bottom area
                                        hex(0x11EB4) : "Planet 2 (Default : 0x1",  # One of the lives on the bottom area

                                # Planet 3:
                                    hex(0x11C93) : "Fuel mothership, Default value = 0x15",
                                    hex(0x11C98) : "Default value : 0x12",
                                    hex(0x11C9D) : "Default value : 0xA",
                                    hex(0x11CA2) : "Default value : 0xF",
                                    hex(0x11CA7) : "Default value : 0xA",
                                    hex(0x11CAC) : "Default value : 0xA",

                                    hex(0x11CB1) : "Default value : 0x10",
                                    hex(0x11CB6) : "Default value : 0xA",
                                    hex(0x11CBB) : "Default value : 0x5",
                                    hex(0x11CC0) : "Default value : 0x9",
                                    hex(0x11CC5) : "Default value : 0xC",
                                    
                                    hex(0x11CCA) : "Default value : 0x9",
                                    hex(0x11CCF) : "Default value : 0x11",
                                    hex(0x11CD4) : "Default value : 0xB",
                                    hex(0x11CD9) : "Default value : 0x11",
                                    hex(0x11CDE) : "Default value : 0x1",
                                    
                                    hex(0x11CE3) : "Default value : 0x1",

                                # Planet 4:
                                    hex(0x11a68) : "Mother ship fuel sprite (Default 0x16)",
                                    hex(0x11a6D) : "Default value : 0x12",
                                    hex(0x11a72) : "Default value : 0xA",
                                    hex(0x11a77) : "Default value : 0x10",
                                    hex(0x11a7c) : "Default value : 0xA",
                                    hex(0x11a81) : "Default value : 0xA",
                                    hex(0x11a86) : "Default value : 0xF",
                                    hex(0x11a8B) : "Default value : 0x9",
                                    hex(0x11a90) : "Default value : 0xC",
                                    hex(0x11a95) : "Default value : 0x5",
                                    hex(0x11a9A) : "Default value : 0x5",
                                    hex(0x11a9F) : "Default value : 0xB",
                                    hex(0x11aA4) : "Default value : 0xB",
                                    hex(0x11aA9) : "Default value : 0x9",
                                    hex(0x11aAE) : "Default value : 0xB",
                                    hex(0x11aB3) : "Default value : 0x11",
                                    hex(0x11aB8) : "Default value : 0x11",
                                    hex(0x11aBD) : "Default value : 0x11",
                                    hex(0x11aC2) : "Default value : 0x1",
                                    hex(0x11aC7) : "Default value : 0x1",
                                    hex(0x11aCC) : "Default value : 0x1",

                                # Planet 5
                                    hex(0x11c2f) : "Item",
                                    # Bonds de 5
                                    hex(0x11c8E) : "Item",


                                # Planet 6:
                                    hex(0x11dc4) : "Item",
                                    # Bonds de 5
                                    hex(0x11e3C) : "Item",

                                # Planet 7:
                                    hex(0x011ad1) : "Item",
                                    # Bonds de 5
                                    hex(0x011b49) : "Item",

                                # Planet 8:
                                    hex(0x011CE8) : "Item",
                                    # Bonds de 5
                                    hex(0x011d56) : "Item",

                                # Planet 9:¸
                                    hex(0x11EB9) : "Item",
                                    # Bonds de 5
                                    hex(0x011F27) : "Item",

                                # Planet 10:
                                    hex(0x11d5b) : "Item",
                                    # Bonds de 5
                                    hex(0x011dbf) : "Item",
                                
                                # Planet 11:
                                    hex(0x11F2C) : "Item",
                                    # ...
                                    hex(0x11f9f) : "Item",

                                # Planet 12:
                                    hex(0x11B4E) : "Item",
                                    # ...
                                    hex(0x11bc6) : "Item",

                                # Planet 13:
                                    hex(0x11BCB) : "Item",
                                    # ...
                                    hex(0x11C2A) : "Item",
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

planetitems ={
    "1" : [0x1B, 0x03, 0x10, 0xA  ,0x12],
    "2" : [0x1A, 0x12, 0x04, 0x06, 0x0A,
           0xF , 0xA , 0x09, 0xF , 0xA ,
           0xC , 0x9 , 0xA , 0x11, 0x9 ,
           0xB , 0x11, 0x11, 0x1 , 0x1 ,
           0x1 ],
    "4" : [0x12, 0xA , 0x10, 0xA , 0xA ,
           0xF , 0x9 , 0xC , 0x5 , 0x5 ,
           0xB , 0xB , 0x9 , 0xB , 0x11,
           0x11, 0x11, 0x1 , 0x1 , 0x1],
    "3" : [0x12, 0xA , 0xF , 0xA , 0xA ,
           0x10, 0xA , 0x5 , 0x9 , 0xC ,
           0x9 , 0x11, 0xB , 0x11, 0x1 ,
           0x1],
    "5" : [],
    "6" : [],
    "7" : [],
    "8" : [],
    "9" : [],
    "10" : [],
    "11" : [],
    "12" : [],
    "13" : [],
    "14" : []
}
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