#!/usr/bin/env python3
import random

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

