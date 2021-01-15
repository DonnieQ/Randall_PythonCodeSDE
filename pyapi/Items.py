class Item:
    """""""Base class for all items"""""""

    def __init__(self, name, description, value, picture):
        self.name = name
        self.description = description
        self.value = value
        self.picture = picture
    def __str__(self): #Passing  variable weapon values using .format
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


# user super to inherit from primary class Item
class Weapon(Item):
    def __init__(self, name, description, value, damage, picture):
        self.damage = damage
        super().__init__(name, description, value, picture)

    def __str__(self): #Passing  variable weapon values using .format
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Kamehameha(Weapon):
    def __init__(self):
        super().__init__(name="""Kamehameha""",
                         description="A move granted from Master Goku, use wisely",
                         value=50,
                         damage=30,
                         picture="""
_    ___    ___    ___    ___            
_`| / __`| / __`| / __`| / .-^  ___       
---/ /----/ /----/ /----/ /--=^^   ^^=,
--/ /----/ /----/ /----/ /---=__   __=' 
|._/   |._/   |._/   |._/       ^^^        

                         """)


class Final_Flash(Weapon):
    def __init__(self):
        super().__init__(name="Final Flash",
                         description="From the Prince of all Sayains!! With love, Vegeta",
                         value=80,
                         damage=60)

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{}HP)".format(self.name,self.healing_value)

class SensuBean(Consumable):
    def __init__(self):
        self.name = "Sensu Bean"
        self.healing_value = 30
