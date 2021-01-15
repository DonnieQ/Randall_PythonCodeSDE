#!/usr/bin/env python3
from collections import OrderedDict
from Player import Player
import World


def play():
    with open('intro.txt', 'r') as f:
        print(f.read())
    #loading in built world
    World.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = World.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("Your journey has come to an early end!")

# loop until we get valid input from user. if action: = to if action!=None. 
def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)#use get to validate agaisn't invalid hot keys
        if action:
            action()
        else:
            print("Invalid action!")

#using OrderdDict(), store actions into dictionary and appear in the same order every time
def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory")

    if isinstance(room, World.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        if World.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if World.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if World.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if World.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")

    return actions

#helper function for get_available_actions
def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()
