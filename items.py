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
def items_offsets_all():
    liste = []
    for key in planetad.keys():
        liste += (planetad[key])
    return liste

def items_values_all():
    liste = []
    for key in planetitems.keys():
        liste += (planetitems[key])
    return liste



planetad = {
    "1":[0x11a4f,   0x11a54,    0x11a59,    0x11a5e,    0x11a63],

    "2":[0x11e46,   0x11e4b,    0x11e50,    0x11e55,    0x11e5a,
         0x11e5f,   0x11e64,    0x11e69,    0x11e6e,    0x11e73,
         0x11e78,   0x11e7d,    0x11e82,    0x11e87,    0x11e8c,
         0x11e91,   0x11e96,    0x11e9b,    0x11eaa,    0x11eaf,
         0x11eb4],

    "3":[0x11c98,   0x11c9d,    0x11ca2,    0x11ca7,    0x11cac,
         0x11cb1,   0x11cb6,    0x11cbb,    0x11cc0,    0x11cc5,
         0x11cca,   0x11ccf,    0x11cd4,    0x11cd9,    0x11cde,
         0x11ce3],

    "4":[0x11a6d,   0x11a72,    0x11a77,    0x11a7c,    0x11a81,
         0x11a86,   0x11a8b,    0x11a90,    0x11a95,    0x11a9a,
         0x11a9f,   0x11aa4,    0x11aa9,    0x11aae,    0x11ab3,
         0x11ab8,   0x11abd,    0x11ac2,    0x11ac7,    0x11acc],

    "5":[0x11c34,   0x11c39,    0x11c3e,    0x11c43,    0x11c48,
         0x11c4d,   0x11c52,    0x11c57,    0x11c5c,    0x11c61,
         0x11c66,   0x11c6b,    0x11c70,    0x11c75,    0x11c7a,
         0x11c7f,   0x11c84,    0x11c89,    0x11c8e],

    "6":[0x11dc9,   0x11dce,    0x11dd3,    0x11dd8,    0x11ddd,
         0x11de2,   0x11de7,    0x11dec,    0x11df1,    0x11df6,
         0x11dfb,   0x11e00,    0x11e05,    0x11e0a,    0x11e0f,
         0x11e14,   0x11e19,    0x11e1e,    0x11e23,    0x11e28,
         0x11e2d,   0x11e32,    0x11e37,    0x11e3c],

    "7":[0x11ad6,   0x11adb,    0x11ae0,    0x11ae5,    0x11aea,
         0x11aef,   0x11af4,    0x11af9,    0x11afe,    0x11b03,
         0x11b08,   0x11b0d,    0x11b12,    0x11b17,    0x11b1c,
         0x11b21,   0x11b26,    0x11b2b,    0x11b30,    0x11b35,
         0x11b3a,   0x11b3f,    0x11b44,    0x11b49],

    "8":[0x11ced,   0x11cf2,    0x11cf7,    0x11cfc,    0x11d01,
         0x11d06,   0x11d0b,    0x11d10,    0x11d15,    0x11d1a,
         0x11d1f,   0x11d24,    0x11d29,    0x11d2e,    0x11d33,
         0x11d38,   0x11d3d,    0x11d42,    0x11d47,    0x11d4c,
         0x11d51,   0x11d56],

    "9":[0x11ebe,   0x11ec3,    0x11ec8,    0x11ecd,    0x11ed2,
         0x11ed7,   0x11edc,    0x11ee1,    0x11ee6,    0x11eeb,
         0x11ef0,   0x11ef5,    0x11efa,    0x11eff,    0x11f04,
         0x11f09,   0x11f0e,    0x11f13,    0x11f18,    0x11f1d,
         0x11f22,   0x11f27],

    "10":[0x11d60,  0x11d65,    0x11d6a,    0x11d6f,    0x11d74,
          0x11d79,  0x11d7e,    0x11d83,    0x11d88,    0x11d8d,
          0x11d92,  0x11d97,    0x11d9c,    0x11da1,    0x11da6,
          0x11dab,  0x11db0,    0x11db5,    0x11dba,    0x11dbf],

    "11":[0x11f31,  0x11f36,    0x11f3b,    0x11f40,    0x11f45,
          0x11f4a,  0x11f4f,    0x11f54,    0x11f59,    0x11f5e,
          0x11f63,  0x11f68,    0x11f6d,    0x11f72,    0x11f77,
          0x11f7c,  0x11f81,    0x11f86,    0x11f8b,    0x11f90,
          0x11f95,  0x11f9a,    0x11f9f],

    "12":[0x11b53,  0x11b58,    0x11b5d,    0x11b62,    0x11b67,
          0x11b6c,  0x11b71,    0x11b76,    0x11b7b,    0x11b80,
          0x11b85,  0x11b8a,    0x11b8f,    0x11b94,    0x11b99,
          0x11b9e,  0x11ba3,    0x11ba8,    0x11bad,    0x11bb2,
          0x11bb7,  0x11bbc,    0x11bc1,    0x11bc6],

    "13":[0x11bd0,  0x11bd5,    0x11bda,    0x11bdf,    0x11be4,
          0x11be9,  0x11bee,    0x11bf3,    0x11bf8,    0x11bfd,
          0x11c02,  0x11c07,    0x11c0c,    0x11c11,    0x11c16,
          0x11c1b,  0x11c20,    0x11c25,    0x11c2a]}

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
           warp,        warp,       life,       life]}
