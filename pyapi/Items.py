class Item:
    """""""Base class for all items"""""""

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self): #Passing  variable weapon values using .format
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    

# using super to inherit from primary class Item
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self): #Passing  variable weapon values using .format
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Kamehameha(Weapon):
    def __init__(self):
        super().__init__(name="Kamehameha",
                         description="A move granted from Master Goku, use wisely",
                         value=50,
                         damage=30)


class Final_Flash(Weapon):
    def __init__(self):
        super().__init__(name="Final Flash",
                         description="From the Prince of all Sayains!! With love, Vegeta",
                         value=80,
                         damage=60)
