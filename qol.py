from gameclass import ROM, infos

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