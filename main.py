class GameCharacter:
    def __init__(self, name, health, level, power):
        self.name = name
        self._health = health
        self._level = level
        self.__power = power

    def attack(self):
        self._health -= 20

    def heal(self, x):
        self._health += x

    def level_up(self):
        self._level += 1

    def info(self):
        print(f"Health:{self._health}")
        print(f"Level:{self._level}")


g1 = GameCharacter("Hero", 100, 1, 50)
g1.attack()
g1.info()
g1.heal(20)
g1.info()
g1.level_up()
g1.info()
