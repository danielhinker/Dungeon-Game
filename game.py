import sys
from character import Character
from monster import *
from spellbook import *
import random

class Game:
    def setup(self):
        print("Welcome to the Dungeon!")
        print("Create your character!")
        self.player = Character()
        # self.spells = [ShieldSlash(),]
        # self.spell_book = self.get_spell()
        self.monsters = [Poring(), Willow(), Minotaur(), Archangel(), Thanatos(), Jester()]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            del self.monsters
            self.monsters = [Poring(), Willow(), Minotaur(), Archangel(), Thanatos(), Jester()]
            monster = random.choice(self.monsters)
            if monster.__class__.__name__ == 'Jester':
                monster.hit_points = self.player.damage * 2
            return monster

        except IndexError:
            return None

    def get_spell(self):
        try:
            for spell in self.player.spell_book:
                print("{}, Mana Cost: {}".format(spell.__class__.__name__, spell.mana_required))
            spell_choice = input("You have {} mana. Which spell do you want to cast?\n".format(self.player.mana_points)).lower()
            if spell_choice == '1':
                return self.player.spell_book[0]
            if spell_choice == '2':
                return self.player.spell_book[1]
            if spell_choice == '3':
                return self.player.spell_book[2]

        except IndexError:
            return None

    def cast_spell(self):
        spell = self.get_spell()
        if self.player.mana_points >= spell.mana_required:
            self.player.mana_points = self.player.mana_points - spell.mana_required
            self.monster.hit_points -= int(spell.spell_damage * self.player.attack_points)
            print("You used {} mana to cast {}. You have {} mana left".format(spell.mana_required, spell.__class__.__name__, self.player.mana_points))
            print("{} dealt {} damage".format(spell.__class__.__name__, int(spell.spell_damage * self.player.attack_points)))
        else:
            print("You need {} mana to cast {}".format(spell.mana_required, spell.__class__.__name__))
            self.attack()

    def attack(self):
        print("You're attacking {}!".format(self.monster))
        attack_choice = input("[W]eapon Attack, [C]ast Spells, [E]scape\n").lower()
        if attack_choice == 'c':
            self.cast_spell()
        elif attack_choice == 'w':
            self.monster.hit_points -= self.player.damage
            print("You dealt {} damage".format(self.player.damage))
        elif attack_choice == 'e':
            self.attack()


    def player_turn(self):
        player_choice = input("[I]nventory, [R]est, [M]ove, [A]ttack, [S]tatus, Spell[B]ook\n").lower()
        if player_choice == 'i':
            print(self.player.inventory)
        if player_choice == 's':
            print(self.player)
        if player_choice == 'r':
            self.player.hit_points += 10 * self.player.level
            self.player.mana_points += 10 * self.player.level
        if player_choice == 'b':
            print(self.player.spell_book)
        if player_choice == 'a':
            return self.attack()
        else:
            return self.player_turn()

    def monster_turn(self):
        if self.monster.hit_points > 0:
            print("{} is attacking you!".format(self.monster))
            self.monster.battlecry()
            self.player.hit_points -= self.monster.attack_points
            print("{} attacked you for {}!".format(self.monster, self.monster.attack_points))
            print("You are at {} HP!".format(self.player.hit_points))
        
    def cleanup(self):
        experience_needed = self.player.level * 5
        if self.monster.hit_points <= 0:
            self.player.experience =+ self.monster.experience
            if self.player.experience > experience_needed:
                self.player.level += 1
                self.player.attack_points = self.player.level * 1.3
                self.player.hit_points = self.player.base_hit_points * 1.6 * self.player.level
                self.player.mana_points = self.player.base_mana_points * 1.5 * self.player.level
                self.player.damage = int(self.player.weapon_damage * self.player.attack_points)
                for spell in self.player.spell_book:
                    spell.mana_required = int(spell.mana_required * (self.player.level * 0.2))
                print("You've leveled up!")
                print("You are now level {}".format(self.player.level))
                # self.player.get_spell_book()
                # self.player.spell_book.spell_damage = self.player.spell_book.spell_damage * self.player.attack_points
            print("You killed {}!".format(self.monster))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()
        print(self.player)

        while self.player.hit_points > 0:
            self.player_turn()
            self.monster_turn()
            self.cleanup()



        print("You died! Thanks for playing {}! You reached Level {}!".format(self.player.name, self.player.level))
        sys.exit()



Game()
