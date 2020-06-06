life = 0x1
crash = 0x2
shield = 0x3
booster = 0x4
warp = 0x11
fuel = 0xA
fueltank = 0xB
map = 0x6
radio = 0xC
crystal1 = 0xF
crystal2 = 0x10
minigame = 0x1B
goldenship = 0x13
goldenwarp = 0x12
lvl2warp = 0x1A
points = 0x5
points2 = 0x9

# 7 : Garbled sprite?
# 8 : Garbled
# 18 : Fuel (I'm sure there is a range for this)

planetitems ={
    "1" : [minigame, shield, crystal2, fuel  ,goldenwarp],
    "2" : [lvl2warp, goldenwarp, booster, 0x06, fuel,
           0xF , fuel , 0x09, 0xF , fuel ,
           0xC , 0x9 , fuel , warp, 0x9 ,
           0xB , warp, warp, life , life ,
           life ],
    "4" : [goldenwarp, fuel , 0x10, fuel , fuel ,
           0xF , 0x9 , 0xC , 0x5 , 0x5 ,
           0xB , 0xB , 0x9 , 0xB , warp,
           warp, warp, life , life , life],
    "3" : [goldenwarp, fuel , 0xF , fuel , fuel ,
           crystal2, fuel , 0x5 , 0x9 , 0xC ,
           0x9 , warp, 0xB , warp, life ,
           life],
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
