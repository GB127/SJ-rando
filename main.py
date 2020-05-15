import argparse
from rando import *


def getoptions():
    parser = argparse.ArgumentParser(description='Solar Jet Randomizer : Randomizers selected')
    parser.add_argument('-p', "--palette", action="store_true",
                    help='Randomize the colors', dest="PaletteRando")
    parser.add_argument('-e', "--engine", action="store_true",
                    help='Randomize the engine', dest="EngineRando")
    parser.add_argument('-m', "--management", action="store_true",
                    help='Randomize the management', dest="ManagementRando")
    return parser.parse_args()


if __name__ == "__main__":
    options = getoptions()
    with open("Vanilla.nes", "rb") as original:
        originaldata = original.read()
        randogame = ROM(originaldata)
        if options.PaletteRando == True:
            paletterandomizer(randogame)
        if options.EngineRando == True:
            engine_randomizer(randogame)
        if options.ManagementRando == True:
            manage_randomizer(randogame)
        with open("testing.nes", "wb") as newrom:
            newrom.write(randogame.data)


