import argparse
from rando import *


def getoptions():
    parser = argparse.ArgumentParser(description='Solar Jet Randomizer : Randomizers selected')
    parser.add_argument("--seed", action="store", help="Seed for the randomization",
                        dest="seed", default="0", metavar="")
    parser.add_argument('-p', "--palette", action="store_true",
                    help='Randomize the colors', dest="Rpalette")
    parser.add_argument("-a", "--astro", action="store_true", 
                        help="Randomize the Astronaut's properties", dest="Rastro")
    parser.add_argument("-g", "--gravity", action="store_true",
                        help="Randomize the gravity", dest="Rgrav"),
    parser.add_argument("-r", "--rocket", action="store_true",
                        help="Randomize the pod's properties", dest="Rrocket")
    parser.add_argument("-f","--fuel", action="store_true",
                        help="Randomize things related to the fuel", dest="Rfuel")
    parser.add_argument("-w", "--weapon", action="store_true",
                        help="Randomize the weapons' properties", dest="Rweapon")
    return parser.parse_args()


if __name__ == "__main__":
    options = getoptions()
    seed = options.seed
    print(seed, type(seed))
    with open("Vanilla.nes", "rb") as original:
        originaldata = original.read()
        randogame = ROM(originaldata)
        if options.Rpalette:
            paletterandomizer(randogame, seed)
        if options.Rastro:
            astro_randomizer(randogame,seed)
        if options.Rgrav:
            gravity_randomizer(randogame,seed)
        if options.Rrocket:
            rocket_randomizer(randogame,seed)
        if options.Rfuel:
            fuel_randomizer(randogame,seed)
        if options.Rweapon:
            weapon_randomizer(randogame,seed)
        with open("testing.nes", "wb") as newrom:
            newrom.write(randogame.data)


