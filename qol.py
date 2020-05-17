from gameclass import ROM, infos

def removeohko():
    game[0x008403] = 234
    game[0x008404] = 234
    game[0x008405] = 234
    game[0x008406] = 234

def invicible_collisions():
    game[0x11030] = 234
    game[0x11031] = 234
    game[0x11036] = 234
    game[0x11037] = 234
