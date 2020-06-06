life = 0x1
crash = 0x2
shield = 0x3
booster = 0x4
warp = 0x11
fuel = 0xA
fueltank = 0xB
map = 0x6
radio = 0xC
crystal = 0xF
crystal2 = 0x10
minigame = 0x1B
goldenship = 0x13
gwarp = 0x12
lvl2warp = 0x1A
points = 0x5
points2 = 0x9

# 7 : Garbled sprite?
# 8 : Garbled
# 18 : Fuel (I'm sure there is a range for this)

planetitems ={
    "1" : [minigame,    shield,     crystal2,   fuel,       gwarp],

    "2" : [lvl2warp,    gwarp,      booster,    map,        fuel,
           crystal,     fuel,       points2,    crystal,    fuel,
           radio,       points2,    fuel,       warp,       points2,
           fueltank,    warp,       warp,       life,       life,
           life],

    "4" : [gwarp,       fuel,       crystal2,   fuel,       fuel,
           crystal,     points2,    radio,      points,     points,
           fueltank,    fueltank,   points2,    fueltank,   warp,
           warp,        warp,       life,       life,       life],
    "3" : [gwarp,       fuel,       crystal,    fuel,       fuel,
           crystal2,    fuel,       points,     points2,    radio,
           points2,     warp,       fueltank,   warp,       life,
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
