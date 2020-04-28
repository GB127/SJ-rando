from io import BytesIO
from gameclass import ROM, infos
infos = infos()

# with the bytesarray:
with open("ROM.nes", "rb") as original:
    originaldata = original.read()
    game = ROM(originaldata)
    print([hex(i) for i in game[0x75D0:0x75DA]])
    game[0x75D6] = 255
    print([hex(i) for i in game[0x75D0:0x75DA]])


infos.listadresses("palettes")
infos.pcheck(0x75D8)