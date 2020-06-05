# Solar Jetman Randomizer
    This is a randomizer for the NES game "Solar Jetman : Hunt for the Golden Warship.

    Current version : Beta version
    Wrote by Niamek.

# Getting started:
    You need to download Python 3.8.
        https://realpython.com/installing-python/
    Drag the gamefile named Vanilla.nes in the same folder
        Note : You can rename your file without any issue.
    Open the command line on the same folder.
        For windows : https://www.thewindowsclub.com/how-to-open-command-prompt-from-right-click-menu/
    type the command : python main.py -h
        then press return/ENTER on the keyboard.
    type the command with the settings you want to use
        EXAMPLE : python main.py -arp --seed 450 --mode reckless

# Features :
    -> Palette randomizer
        -- Rocket's palettes
        -- Bars
        -- Score
        -- Title screen (Dots and astronaut's fire)
    -> Rocket's randomizer :
        -- Rocket's max speed
        -- Rocket's acceleration
    -> Astronaut randomizer :
        -- Astronaut's max speed
        -- Astronaut's acceleration


# Future features :
    -> Better handling of filenames
    -> Gravity randomizer
        WIP
    -> Weapon randomizer
    -> Item randomizer
        WIP
    -> And much more!


# Detailled descriptions of the randomizers:
    -> Astro randomizer: X maxspeed, Y up maxspeed, jetpack acceleration, X acceleration
        -> X max speed is randomized with a value of the following range: [3,4,5,6,7,8,9,10]
            - Vanilla value is 7, but actual vanilla is a little bit over 3
        -> Y max speed is randomized to a value of the following range: [3,4,5,6,7,8]
            - Vanilla value is 3

        -> X acceleration is randomized: Note that there are two pieces : the friction that always reduce the speed of the astronaut and the acceleration.
            - the friction is randomized. It can be any value from 0 to 243.
            - The acceleration is randomized. It is always at least 12 over the friction, with a maximum of 255.
        -> Y acceleration is randomized : currently only the jetpack power is randomized.
            - Jetpack's power is randomized from 32 to 255.
             
    -> Palette randomizer: colors
        I made a somewhat algorithm to make sure the rocket's colors make sense.
    -> Rocket randomizer: X&Y maxspeed, acceleration
        -- The X&Y max speed is randomized jointly : it can be any from the following value: [3,4,5,6,7,8]
            -> Vanilla value is 3.
            -> This has a side effect of altering astronaut's max fallspeed as they share the same Y maxspeed.
        -- The acceleration is randomized:
            - The acceleration for X and Y speed depends on the rocket's direction. This dependency is randomized. It can be either : [vanilla, linearized, reversed]
            - The max value of acceleration is randomized. it can be anything in the following range : [64,255]
                -> 64 is vanilla.
            - All the others acceleration of the distribution are adjusted with the same ratio of vanilla max accel vs. randomized max accel.

# ACKNOLEDGEMENTS:
    steve_hacks : For answering my multiples questions and being patient.
    MeleeWizard : For suggesting this game and helping in the testings
    sbm : For helping in understanding upcodes
    TheMotherBrains86 : For speedrunning this game and showing interest in the randomizer. And running this for the Randomania superweek.
    Randomania discord channel for being a useful place to learn about randomizers.
    Randomizers communities : This randomizer is inspired by their "ideas" of other randomizers.