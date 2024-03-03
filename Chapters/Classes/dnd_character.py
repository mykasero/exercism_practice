from random import randint as rint
import math


def modifier(number):
    return math.floor((number - 10) / 2)


class Character:
    def __init__(self):
        self.stats = []  # str, dex, const, int, wisd, cha
        self.rolls = []  # 4 rolled nums from a 6D
        self.hitpoints = 10

        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

        for stats in range(6):
            for rolls in range(4):
                self.rolls.append(rint(1, 6))
            self.rolls.pop(self.rolls.index(min(self.rolls)))
            self.stats.append(sum(self.rolls))
            self.rolls = []

        self.strength = self.stats[0]
        self.dexterity = self.stats[1]
        self.constitution = self.stats[2]
        self.intelligence = self.stats[3]
        self.wisdom = self.stats[4]
        self.charisma = self.stats[5]

        self.hitpoints = 10 + math.floor((self.constitution - 10) / 2)

    def ability(self):
        return self.stats[rint(0, 5)]
