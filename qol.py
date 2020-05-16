from gameclass import ROM, infos

def removeohko():
    game[0x008403] = 234
    game[0x008404] = 234
    game[0x008405] = 234
    game[0x008406] = 234