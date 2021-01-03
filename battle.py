#!/usr/bin/env python3
import random

def fight(player, mon):
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
def execute(option, p1, mon):
    if(option == "1"):
        fight(p1, mon)
    else:
        print("You ran from the fight.")
