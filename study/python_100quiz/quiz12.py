class Wizard:
    status = {'skill': '파이어볼'}

    def __init__(self, **kwargs):
        self.status['health'] = kwargs['health']
        self.status['mana'] = kwargs['mana']
        self.status['armor'] = kwargs['armor']

    def attack(self):
        print(self.status['skill'])

    @property
    def health(self):
        return self.status['health']

    @property
    def mana(self):
        return self.status['mana']

    @property
    def armor(self):
        return self.status['armor']

    @health.setter
    def health(self, health):
        self.status['health'] = health

    @mana.setter
    def mana(self, mana):
        self.status['mana'] = mana

    @armor.setter
    def armor(self, armor):
        self.status['armor'] = armor


x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()
x.health = 111
print(x.health, x.mana, x.armor)


# class Wizard:
#     def stats(self, health, mana, armor):
#         self.health = health
#         self.mana = mana
#         self.armor = armor
#
#     def attack(self):
#         print('파이어볼')
#
#
# x = Wizard(health=545, mana=210, armor=10)
# print(x.health, x.mana, x.armor)
# x.attack()