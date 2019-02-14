

class SpellBook:
    spell_damage = 1
    mana_required = 1
    # spell_name = ''
    # cast_time = 1

    # def get_spell_damage(self):
    #     if self.spell_name == 'Firebolt':
    #         self.spell_damage = 7
    #     if self.spell_name == 'Powerstrike':
    #         self.spell_damage = 3
    #     if self.spell_name == 'Doubleshot':
    #         self.spell_damage = 4
    #     if self.spell_name == 'Firebolt':
    #         self.spell_damage = 7
    #     if self.spell_name == 'Powerstrike':
    #         self.spell_damage = 3
    #     if self.spell_name == 'Doubleshot':
    #         self.spell_damage = 4

    # def __init__(self, **kwargs):
    #     self.damage = self.get_spell_damage()

    def __str__(self):
        return "{} is casted and does {}".format(self.__class__.__name__, self.spell_damage)

class ShieldSlash(SpellBook):
    spell_damage = 10
    mana_required = 10

class ChargingStar(SpellBook):
    spell_damage = 30
    mana_required = 20

class FinalJustice(SpellBook):
    spell_damage = 100
    mana_required = 50

class FireBolt(SpellBook):
    spell_damage = 60
    mana_required = 30

class GustofStorm(SpellBook):
    spell_damage = 150
    mana_required = 50

class LordofVermillion(SpellBook):
    spell_damage = 300
    mana_required = 80

class Doublestrafe(SpellBook):
    spell_damage = 40
    mana_required = 20

class BlitzBeat(SpellBook):
    spell_damage = 90
    mana_required = 30

class ArrowStorm(SpellBook):
    spell_damage = 130
    mana_required = 50


Warrior_spells = [ShieldSlash(), ChargingStar(), FinalJustice()]

Mage_spells = [FireBolt(), GustofStorm(), LordofVermillion()]

Archer_spells = [Doublestrafe(), BlitzBeat(), ArrowStorm()]