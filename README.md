# Solar Jetman Randomizer
    This is a randomizer for the NES game "Solar Jetman : Hunt for the Golden Warship."

    Current version : Version 1.0
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
        This will display what the randomizer supports.
        You can skip this step.
    type the command with the settings you want to use
        EXAMPLE : python main.py -arp --seed 450 --mode reckless

# Features :
    -> Palette randomizer
    -> Rocket's randomizer
    -> Astronaut randomizer
    -> Some modes: normal, reckless

# Future features :
    -> Better handling of filenames
    -> Gravity randomizer
    -> Weapon randomizer
    -> Item randomizer
    -> And much more!

# ROM modifications :
    To open up some randomization, I have removed some instructions in the code. As a side effect, alongside with some other randomizations, the last level is altered. To compromise, the new "vanilla" maxspeed for the last level and the astronaut's are now 3. And the acceleration for the last level is now XX and YY for X and Y respectively. I've done this to allow astronaut maxspeed randomization. Since the last level use the same formula, they share the same max speed, if it's lower than 5. I've honestly not understood how it stays at 5. And since the last level is only one level among the 14 available levels and is completely different, I decided to go with this change.

# Detailled descriptions of the randomizers:
    -> Astro randomizer: X maxspeed, Y up maxspeed, jetpack acceleration, X acceleration
    -> X max speed is randomized with a value of the following range: [3,4,5,6,7,8,9,10]
        - Vanilla value is 7, but actual vanilla behavior is a little bit over 3
        - This has a side effect of altering the max speed of the last level if the new maxspeed is 3-4-5. Vanilla maxspeed is 5. The new "vanilla" value following forementionned modification is 3.
    -> Y max speed is randomized to a value of the following range: [3,4,5,6,7,8]
        - Vanilla value is 3
        - This has a side effect of altering the last level's y max speed. The vanilla speed in this level is 3. The maxpseed in the last level can go up to 5.

    -> X acceleration is randomized: Note that there are two pieces : the friction that always reduce the speed of the astronaut and the acceleration.
        - the friction is randomized. It can be any value from 0 to 243.
        - The acceleration is randomized. It is always at least 12 over the friction, with a maximum of 255.
    -> Y acceleration is randomized : currently only the jetpack power is randomized.
        - Jetpack's power is randomized. It can be in the following range: [32,..., 255].

    -> Palette randomizer: colors
    I made a somewhat algorithm to make sure the rocket's colors make sense.
    -> Rocket randomizer: X&Y maxspeed, acceleration
    -- The X&Y max speed is randomized together : it can be any from the following value: [3,4,5,6,7,8]
        -> Vanilla value is 3.
        -> This has a side effect of altering astronaut's max fallspeed as they share the same Y maxspeed.
    -- The acceleration is randomized:
        - The acceleration for X and Y speed depends on the rocket's direction. This dependency is randomized. It can be either : [vanilla, linearized, reversed]
        - The max value of acceleration is randomized. it can be anything in the following range : [64,...,255]
            -> 64 is vanilla.
        - All the others acceleration of the distribution are adjusted with the same ratio of vanilla max accel vs. randomized max accel.

# Modes:
    -> Normal : This is the normal mode. No major changes.
    -> reckless : This mode will remove the constraints that block you from being a true bulldozer. Fear not of the walls nor enemies with this mode! Note that this doesn't remove the OHKO collisions from the last level.
        -> This mode highlight the rocket's randomizer
        -> disable any rocket damage from enemies bullet.
        -> Disable any rocket damage from wall collisions.


# ACKNOLEDGEMENTS:
    steve_hacks : For answering my multiples questions and being patient.
    MeleeWizard : For suggesting this game and helping in the testings
    sbm : For helping in understanding upcodes
    TheMotherBrains86 : For speedrunning this game, showing big interest in the randomizer, and running this for the Randomania superweek.
    Randomania discord channel for being a useful place to learn about randomizers.
    Randomizers communities : This randomizer is inspired by other randomizers' "structure".