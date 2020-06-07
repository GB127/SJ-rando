life = 0x1
crash = 0x2
shield = 0x3
booster = 0x4
points = 0x5
map = 0x6
points2 = 0x9
fuel = 0xA
fueltank = 0xB
radio = 0xC
crystal = 0xF
crystal2 = 0x10
warp = 0x11
minigame = 0x1B
gwarp = 0x12
goldenship = 0x13
lvl2warp = 0x1A


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

    "3" : [gwarp,       fuel,       crystal,    fuel,       fuel,
           crystal2,    fuel,       points,     points2,    radio,
           points2,     warp,       fueltank,   warp,       life,
           life],

    "4" : [gwarp,       fuel,       crystal2,   fuel,       fuel,
           crystal,     points2,    radio,      points,     points,
           fueltank,    fueltank,   points2,    fueltank,   warp,
           warp,        warp,       life,       life,       life],

    "5" : [gwarp,       minigame,   crystal2,   fuel,       crystal,
           fuel,        fuel,       fuel,       points2,    points2,
           radio,       radio,      fueltank,   warp,       warp, 
           fueltank,    fueltank,   life,       life],

    "6" : [gwarp,       crystal,    crystal2,   fuel,       crystal2,
           crystal2,    fuel,       fuel,       crystal2,   fuel,
           points2,     points2,    radio,      radio,      radio,
           radio,       fueltank,   warp,       warp,       warp,
           warp,        life,       life,       life],

    "7" : [gwarp,       crystal2,   crystal2,   fuel,       crystal2,
           fuel,        crystal2,   fuel,       crystal2,   fuel,
           crystal,     warp,       warp,       points2,    points2,
           radio,       radio,      fueltank,   fueltank,   warp,
           life,        fueltank,   life,       life],

    "8" : [minigame,    gwarp,      crystal2,   crystal2,   fuel,
           crystal,     fuel,       fuel,       fuel,       crystal2,
           radio,       points2,    radio,      radio,      warp,
           warp,        fueltank,   warp,       fueltank,   fueltank,
           life,        life],

    "9" : [gwarp,       minigame,   fuel,       crystal2,   fuel,
           crystal2,    fuel,       crystal2,   fuel,       fuel,
           crystal,     points2,    points2,    radio,      points2,
           warp,        fueltank,   fueltank,   warp,       warp,
           fueltank,    life],

    "10": [gwarp,       crystal2,   crystal,    fuel,       fuel,
           crystal2,    fuel,       fuel,       crystal2,   fuel,
           crystal2,    points2,    points2,    radio,      points2,
           life,        warp,       fueltank,   life,       warp],

    "11": [gwarp,       crystal2,   crystal2,   fuel,       fuel,
           crystal,     crystal2,   fuel,       crystal2,   fuel,
           crystal2,    points2,    points2,    radio,      points2,
           radio,       warp,       fueltank,   warp,       warp,
           fueltank,    fueltank,   life],

    "12": [gwarp,       crystal2,   crystal2,   fuel,       crystal2,
           crystal2,    fuel,       crystal,    fuel,       fuel,
           crystal2,    points2,    points2,    radio,      points2,
           points2,     warp,       warp,       fueltank,   warp,
           warp,        fueltank,   life,       life],

    "13": [gwarp,       crystal2,   fuel,       crystal,    crystal2,
           fuel,        fuel,       crystal2,   fuel,       points2,
           points2,     radio,      radio,      fueltank,   warp,
           warp,        warp,       life,       life]
}

"""
# Planet items randomizer / Subplanet items randomizer
    # With a logic
    # Without a logic
# Planet items + "Subplanet" items randomizer
# ALL items randomizer (Golden warpship still isolated)

modes idea:
    goldmining : No fuel to gather, only the goldparts.
    no goldship : No goldenship to gather, only the fuels
"""