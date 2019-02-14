
WEAPONS = ['bow', 'sword', 'staff', 'dagger',]


class Weapon:
    base_damage = 1
    critical_damage = 1
    critical_chance = 1
    attack_speed = 1
    cast_time = 1



    def get_weapon_stats(self):
        if self.weapon =='Bow':
            self.weapon_damage = 3
            # self.critical_damage = self.damage * 2
            # self.critical_chance = self.critical * 0.15
            # self.attack_speed = self.attack_speed * 1
        if self.weapon == 'Sword':
            self.weapon_damage = 6
            # self.critical_damage = self.damage * 2
            # self.critical_chance = self.critical * 0.15
            # self.attack_speed = self.attack_speed * 2
        if self.weapon =='Dagger':
            self.weapon_damage = 6
            # self.critical_damage = self.damage * 2
            # self.critical_chance = self.critical * 0.15
            # self.attack_speed = self.attack_speed * 2
        if self.weapon =='Staff':
            self.weapon_damage = 1
            # self.critical_damage = self.damage * 1.5
            # self.critical_chance = self.critical * 0.10
            # self.attack_speed = self.attack_speed * 3
            # self.cast_time = self.cast_time * 1.5


class SwordofaThousandTruths(Weapon):
    base_damage = 100000000000
