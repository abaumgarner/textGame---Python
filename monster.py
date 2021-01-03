#!/usr/bin/env python3
import random

""" Author: Aaron Baumgarner
    Created: 12/14/20
    Updated: 1/3/21
    Notes: Class used for generating variuous monster types for the player to battle. This is based on how I would have written it in Java or C# but without extracting it even more. I could 
            write it with a single monster class and then send in each element but having a class for each monster type allows for someone to look at the code more easily. Encoutner function
            simply generates a new random number and creates a new monster based on the random number. I may need to adjust it to allow for more smaller monsters later on since a wolf is 
            generated more often. 

"""

""" Basic beast with moderate power """
class Beast:
    def __init__(self):
        self.name = "Beast"
        self.hp = 30
        self.str = 5
        self.dex = 6
        self.dmg = self.str
    def printStr(self):
        return str(self.str)
    def attack(self):
        return "tore"
    def printHp(self):
        return str(self.hp)

""" Simple wolf as cannon fodder """
class Wolf:
    def __init__(self):
        self.name = "Wolf"
        self.hp = 10
        self.str = 2
        self.dex = 1
        self.dmg = self.str
    def printStr(self):
        return str(self.str)
    def attack(self):
        return "clawed"
    def printHp(self):
        return str(self.hp)

""" Boss level monster """
class Dragon:
    def __init__(self):
        self.name = "Dragon"
        self.hp = 100
        self.str = 50
        self.dex = 100
        self.dmg = self.str
    def printStr(self):
        return str(self.str)
    def attack(self):
        return "bbq'd"
    def printHp(self):
        return str(self.hp)

""" Generates a new monster """
def encounter():
    num = round(random.random()*10)

    if(num == 1):
        mon = Beast()
    elif(num == 20):
        mon = Dragon()
    else:
        mon = Wolf()
    return mon

