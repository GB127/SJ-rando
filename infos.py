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
                                # Sub planet
                                    hex(0x11FA4): "Subplanet item",
                                    hex(0x11FA9): "Subplanet item",
                                    hex(0x11FAE): "Subplanet item",

                            # Planet 2 :
                                    hex(0x11E41) : "Planet 2 (Default : 0x16)",  # Fuel sprite
                                    hex(0x11E46) : "Planet 2 warp to the center, near mothership",
                                    hex(0x11E4B) : "Planet 2 Warp to GS, Right tunnel",
                                    hex(0x11E50) : "Planet 2 Booster, to the left of Mother Ship",
                                    hex(0x11E55) : "Planet 2 Map, Bottom left of planet",
                                    hex(0x11E5A) : "Planet 2 Fuel on the right of mother ship",
                                    hex(0x11E5F) : "Planet 2 Crystal left tunnel",
                                    hex(0x11E64) : "Planet 2 Bottom section fuel",
                                    hex(0x11E69) : "Planet 2 Middle section points",  
                                    hex(0x11E6E) : "Planet 2 Middle section crystal",
                                    hex(0x11E73) : "Planet 2 Fuel mothership section",
                                    hex(0x11E78) : "Planet 2 Middle section pts item",
                                    hex(0x11E7D) : "Planet 2 Pts mothership section",
                                    hex(0x11E82) : "Planet 2 Fuel left tunnel",
                                    hex(0x11E87) : "Planet 2 Left tunnel astro warp",
                                    hex(0x11E8C) : "Planet 2 Middle section pts item",
                                    hex(0x11E91) : "Planet 2 Bottom section fuel tank",
                                    hex(0x11E96) : "Planet 2 Middle section astro warp",
                                    hex(0x11E9B) : "Planet 2 Right tunnel astro warp",
                                    hex(0x11EA0) : "Planet 2 item, unused",
                                    hex(0x11EA5) : "Planet 2 item, unused",
                                    hex(0x11EAA) : "Planet 2 Bottom area life",
                                    hex(0x11EAF) : "Planet 2 Bottom area life",
                                    hex(0x11EB4) : "Planet 2 Bottom area life",
                                    #subplanet:
                                        hex(0x11FEF) : "Subplanet item, default 0x11",
                                        hex(0x11FF4) : "Subplanet item, default 0x12",
                                        hex(0x11FF9) : "Subplanet item, default 0x13",
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
                                hex(0x11c2f) : "Default : 0x15",
                                hex(0x11c34) : "Default : 0x12",
                                hex(0x11c39) : "Default : 0x1B",
                                hex(0x11c3E) : "Default : 0x10",
                                hex(0x11c43) : "Default : 0xA",
                                hex(0x11c48) : "Default : 0xF",
                                hex(0x11c4D) : "Default : 0xA",
                                hex(0x11c52) : "Default : 0xA",
                                hex(0x11c57) : "Default : 0xA",
                                hex(0x11c5C) : "Default : 0x9",
                                hex(0x11c61) : "Default : 0x9",
                                hex(0x11c66) : "Default : 0xC",
                                hex(0x11c6B) : "Default : 0xC",
                                hex(0x11c70) : "Default : 0xB",
                                hex(0x11c75) : "Default : 0x11",
                                hex(0x11c7A) : "Default : 0x11",
                                hex(0x11c7F) : "Default : 0xB",
                                hex(0x11c84) : "Default : 0xB",
                                hex(0x11c89) : "Default : 0x1",
                                hex(0x11c8E) : "Default : 0x1",

                            # Planet 6:
                                hex(0x11dc4) : 'default = 0x15',
                                hex(0x11dc9) : 'default = 0x12',
                                hex(0x11dce) : 'default = 0xf',
                                hex(0x11dd3) : 'default = 0x10',
                                hex(0x11dd8) : 'default = 0xa',
                                hex(0x11ddd) : 'default = 0x10',
                                hex(0x11de2) : 'default = 0x10',
                                hex(0x11de7) : 'default = 0xa',
                                hex(0x11dec) : 'default = 0xa',
                                hex(0x11df1) : 'default = 0x10',
                                hex(0x11df6) : 'default = 0xa',
                                hex(0x11dfb) : 'default = 0x9',
                                hex(0x11e00) : 'default = 0x9',
                                hex(0x11e05) : 'default = 0xc',
                                hex(0x11e0a) : 'default = 0xc',
                                hex(0x11e0f) : 'default = 0xc',
                                hex(0x11e14) : 'default = 0xc',
                                hex(0x11e19) : 'default = 0xb',
                                hex(0x11e1e) : 'default = 0x11',
                                hex(0x11e23) : 'default = 0x11',
                                hex(0x11e28) : 'default = 0x11',
                                hex(0x11e2d) : 'default = 0x11',
                                hex(0x11e32) : 'default = 0x1',
                                hex(0x11e37) : 'default = 0x1',
                                hex(0x11e3c) : 'default = 0x1',
                            # Planet 7:
                                hex(0x11ad1) : 'default = 0x16',
                                hex(0x11ad6) : 'default = 0x12',
                                hex(0x11adb) : 'default = 0x10',
                                hex(0x11ae0) : 'default = 0x10',
                                hex(0x11ae5) : 'default = 0xa',
                                hex(0x11aea) : 'default = 0x10',
                                hex(0x11aef) : 'default = 0xa',
                                hex(0x11af4) : 'default = 0x10',
                                hex(0x11af9) : 'default = 0xa',
                                hex(0x11afe) : 'default = 0x10',
                                hex(0x11b03) : 'default = 0xa',
                                hex(0x11b08) : 'default = 0xf',
                                hex(0x11b0d) : 'default = 0x11',
                                hex(0x11b12) : 'default = 0x11',
                                hex(0x11b17) : 'default = 0x9',
                                hex(0x11b1c) : 'default = 0x9',
                                hex(0x11b21) : 'default = 0xc',
                                hex(0x11b26) : 'default = 0xc',
                                hex(0x11b2b) : 'default = 0xb',
                                hex(0x11b30) : 'default = 0xb',
                                hex(0x11b35) : 'default = 0x11',
                                hex(0x11b3a) : 'default = 0x1',
                                hex(0x11b3f) : 'default = 0xb',
                                hex(0x11b44) : 'default = 0x1',
                                hex(0x11b49) : 'default = 0x1',
                            # Planet 8:
                                hex(0x11ce8) : 'default = 0x15',
                                hex(0x11ced) : 'default = 0x1b',
                                hex(0x11cf2) : 'default = 0x12',
                                hex(0x11cf7) : 'default = 0x10',
                                hex(0x11cfc) : 'default = 0x10',
                                hex(0x11d01) : 'default = 0xa',
                                hex(0x11d06) : 'default = 0xf',
                                hex(0x11d0b) : 'default = 0xa',
                                hex(0x11d10) : 'default = 0xa',
                                hex(0x11d15) : 'default = 0xa',
                                hex(0x11d1a) : 'default = 0x10',
                                hex(0x11d1f) : 'default = 0xc',
                                hex(0x11d24) : 'default = 0x9',
                                hex(0x11d29) : 'default = 0xc',
                                hex(0x11d2e) : 'default = 0xc',
                                hex(0x11d33) : 'default = 0x11',
                                hex(0x11d38) : 'default = 0x11',
                                hex(0x11d3d) : 'default = 0xb',
                                hex(0x11d42) : 'default = 0x11',
                                hex(0x11d47) : 'default = 0xb',
                                hex(0x11d4c) : 'default = 0xb',
                                hex(0x11d51) : 'default = 0x1',
                                hex(0x11d56) : 'default = 0x1',
                            # Planet 9:
                                hex(0x11eb9) : 'default = 0x15',
                                hex(0x11ebe) : 'default = 0x12',
                                hex(0x11ec3) : 'default = 0x1b',
                                hex(0x11ec8) : 'default = 0xa',
                                hex(0x11ecd) : 'default = 0x10',
                                hex(0x11ed2) : 'default = 0xa',
                                hex(0x11ed7) : 'default = 0x10',
                                hex(0x11edc) : 'default = 0xa',
                                hex(0x11ee1) : 'default = 0x10',
                                hex(0x11ee6) : 'default = 0xa',
                                hex(0x11eeb) : 'default = 0xa',
                                hex(0x11ef0) : 'default = 0xf',
                                hex(0x11ef5) : 'default = 0x9',
                                hex(0x11efa) : 'default = 0x9',
                                hex(0x11eff) : 'default = 0xc',
                                hex(0x11f04) : 'default = 0x9',
                                hex(0x11f09) : 'default = 0x11',
                                hex(0x11f0e) : 'default = 0xb',
                                hex(0x11f13) : 'default = 0xb',
                                hex(0x11f18) : 'default = 0x11',
                                hex(0x11f1d) : 'default = 0x11',
                                hex(0x11f22) : 'default = 0xb',
                                hex(0x11f27) : 'default = 0x1',
                            # Planet 10:
                                hex(0x11d5b) : 'default = 0x15',
                                hex(0x11d60) : 'default = 0x12',
                                hex(0x11d65) : 'default = 0x10',
                                hex(0x11d6a) : 'default = 0xf',
                                hex(0x11d6f) : 'default = 0xa',
                                hex(0x11d74) : 'default = 0xa',
                                hex(0x11d79) : 'default = 0x10',
                                hex(0x11d7e) : 'default = 0xa',
                                hex(0x11d83) : 'default = 0xa',
                                hex(0x11d88) : 'default = 0x10',
                                hex(0x11d8d) : 'default = 0xa',
                                hex(0x11d92) : 'default = 0x10',
                                hex(0x11d97) : 'default = 0x9',
                                hex(0x11d9c) : 'default = 0x9',
                                hex(0x11da1) : 'default = 0xc',
                                hex(0x11da6) : 'default = 0x9',
                                hex(0x11dab) : 'default = 0x1',
                                hex(0x11db0) : 'default = 0x11',
                                hex(0x11db5) : 'default = 0xb',
                                hex(0x11dba) : 'default = 0x1',
                                hex(0x11dbf) : 'default = 0x11',                            
                            # Planet 11:
                                hex(0x11f2c) : 'default = 0x15',
                                hex(0x11f31) : 'default = 0x12',
                                hex(0x11f36) : 'default = 0x10',
                                hex(0x11f3b) : 'default = 0x10',
                                hex(0x11f40) : 'default = 0xa',
                                hex(0x11f45) : 'default = 0xa',
                                hex(0x11f4a) : 'default = 0xf',
                                hex(0x11f4f) : 'default = 0x10',
                                hex(0x11f54) : 'default = 0xa',
                                hex(0x11f59) : 'default = 0x10',
                                hex(0x11f5e) : 'default = 0xa',
                                hex(0x11f63) : 'default = 0x10',
                                hex(0x11f68) : 'default = 0x9',
                                hex(0x11f6d) : 'default = 0x9',
                                hex(0x11f72) : 'default = 0xc',
                                hex(0x11f77) : 'default = 0x9',
                                hex(0x11f7c) : 'default = 0xc',
                                hex(0x11f81) : 'default = 0x11',
                                hex(0x11f86) : 'default = 0xb',
                                hex(0x11f8b) : 'default = 0x11',
                                hex(0x11f90) : 'default = 0x11',
                                hex(0x11f95) : 'default = 0xb',
                                hex(0x11f9a) : 'default = 0xb',
                                hex(0x11f9f) : 'default = 0x1',
                            # Planet 12:
                                hex(0x11b4e) : 'default = 0x15',
                                hex(0x11b53) : 'default = 0x12',
                                hex(0x11b58) : 'default = 0x10',
                                hex(0x11b5d) : 'default = 0x10',
                                hex(0x11b62) : 'default = 0xa',
                                hex(0x11b67) : 'default = 0x10',
                                hex(0x11b6c) : 'default = 0x10',
                                hex(0x11b71) : 'default = 0xa',
                                hex(0x11b76) : 'default = 0xf',
                                hex(0x11b7b) : 'default = 0xa',
                                hex(0x11b80) : 'default = 0xa',
                                hex(0x11b85) : 'default = 0x10',
                                hex(0x11b8a) : 'default = 0x9',
                                hex(0x11b8f) : 'default = 0x9',
                                hex(0x11b94) : 'default = 0xc',
                                hex(0x11b99) : 'default = 0x9',
                                hex(0x11b9e) : 'default = 0x9',
                                hex(0x11ba3) : 'default = 0x11',
                                hex(0x11ba8) : 'default = 0x11',
                                hex(0x11bad) : 'default = 0xb',
                                hex(0x11bb2) : 'default = 0x11',
                                hex(0x11bb7) : 'default = 0x11',
                                hex(0x11bbc) : 'default = 0xb',
                                hex(0x11bc1) : 'default = 0x1',
                                hex(0x11bc6) : 'default = 0x1',
                            # Planet 13:
                                hex(0x11bcb) : 'default = 0x15', # mother ship
                                hex(0x11bd0) : 'default = 0x12',  # Warp
                                hex(0x11bd5) : 'default = 0x10',
                                hex(0x11bda) : 'default = 0xa',
                                hex(0x11bdf) : 'default = 0xf',
                                hex(0x11be4) : 'default = 0x10',
                                hex(0x11be9) : 'default = 0xa',
                                hex(0x11bee) : 'default = 0xa',
                                hex(0x11bf3) : 'default = 0x10',
                                hex(0x11bf8) : 'default = 0xa',
                                hex(0x11bfd) : 'default = 0x9',
                                hex(0x11c02) : 'default = 0x9',
                                hex(0x11c07) : 'default = 0xc',
                                hex(0x11c0c) : 'default = 0xc',
                                hex(0x11c11) : 'default = 0xb',
                                hex(0x11c16) : 'default = 0x11',
                                hex(0x11c1b) : 'default = 0x11',
                                hex(0x11c20) : 'default = 0x11',
                                hex(0x11c25) : 'default = 0x1',
                                hex(0x11c2a) : 'default = 0x1'
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

