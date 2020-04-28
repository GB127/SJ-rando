from io import BytesIO

# with the bytesIO
with open("ROM.nes", "rb") as ROM:
    game = BytesIO(ROM.read())
    game.seek(0x75D0,0)
    test2 = game.read(10)
    print([hex(i) for i in test2])
    game.seek(0x75D6,0)
    game.write(bytes([255]))
    game.seek(0x75D0,0)
    test2 = game.read(10)
    print([hex(i) for i in test2])

print("-----------Seperator---------------")
# with the bytesarray:
with open("ROM.nes", "rb") as ROM:
    game = bytearray(ROM.read())
    print([hex(i) for i in game[0x75D0:0x75DA]])
    game[0x75D6] = 255
    print([hex(i) for i in game[0x75D0:0x75DA]])
    with open("ROM2.nes", "wb") as newgame:
        newgame.write(game)