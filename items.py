import random

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
planetad = {
    "1":[0x11a4a,0x11a4f,0x11a54,0x11a59,0x11a5e,0x11a63],
    "2":[0x11e41,0x11e46,0x11e4b,0x11e50,0x11e55,0x11e5a,0x11e5f,0x11e64,0x11e69,0x11e6e,0x11e73,0x11e78,0x11e7d,0x11e82,0x11e87,0x11e8c,0x11e91,0x11e96,0x11e9b,0x11ea0,0x11ea5,0x11eaa,0x11eaf,0x11eb4],
    "3":[0x11c93,0x11c98,0x11c9d,0x11ca2,0x11ca7,0x11cac,0x11cb1,0x11cb6,0x11cbb,0x11cc0,0x11cc5,0x11cca,0x11ccf,0x11cd4,0x11cd9,0x11cde,0x11ce3],
    "4":[0x11a68,0x11a6d,0x11a72,0x11a77,0x11a7c,0x11a81,0x11a86,0x11a8b,0x11a90,0x11a95,0x11a9a,0x11a9f,0x11aa4,0x11aa9,0x11aae,0x11ab3,0x11ab8,0x11abd,0x11ac2,0x11ac7,0x11acc],
    "5":[],
    "6":[],
    "7":[],
    "8":[],
    "9":[],
    "10":[],
    "11":[],
    "12":[],
    "13":[]}

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

def item_randomizer_nologic(game,seed):
    random.seed(seed)
    planets = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
    for i in planets:
        planetad[i] = random.shuffle(planetitems[i])


"""
# Planet items randomizer / Subplanet items randomizer
    # With a logic
    # Without a logic
# Planet items + "Subplanet" items randomizer
# ALL items randomizer (Golden warpship still isolated in the subplanets)

modes idea:
    goldhunt : No fuel to gather needed to gather, only the goldparts.
    refuel : No goldenship to gather, only the fuels
        the fuels can't be on subplanet.

Approach:
    Check if I flag is on
        Check if mode goldhunt is on:
            if yes, shuffle accordingly
        Check if logic
            shuffle accordingly
"""