#!/usr/bin/env python3
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.dmg = (round(random.random()*10))+2
        self.str = (round(random.random()*10))+2
        self.dex = (round(random.random()*10))+2
        self.lvl = 1
    def printStr(self):
        return str(self.str)
    def printHp(self):
        return str(self.hp)
    def attack(self):
        return "used a sword to attack"