#!/usr/bin/env python3
import random

""" Author: Aaron Baumgarner
    Created: 12/14/20
    Updated: 1/3/21
    Notes: Class used to create and contain all of the information about a player. Most settings are random to make the game more interesting, similar to roll die for DnD
            and placing the stats randomly. Leaving room for adding in XP and level ups as the player starts battling more and more monsters. Basic skeleton that can easily
            be updated as I think of new things.

"""

class Character:
    """ Initializing the player with all of the needed information """
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.dmg = (round(random.random()*10))+2
        self.str = (round(random.random()*10))+2
        self.dex = (round(random.random()*10))+2
        self.lvl = 1
        self.xp = 0
        self.weapon = "sword"
    
    """ Simple toString for str """
    def printStr(self):
        return str(self.str)
    
    """ Simple toString for HP """
    def printHp(self):
        return str(self.hp)
    
    """ Basic string for when the player attacks """
    def attack(self):
        return "used a " + self.weapon + " to attack"