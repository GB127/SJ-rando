import argparse
from randomizer import *

def getoptions():
    parser = argparse.ArgumentParser(description='Solar Jet Randomizer, Version 2, written by Niamek', epilog="If you want more details about the flags or modes, the README details everything.")
    parser.add_argument("-a", "--astro", action="store_true",
                        help="Randomize the Astronaut's properties", dest="Rastro")
    #parser.add_argument("-g", "--gravity", action="store_true",
                        #help="Randomize the gravity", dest="Rgrav"),
    parser.add_argument("-i", "--items", action="store_true",
                        help="Randomize the items with no logic", dest="Ritems_no")
    parser.add_argument("-I", "--Items", action="store_true",
                        help="Randomize the items with logic", dest="Ritems")
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
    parser.add_argument("--mode", choices=["normal", "reckless", "goldhunt"],
                        default="normal", dest="mode", help="Game mode")

    return parser.parse_args()


if __name__ == "__main__":
    options = getoptions()

    if options.Ritems_no and options.Ritems:
        raise BaseException("Item randomizer can't do both logic & no logic (flags i & I)")

    with open("Vanilla.nes", "rb") as original:
        randogame = Rando(original.read())
        randogame.seed = str(options.seed)[2:] if options.seed < 1 else options.seed

        if options.Rpalette:
            randogame.palette_randomizer()
        if options.Rastro:
            randogame.astro_randomizer()
        if options.Rrocket:
            randogame.rocket_randomizer()
        if options.Ritems_no:
            randogame.items_randomizer(logic=False)
        if options.Ritems:
            randogame.items_randomizer(logic=True)

#############################MODES######################################
        if options.mode == "reckless":
            randogame.mode_reckless()
        elif options.mode == "goldhunt":
            randogame.mode_goldhunt()
#########END of the randomizer program : Write the new file############
        with open(f"Solar Jetman_{randogame.flags}_{randogame.mode}_{randogame.seed}.nes", "wb") as newrom:
            newrom.write(randogame.data)
