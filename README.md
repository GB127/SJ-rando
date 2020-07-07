# Solar Jetman Randomizer
    This is a randomizer for the NES game "Solar Jetman : Hunt for the Golden Warpship."

    You will need a version of the game. I cannot help you on this.

    Current version : Version 1.3
    Wrote by Niamek.

    Discord channel : https://discord.gg/HNDEnvz


# Files included:
* .gitignore : You can delete this, it's for github and me.
* README.md : infos about the randomizer, please read at least the Getting started section.
* main.py : the one and only script to run. All the other scripts don't do anything interesting by themself.
* randomizer.py : This file includes everything:
** The codes for changing the game (and thus everything relies on this file).
** some code that will change very specific stuffs. 
** Includes all randomizers of the program.
* subrando.py : a module that containt fragments of codes needed for the randomizer.py file. Created to lighten the code of randomizer.py.

* Any other files are dev files. You can delete them.
** assembly.txt : This is a file I made to better understand some portion of the game. It's really a mess, so read at your own risk. You can delete this: none of the scripts need this file.
** infos.py : This is a file I use to store infos I found. You can delete this as the randomizer don't use it.

# Getting started:
    You need to download Python 3.8.
        https://realpython.com/installing-python/
    Drag the game named Vanilla.nes in the same folder.
        Note : You can rename your file without any issue.
        Note : The capital is important. I've never worked with anything that let you select your file or something. I personally prefer it with a capital, so for now, I settled with this. This is something I'll fix eventually.
    Open the command line on the same folder.
        For windows : https://www.thewindowsclub.com/how-to-open-command-prompt-from-right-click-menu/
    type the command : python main.py -h
        then press return/ENTER on the keyboard.
        This will display what the randomizer supports.
        You can skip this step.
    type the command with the settings you want to use.
        EXAMPLE : python main.py -arp --seed 450 --mode reckless

# Features :
* Some modes: normal, reckless
* Astronaut randomizer
* Palette randomizer
* Rocket's randomizer

## Future features :
* Gravity randomizer
* Weapon randomizer
* Item randomizer
* And much more!

# Modes:
    -> normal : This is the normal mode. No major changes.
    -> reckless : This mode will remove the constraints that block you from being a true bulldozer. Fear not of the walls nor enemies with this mode! This doesn't remove the OHKO collisions from the last level.
        -> This mode highlight the rocket's randomizer
        -> Disable any rocket damage from enemies bullet.
        -> Disable any rocket damage from wall collisions.
    -> goldhunt : This mode will remove the need of gathering the fuels before hunting the gold warpship. Ideal for a quick hunting game.
        -> This mode highlights the item randomizer.
        -> Set all planets' initial mothership's fuel to full.
        -> Change all fuels to fueltanks
    -> lateral : The gravity is now on the side!
        -> This mode highlights the gravity randomizer.
        -> The gravity now affect the X speed instead of Y speed
        -> Disable the spring effect

# ROM modifications :
    To open up some randomization, some instructions in the code were removed. As a side effect, alongside with some other randomizations, the last level is altered. To compromise, I've set a new "vanilla" X maxspeed for the last level and the astronaut's. If I understand FATRATKNIGHT's notes, my changes may have changed interactions between the pod and the thetered item. I did not notice this prior of Version 1. I'll leave it as is, since it's not that noticeable or huge.

    I've done this to allow astronaut maxspeed randomization. Since the last level use the same formula, they share the same max speed, if it's lower than 5. I've honestly not understood how it stays at 5. And since the last level is only one level among the 14 available levels and is completely different, I decided to go with this change.

    In summary :
        Astronaut max speed changes :
            X : 7 (3,56)  -> 3
            Y : 3  -> 3


        Last level :
            X max speed: 5 -> 3
            Y max speed: 3 -> 3


# Detailled descriptions of the randomizers:
    -> Astro randomizer: X maxspeed, Y up maxspeed, jetpack acceleration, X acceleration
        -> X max speed is randomized with a value of the following range: [3,4,5,6,7,8,9,10]
            - Vanilla value is 7, but actual vanilla behavior is a little bit over 3
            - NOTE: This has a side effect of altering the max speed of the last level if the new maxspeed is 3-4-5. Vanilla X maxspeed is 5. The new "vanilla" value following forementionned modification is 3.
        -> Y max speed is randomized to a value of the following range: [3,4,5,6,7,8]
            - Vanilla value is 3
            - NOTE: This has a side effect of altering the last level's y max speed. The vanilla speed in this level is 3. The maxpseed in the last level can go up to 5.

        -> X acceleration is randomized: Note that there are two pieces : the friction that always reduce the speed of the astronaut and the acceleration.
            - the friction is randomized. It can be any value from 0 to 243.
                - Vanilla : 2
            - The acceleration is randomized. It is always at least 12 over the friction to make sure it's playable, with a maximum of 255.
        -> Jetpack's power is randomized (Y acceleration for going up is randomized)
            - It can be in the following range: [22,..., 255].
                - Vanilla : 32

    -> Palette randomizer: colors
        I made a somewhat algorithm to make sure the rocket's colors make sense.
    -> Rocket randomizer: X&Y maxspeed, acceleration
        -- The X&Y max speed is randomized together : it can be any from the following value: [3,4,5,6,7,8]
            -> Vanilla value is 3.
            -> This has a side effect of altering astronaut's max fallspeed as they share the same Y maxspeed.
        -- The acceleration is randomized:
            - The acceleration for X and Y speed depends on the rocket's direction. This dependency is randomized. It can be either : [vanilla, linearized, reversed]
            - The max value of acceleration is randomized. it can be anything in the following range : [20,...,255]
                -> Note that the speed of the rocket will determine the minimum of the range. Here are the minimum according to speed:
                    speed => min acceleration
                    3 => 20
                    4 => 42
                    5 => 64
                    6 => 86
                    7 => 108
                    8 => 130
                -> 64 is vanilla.
            - All the others acceleration of the distribution are adjusted with the same ratio of vanilla max accel vs. randomized max accel.



# ACKNOLEDGEMENTS:
    steve_hacks : For answering my multiples questions and being patient.
    MeleeWizard : For suggesting this game and helping in the testings. Also big thanks for answering lots of my questions.
    TheMotherBrains86 : For speedrunning this game, showing big interest in the randomizer, and running this for the Randomania superweek.
    FATRATKNIGHT : for his lua script that gave me some useful infos to start everything. Here is the link of the lua script: http://tasvideos.org/userfiles/info/12531497925152203
    Randomania discord channel for being a useful place to learn about randomizers.
    Randomizers communities : This randomizer is inspired by other randomizers' "structure".
    sbm : For helping in understanding upcodes