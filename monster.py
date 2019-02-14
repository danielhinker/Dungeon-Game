import random

COLORS = ['Water', 'Fire', 'Dark', 'Wind', 'Silver', 'Gold', 'Platinum', 'Light']

class Monster:
    level = 1
    hit_points = 1
    mana_points = 1
    attack_points = 1
    experience = 1
    sound = ''


    def __init__(self, **kwargs):
        self.color = random.choice(COLORS)
        if self.color == 'Dark':
            self.hit_points = self.hit_points * 2
            self.attack_points = self.attack_points * 2
            self.experience = self.experience * 1.5

    def __str__(self):
        return "{} {}, HP: {}".format(self.color, self.__class__.__name__, self.hit_points)

    def battlecry(self):
        return self.sound


class Poring(Monster):
    level = 1
    hit_points = 15
    experience = 10
    attack_points = 15
    sound = 'squeak'

class Willow(Monster):
    level = 5
    hit_points = 50
    experience = 35
    attack_points = random.randint(30, 50)
    sound = 'Bark'

class Minotaur(Monster):
    level = 30
    hit_points = 450
    experience = 100
    attack_points = 100
    sound = 'For Aiur'

class Archangel(Monster):
    level = 50
    hit_points = 600
    experience = 500
    attack_points = 250
    sound = 'Judgement will be passed'

class Thanatos(Monster):
    level = 99
    hit_points = 6000
    experience = 9000
    attack_points = 750
    sound = 'The end is now'

Jester_AP = [1, 1, 1, 1, 1, 1, 99999]
class Jester(Monster):
    level = 10
    hit_points = 100
    experience = 100
    attack_points = random.choice(Jester_AP)
    sound = 'The end is now'