import argparse
from randomizer import *

def getoptions():
    parser = argparse.ArgumentParser(description='Solar Jet Randomizer, Version 1.03, written by Niamek', epilog="If you want more details about the flags or modes, the README details everything.")
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
                        dest="seed", default=random.random(), metavar="", type=int)
    parser.add_argument("--mode", choices=["normal", "reckless"],
                        default="normal", dest="mode", help="Game mode")

    return parser.parse_args()


if __name__ == "__main__":
    options = getoptions()
    flags = ""
    mode = "normal"
    with open("Vanilla.nes", "rb") as original:
        originaldata = original.read()
        randogame = Rando(originaldata)
        randogame.seed = str(options.seed)[2:] if options.seed < 1 else options.seed

        randogame.disable_max4()
        if options.Rpalette:
            randogame.palette_randomizer()
        if options.Rastro:
            randogame.astro_randomizer()
            flags += "a"
        #if options.Rgrav:
            #gravity_randomizer(randogame,seed)
        if options.Rrocket:
            randogame.rocket_randomizer()
            flags += "r"
        #if options.Rfuel:
            #fuel_randomizer(randogame,seed)
        #if options.Rweapon:
            #weapon_randomizer(randogame,seed)
        if options.mode:
            if options.mode == "reckless":
                randogame.mode_reckless()
                mode = "reckless"

            #elif options.mode == "improved":
                # self.mode_improved()
                # mode = "improved"

            elif options.mode == "goldhunt":
                randogame.mode_goldhunt()
                mode = "goldhunt"
        with open(f"Solar Jetman_{flags}_{mode}_{randogame.seed}.nes", "wb") as newrom:
            newrom.write(randogame.data)
