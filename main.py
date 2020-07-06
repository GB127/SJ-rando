import argparse
from rando import *
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
    seed = str(options.seed)[2:] if options.seed < 1 else options.seed
    flags = ""
    mode = "normal"
    with open("Vanilla.nes", "rb") as original:
        originaldata = original.read()
        randogame = Rando(originaldata)
        randogame.disable_max4()
        if options.Rpalette:
            randogame.palette_randomizer(seed)
        if options.Rastro:
            randogame.astro_randomizer(seed)
            flags += "a"
        #if options.Rgrav:
            #gravity_randomizer(randogame,seed)
        if options.Rrocket:
            randogame.rocket_randomizer(seed)
            flags += "r"
        #if options.Rfuel:
            #fuel_randomizer(randogame,seed)
        #if options.Rweapon:
            #weapon_randomizer(randogame,seed)
        if options.mode:
            if options.mode == "reckless":
                randogame.disable_fuelloss_collisions()
                randogame.disable_ohko()
                mode = "reckless"

            #elif options.mode == "improved":
            #    disable_springeffect(randogame)
            #    mode = "improved"

            # What I want to add:
                # fixed damage instead of OHKO from enemies bullet
                # Easier to transport golden warship
                # No planet 13 labyrinth
                # last level no ohko walls please
            elif options.mode == "goldhunt":
                randogame.mode_goldhunt()
                mode = "goldhunt"
        with open(f"Solar Jetman_{flags}_{mode}_{seed}.nes", "wb") as newrom:
            newrom.write(randogame.data)
