from gameclass import ROM, infos

def remove_uselesscodes(game):
    game.setmulti(0x0048D4, 0x0048D6, 0xEA)  # For the pod
    game.setmulti(0x4490,0x4492, 0xEA)  # For the astronaut
    game.setmulti(0x4c47,0x004c6a,0xEA)  # Ceci semble fonctionner

    # This is the new "vanilla max speed"
    game[0x3a25] = 3
    game[0x3a2E] = game[0x3a25]  # X speed
    game[0x3a8f] = 3  # up maxspeed Y up
    game[0x3a98] = game[0x3a8f]




def disable_ohko(game):
    game[0x008403] = 234
    game[0x008404] = 234
    game[0x008405] = 234
    game[0x008406] = 234

def disable_fuelloss_collisions(game):
    game[0x11030] = 234
    game[0x11031] = 234
    game[0x11036] = 234
    game[0x11037] = 234

def disable_shield_fuelusage(game):
    game[0x0049f0] = 0
    game[0x0049f1] = 0

def disable_fuelusage(game):
    game[0x386B7] = 0  # Normal
    game[0x386AF] = 0

def disable_springeffect(game):
    game[0x48A1] = 0xEA
    game[0x48A2] = 0xEA
    game[0x48A3] = 0xEA
    game[0x48A4] = 0xEA
    game[0x48A5] = 0xEA
    game[0x48A6] = 0xEA
    game[0x48A7] = 0xEA
    game[0x48A8] = 0xEA
    game[0x48A9] = 0xEA

