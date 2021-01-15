class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie Classmate?", hp=10, damage=2)


class PhantomGina(Enemy):
    def __init__(self):
        super().__init__(name="Phantom Gina", hp=30, damage=15)

class AbelColony(Enemy):
    def __init__(self):
        super().__init__(name="Colony of little Abels", hp=100, damage=4)

class DustinZombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie Dustin", hp=80, damage=15)
