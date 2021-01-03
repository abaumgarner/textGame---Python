#!/usr/bin/env python3
import random

""" Author: Aaron Baumgarner
    Created: 12/14/20
    Updated: 1/3/21
    Notes: This class contains all of the battle logic. In the fight function, a dex number is generated and compared to the monster's dex. This is loosly based on DnD battle mechanics 
            that I vaguely remember to make it a little more insteresting than just looking at the base str of each. If the dexRoll is larger than the monster's then the player attacks.
            If the dexRoll is lower than the monster's, the monster attacks. The execute function is used to start a battle from the game class.

"""

""" Main battle mechanics """
def fight(player, mon):
    """ Loosely based on DnD from what I can remember to make the game more insteresting and outcomes more random """
    dexRoll = (round(random.random()*10))+2

    if(dexRoll > mon.dex):
        mon.hp -= player.dmg

        if mon.hp < 0:
            mon.hp = 0
        elif player.hp < 0:
            player.hp = 0
        print(player.name + " " + player.attack() + " the " + mon.name + " dealing " + str(player.dmg) + " points of damage.")
        
        if(mon.hp <= 0):
            print(mon.name + " has been defeated.")
        else:
            print(mon.name + " has " + mon.printHp() + " hp left.")
    elif(dexRoll == mon.dex and player.str > mon.str):
        mon.hp -= player.dmg
        print(player.name + " " + player.attack() + " the " + mon.name + " dealing " + str(player.dmg) + " points of damage.")
        
        if(mon.hp <= 0):
            print(mon.name + " has been defeated.")
        else:
            print(mon.name + " has " + mon.hp + " hp left.")
    else:
        player.hp -= mon.dmg

        if(player.hp <= 0):
            print(player.name + " has been defeated.")
        else:
            print(mon.name + " " + mon.attack() + " " + player.name + " dealing " + str(mon.dmg) + " points of damage.")

""" Used to start the battle. Original thought was to handle the running in here as well but I switched it to the main game class """
def execute(option, p1, mon):
    if(option == "1"):
        fight(p1, mon)
    else:
        print("You ran from the fight.")
