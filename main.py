import argparse
from rando import *
from qol import *

def getoptions():
    parser = argparse.ArgumentParser(description='Solar Jet Randomizer : Randomizers selected')
    parser.add_argument("-a", "--astro", action="store_true",
                        help="Randomize the Astronaut's properties", dest="Rastro")
    #parser.add_argument("-g", "--gravity", action="store_true",
                        #help="Randomize the gravity", dest="Rgrav"),
    parser.add_argument('-p', "--palette", action="store_true",
                        help='Randomize the colors', dest="Rpalette")
    parser.add_argument("-r", "--rocket", action="store_true",
                        help="Randomize the pod's properties", dest="Rrocket")
    #parser.add_argument("-f","--fuel", action="store_true",
    #                    help="Randomize things related to the fuel", dest="Rfuel")
    #parser.add_argument("-w", "--weapon", action="store_true",
    #                    help="Randomize the weapons' properties", dest="Rweapon")
    parser.add_argument("--seed", action="store", help="Seed for the randomization",
                        dest="seed", default=str(random.random()), metavar="")
    parser.add_argument("--mode", choices=[None, "reckless", "improved"],
                        default=None, dest="mode", help="Game mode")

    return parser.parse_args()


if __name__ == "__main__":
    options = getoptions()
    seed = options.seed[2:]
    with open("Vanilla.nes", "rb") as original:
        originaldata = original.read()
        randogame = ROM(originaldata)
        remove_uselesscodes(randogame)
        if options.Rpalette:
            palette_randomizer(randogame, seed)
        if options.Rastro:
            astro_randomizer(randogame,seed)
        #if options.Rgrav:
            #gravity_randomizer(randogame,seed)
        if options.Rrocket:
            rocket_randomizer(randogame,seed)
        #if options.Rfuel:
            #fuel_randomizer(randogame,seed)
        #if options.Rweapon:
            #weapon_randomizer(randogame,seed)
        if options.mode:
            if options.mode == "reckless":
                disable_fuelloss_collisions(randogame)
                disable_ohko(randogame)
            elif options.mode == "improved":
                disable_springeffect(randogame)
        with open("testing.nes", "wb") as newrom:
            newrom.write(randogame.data)
