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

def shift_gravity(game,action=True):
    if action:
        disable_springeffect(game)
        game[0x388A6] = 0x36
        game[0x388BE] = 0x86
        game[0x388BF] = 0xB8  
        game[0x388AD] = 0xA1
        game[0x388AE] = 0xB8
        game[0x388b2] = 0x36
        game[0x388B7] = 0x36
    else:
        pass
