#!/usr/bin/env python3

""" Author: Aaron Baumgarner
    Created: 12/14/20
    Updated: 1/3/21
    Notes: Main class where the game starts. The user is prompted for a username and then a monster is randomly generated. Once the monster has been generated
            the user is prompted to either attack, run, or quit the game. Attacking will run the battle class. If the user decides to run, the current encounter
            will end and a new monster will be randomly selected. This little program was created to pass the time and to get me back into programming. 

"""

import player
import monster
import battle

username = input("Enter Username: ")
p1 = player.Character(username)
mon = monster.encounter()
print()
print("A mighty " + mon.name + " appears.")

while p1.hp > 0:
    print("\t" + p1.name + "\t\t" + "Monster")
    print("      ---------------------------")
    print("HP: \t " + p1.printHp() + "\t\t " + mon.printHp())
    print("STR: \t " + p1.printStr() + "\t\t " + mon.printStr())

    print()
    print("1) Attack")
    print("2) Run")
    print("Q) Quit")

    option = input("Which would you like to do: ")
    if option == "Q":
        exit()
    elif option == "1":
        battle.execute(option, p1, mon)
    elif option == "2":
        print("You ran from the monster.")
        print()
        mon = monster.encounter()
        print()
        print("A mighty " + mon.name + " appears.")

    if mon.hp == 0:
        mon = monster.encounter()
        print()
        print()
        print("A mighty " + mon.name + " appears.")