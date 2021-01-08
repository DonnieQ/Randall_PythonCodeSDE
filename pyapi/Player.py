import Items
class Player:
    def __init__(self):
        self.inventory = [Items.Kamehameha]
        self.hp = 100
    
    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            # isinstance(object, type) -- returns true if i is actaully that type 
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        # using format to print best weapon currently in inventory
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))
