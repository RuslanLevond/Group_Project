from Player import *
from Items import *
from Game import *
## This is going to be moved to the main game and renamed to execute_combat
def attacks(enemy):
    if enemy["base_health"] == enemy["health"]:
        print("The", enemy["name"], "is about to attack you and the only way to get past will be to defeat him!")
        for items in player[inventory]:
            print ("use", items[name].upper, "to attack the guard first")
        print("what would you like to do?")
        player_input = action_menu(inventory)
        if player_input[0] == "security" or "baseball":
            enemy["health"] = enemy["health"] - 1
            player_health = player_health - damage
        elif player_input[0] == "pistol":
            enemy["health"] = enemy["health"] - 2
            player_health = player_health - damage
        elif player_input[0] == "stun":
            enemy["health"] = enmemy["health"] - 4
            player_health = player_health - damage
    elif enemy["health"] > 0 and enemy["health"] < enemy["base_health"]:
        print("The", enemy["name"], "is still alive and about to attack again, what will you do?")
        for items in player[inventory]:
            print ("USE", items[name].upper, "to attack the", name, "first")
        print("what would you like to do?")
        player_input = action_menu(inventory)
        if player_input[0] == "security" or "baseball":
            enemy["health"] = enemy["health"] - 1
            player_health = player_health - damage
        elif player_input[0] == "pistol":
            enemy["health"] = enemy["health"] - 2
            player_health = player_health - damage
        elif player_input[0] == "stun":
            enemy["health"] = enemy["health"] - 3
            player_health = player_health - damage
    else:
        print("you have killed the", enemy["name"],"anything the", enemy["name"], "had would have dropped on the floor")
## this is what will actually be in this file!!
enemy_guard_outside = {
    "name" : "guard",
    "health" : 3,
    "base_health" : 3,
    "damage" : 1
    }
enemy_receptionist = {
    "name" : "receptionist",
    "health" : 2,
    "base_health" : 2,
    "damage" : 1
    }
enemy_guard_toilet = {
    "name" : "guard",
    "health" : 4,
    "base_health" : 4,
    "damage" : 1
    }
enemy_guard_floor1 = {
    "name" : "guard",
    "health" : 3,
    "base_health" : 3,
    "damage" : 2
    }
enemy_guard_security = {
    "name" : "guard",
    "health" : 5,
    "base_health" : 5,
    "damage" : 1
    }
enemy_BIGBOSS = {
    "name" : "big boss",
    "health" : 8,
    "base_health" : 8,
    "damage" : 2
    }
enemies = {
    "guard_outside" : enemy_guard_outside,
    "receptionist" : enemy_receptionist,
    "toilet_guard" : enemy_guard_toilet,
    "floor1_guard" : enemy_guard_floor1,
    "Security_guard" : enemy_guard_security,
    "big_boss" : enemy_BIGBOSS
    }
## to call the function will be attacks(enemies[guard_outside])
