import random
from weapon import Weapon
from spellbook import *

class Character(Weapon, SpellBook):
    base_hit_points = 100
    base_mana_points = 50
    experience = 0
    weapon_damage = 0

    def get_class(self):
        class_choice = input("What is your class? [W]arrior, [M]age, [A]rcher: ").lower()
        while class_choice not in 'wma':
            class_choice = input("What is your class? [W]arrior, [M]age, [A]rcher: ").lower()
        else:
            if class_choice == 'w':
                return 'Warrior'
            elif class_choice == 'm':
                return 'Mage'
            elif class_choice == 'a':
                return 'Archer'

    def get_weapon(self):
        if self.class_choice == 'Warrior':
            self.weapon = 'Sword'
            self.get_weapon_stats()
            return 'Sword'
        elif self.class_choice == 'Mage':
            self.weapon = 'Staff'
            self.get_weapon_stats()
            return 'Staff'
        elif self.class_choice == 'Archer':
            self.weapon = 'Bow'
            self.get_weapon_stats()
            return 'Bow'

    def get_spell_book(self):
        if self.class_choice == 'Warrior':
            if self.level >= 1:
                self.spell_book.append(Warrior_spells[0])
                if self.level >= 5:
                    self.spell_book.append(Warrior_spells[1])
                    if self.level >= 10:
                        self.spell_book.append(Warrior_spells[2])
        elif self.class_choice == 'Mage':
            if self.level >= 1:
                self.spell_book.append(Mage_spells[0])
                if self.level >= 5:
                    self.spell_book.append(Mage_spells[1])
                    if self.level >= 10:
                        self.spell_book.append(Mage_spells[2])
        elif self.class_choice == 'Archer':
            if self.level >= 1:
                self.spell_book.append(Archer_spells[0])
                if self.level >= 5:
                    self.spell_book.append(Archer_spells[1])
                    if self.level >= 10:
                        self.spell_book.append(Archer_spells[2])


    def __init__(self, **kwargs):
        self.name = input("Character Name: ")
        self.hit_points = self.base_hit_points
        self.mana_points = self.base_mana_points
        self.level = 10
        self.attack_points = self.level * 1.3
        self.experience = 0
        self.class_choice = self.get_class()
        self.weapon = self.get_weapon()
        self.damage = int(self.weapon_damage * self.attack_points)
        self.spell_book = []
        self.get_spell_book()
        self.skilltree = {}
        self.inventory = {}


        for key, value in kwargs.items():
            setattr(self, key, value)

        # self.name =
        # na

    def __str__(self):
        return '{}, the {}, Level: {}, HP: {}, MP: {}, XP: {}, Weapon: {}, Damage: {}'.format(self.name, self.class_choice, self.level, self.hit_points, self.mana_points, self.experience, self.weapon, self.damage)
    #
    # def attack(self):
    #
    # def cast():
    #     print(self.spells)
    #
    # def inventory():
    #
    # def move():
    #
    # def spells():
    #
    # def rest():
