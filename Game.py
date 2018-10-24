from Map import *
from Player import *
from Items import *
from Gameparser import *
from People import *
from Enemies import *
import random
import time
def list_of_items(items):
    #This function puts items into the list.
    string = ''
    new_list = []
    for item in items:
        new_list.append(item["name"])
        string = ", ".join(new_list)
    return string

def list_of_people(people):

    if not people:
        return str("")
    else:
        return ', '.join(str(k["name"] + " (" + str(k["description"]) + ")") for k in list(people))

def print_room_items(room):
    #This function takes a room as an input and prints all of the items.
    list_items = list_of_items(room["items"])
    if(list_items == ""):
        print("There are no items here.")
    else:
        print("There is " + list_items + " here.\n")

def print_room_people(room):

    h = list_of_people(room["people"])
    if str(h) == "":
        pass
    else:
        print("There is " + str(h) + " here.")
        print("")
        
def print_inventory_items(items):
    #This function takes a list of player's inventory items and prints them.
    list_items = list_of_items(items)
    if (list_items == ""):
        print("You don't have any items.")
    else:
        print("You have " + list_items + ".\n")

def print_room(room):
    #This function prints out the current room with description and items.
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()

        
def exit_leads_to(exits, direction):
    #This function takes a dictionary of exits and a direction, returns the exits from the current room.
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    #This function prints out where the player can go, the direction and the exit it leads to.
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items, room_people, room_enemies):
    #This function calls print_exit and exit_leads_to functions which outputs player navigation options. As well, it prints out what items the player can take and drop.
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for q in room_people:
        print("ASK " + q["id"].upper() + " to ask the " + q["name"] + " if they can help"
            " you find your target.")
 
    print("SEARCH PLACE to search for items around.")
    if inventory != []:
        print ("SHOW INVENTORY to see your inventory.")
    if room_enemies == []:
        print("REST to sleep and regain your stamina.")
    if(current_room == rooms["Station1"] and items_train_ticket["acquired"] == False):
        print("BUY to buy a train ticket.")
    if(current_room == rooms["Elevator"]):	
       print("PIN to enter a pin number to use the elevator.")
       
    print("STATS to check your character's stats.")
    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):

    #Reception door condition
    if security_room_pass == False and current_room == rooms["Reception1"] and chosen_exit == "north":
        return False

    #Control room condition
    if items_b1_keycard not in inventory and current_room == rooms["Lobby1"] and chosen_exit == "south":
        return False
    #Rope condition
    if items_rope not in inventory and current_room == rooms["Roof1"] and chosen_exit == "north":
        return False 
    #This function checks if the exit the player has inputted is valid.
    return chosen_exit in exits

def mass_kg():
    mass = 0
    for c in inventory:
        mass = mass + c["mass"]
        if mass > 2.5:
            mass = mass - c["mass"]
            print("")
            print("You are currently carrying " + str(mass) + " kg.")
            print("You cannot carry heavier than 2.5 kg.")
            print("You have to drop something in order to take the item.")
            return False

# def weight_ok(item_id):
#     #This function checks if the weight of the inventory does not exceed player's item weight limit.
#     total_mass = 0
#     for item in inventory:
#         total_mass = total_mass + item["mass"]
#     total_mass = total_mass + items[item_id]["mass"]
#     if (total_mass < 3):
#         return True
#     else:
#         return False

def execute_go(direction, stamina):
    #This function calls is_valid_exit function which would check if the exit is valid and then if the exit is valid, it would update the current room.
    global current_room
    global security_room_pass
    check = 0
    #Lobby check
    if current_room == rooms["Lobby1"]:
        security_room_pass = True
    if current_room == rooms["Roof1"]:
        check = 1
        
    
    exits = current_room["exits"]
    if is_valid_exit(exits, direction) == True:
        if (items_train_ticket["acquired"] == False and current_room["name"] == "the NORTH train station" and direction == "south"):
            print("You cannot travel on the train, please buy a train ticket.")
        elif (room_elevator["allowed"] == False and direction == "up" and current_room == rooms["Elevator"]):	
           print("To use the elevator, you need to enter a pin number.")
        else:
            current_room = move(exits, direction)
            stamina = stamina - 1
        
    else:
        print("You cannot go there.")
    return stamina

def execute_ask(people_id):
    o = current_room["people"]
    if o == []:
        print("There is nobody here")
    else:
        for l in o:
            if people_id == l["id"]:
                print("")
                print("YOU:")
                print("")
                print("Hey, have you seen anyone suspicious running around?")
                print("")
                print(l["name"].upper() + ":")
                print("")
                print(l["knowledge"])
                break
    if people_id != l["id"]:
        print("You cannot ask this person!")


def execute_take(item_id):
    #This function will check if the item is in the room and will put it in the player's inventory only in the case if the weight is ok and the item is in the room
    items_in_room = current_room["items"]
    if items_in_room == []:
        print("There are no items left to take in this room.")
    else:
        for items in items_in_room:
            if items["id"] == item_id:
                inventory.append(items)
                items_in_room.remove(items)
                if (items["id"] == "strength"):
                    attribute_dictionary["Strength"] = attribute_dictionary["Strength"] + 1
                    stats_dictionary["Max health"] = stats_dictionary["Max health"] + 1 
                    print("Your strength attributes has been increased.")
                    inventory.remove(items)
                elif (items["id"] == "intelligence"):
                    attribute_dictionary["Intelligence"] = attribute_dictionary["Intelligence"] + 1
                    stats_dictionary["Accuracy"] = stats_dictionary["Accuracy"] - 1
                    print("Your intelligence attributes has been increased.")
                    inventory.remove(items)
                elif (items["id"] == "agility"):
                    attribute_dictionary["Agility"] = attribute_dictionary["Agility"] + 1
                    stats_dictionary["Stamina"] = stats_dictionary["Stamina"] + 1
                    print("Your agility attributes has been increased.")
                    inventory.remove(items)
                elif (items["id"] == "aid"):
                    print("Your health has been regenerated.")
                    stats_dictionary["Max health"] = attribute_dictionary["Strength"] + 8
                    inventory.remove(items)
                elif (items["id"] == "serum"):
                    break
                break
        if items["id"] != item_id:
            print("You cannot take that.")
        if mass_kg() == False:
            inventory.remove(items)
            items_in_room.append(items)
    

def execute_drop(item_id):
    #This function works just like execute_take function, it will check if the item is in inventory and then drop it into the room's items.
    if inventory == []:
        print("You don't have any items.")
    else:
        for r in inventory:
            if item_id == r["id"]:
                current_room["items"].append(r)
                inventory.remove(r)
                break
        if r["id"] != item_id:
            print("You cannot drop that.")

def execute_stats(attribute, stamina):
    #This function will show current player's stats, all of the attributes they have picked. The attribute parameter is going to be attribute_dictionary.
    print()
    print("Your current attributes are:")
    print("Strength - " + str(attribute["Strength"]))
    print("Intelligence - " + str(attribute["Intelligence"]))
    print("Agility - " + str(attribute["Agility"]))
    print()
    print("Your current stats are:")
    print("Health - " + str(stats_dictionary["Max health"]))
    print("Accuracy (chance of hitting an enemy)- 1/" + str(stats_dictionary["Accuracy"]))
    print("Stamina (if it hits 0, you are not able to enter any rooms. To regain stamina, you will need to rest.)- " + str(stamina))
    return stamina

def execute_buy():
    #This function will be used in the train station to buy a ticket for the train. The player can go to the train station two only with the ticket.
    for inv in inventory:
        if (inv["id"] == "ticket" and current_room == rooms["Station1"]):
            print("You cannot buy anymore tickets.")
    if (current_room == rooms["Station1"] and items_train_ticket["acquired"] == False):
        print("You bought a ticket for the train. Now you can go on the train.")
        inventory.append(items_train_ticket)
        items_train_ticket["acquired"] = True
    elif (current_room != rooms["Station1"]):
        print("You cannot buy in this room.")

def execute_pin(user_pin):
    #This function will check if the user has entered a valid pin number for the elevator. If not, then the enter_pin function will be executed where the player will be asked to enter a pin number again. Otherwise, the player can use the elevator.
    #Here is a new variable which is elevator_pin variable, it will be used as a reference to the user's pin, it will check if they have entered a correct pin. Elevator pin is - 179535
    print("You are entering a pin number to use the elevator...")
    if(current_room == rooms["Elevator"] and user_pin == elevator_pin):
        
        print("You have entered correct pin number.")
        print("Now you can use the elevator.")
        room_elevator["allowed"] = True
    elif(current_room == rooms["Elevator"] and user_pin != elevator_pin):
        
        print("You have entered a wrong pin number, please enter a correct pin number")
    else:
        pass

def execute_rest(stamina):
    #This function will regain player's stamina by resting. The player will not be able to rest if there is an enemy in the room. It will put player's stamina back to the default which is effected by the attributes using updated_stamina variable as max_rest parameter which is declared in the Player.py
    if (current_room["enemies"] == []):
        sec = 0
        print("You are resting...")
        while sec < 5:
            sec += 1
            time.sleep(1)
            print("...")
            if(sec == 5):
                stamina = stats_dictionary["Stamina"]
                print("Your current Stamina: " + str(stamina))
                print("You have rested, now you stamina is back to usual.")
    else:
        print("You cannot rest here, there is an enemy nearby.")
    return stamina

def execute_inventory():
    print_inventory_items(inventory)
    print ("You can:")
    for item in inventory:
        print("DROP " + item["id"].upper() + " to drop your " + item["name"] + ".")
    print ("DO NOTHING")
    command = inventory_menu(current_room["exits"], current_room["items"], inventory, current_room["people"])
    execute_command(command)


def execute_search(room):
    print_room_items(current_room)
    print ("You can:")
    for i in current_room["items"]:
        print("TAKE " + i["id"].upper() + " to take " + i["name"] + ".")
    print ("DO NOTHING")
    command = search_menu(current_room["exits"], current_room["items"], inventory, current_room["people"])
    execute_command(command)

def execute_command_stamina(command, stamina):
    if command[0] == "go":
        if(stamina == 0):
           print("You cannot walk any further, you are way too tired. You need some sleep!")	
           return stamina
        elif len(command) > 1:
            stamina = execute_go(command[1], stamina)
            return stamina
        else:
            print("Go where?")
            return stamina

    elif command[0] == "rest":
        stamina = execute_rest(stamina)
        return stamina
    elif command[0] == "stats":
        stamina = execute_stats(attribute_dictionary, stamina)
        return stamina
    else:
        execute_command(command)
        return stamina
        
def execute_command(command):
    #This function will check if user types in go, take or drop and will call appropriate execute functions.
    #Not sure if this line was necessary as we will be using 0 length commands. if 0 == len(command):
        #return
    if command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "ask":
        if len(command) > 1:
            execute_ask(command[1])
        else:
            print("Ask who?")
        
    elif command[0] == "pin":
        if len(command) > 1:
            execute_pin(command[1])
        else:
            print("Please enter a pin number!")

    elif command[0] == "buy":
        execute_buy()

    elif command[0] == "inventory":
        execute_inventory()

    elif command[0] == "nothing":
        pass

    elif command[0] == "search":
        if len(command) > 1:
            execute_search(command[1])
        else:
            print("Search what?")

    else:
    	print("You can't do that!")

def menu(exits, room_items, inv_items, room_people, room_enemies):
    #This function will display the main menu, read player's input, normalise it and then return normalised user's input.
    
    # Display menu
    print_menu(exits, room_items, inv_items, room_people, room_enemies)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input
def inventory_menu(exits, room_items, inv_items, room_people):
    #This function will display the main menu, read player's input, normalise it and then return normalised user's input.

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def search_menu(exits, room_items, inv_items, room_people):
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input
def combat_menu(health, base_health, name, damage):
    player_input = ("")
    Player_Input = []
    while health > 0 and stats_dictionary["Max health"] > 0: 
        if health == base_health:
            print("The", name, "is about to attack you and the only way to get past will be to defeat him!")
            for items in inventory:
                print ("use", items["id"].upper(), "to attack the", name, "first")
            print("what would you like to do?")
            Player_Input = input(" ")
            Player_Input = normalise_input(Player_Input)
            player_input = "".join(Player_Input)
            for items in inventory:
                if items["id"] == player_input and player_input == "baton" or items["id"] == player_input and player_input == "baseball":
                    if randomiser() == True:
                        print("You have hit an enemy " + "'" + name + "'")
                        stats_dictionary["Max health"] = stats_dictionary["Max health"] - damage
                        health = health - 1
                    else:
                        print("You missed")
                elif items["id"] == player_input and player_input == "pistol":
                    if randomiser() == True:
                        print("You have hit an enemy " + "'" + name + "'")
                        stats_dictionary["Max health"] = stats_dictionary["Max health"] - damage
                        health = health - 2
                    else:
                        print("You missed")
                elif items["id"] == player_input and player_input == "stun":
                    inventory.remove(items_stun_gun)
                    if randomiser() == True:
                        print("You have hit an enemy " + "'" + name + "'")
                        stats_dictionary["Max health"] = stats_dictionary["Max health"] - damage
                        health = health - 4
                    else:
                        print("You missed")
        elif health > 0 and health < base_health:
            print("The", name, "is still alive and about to attack again, what will you do?")
            for items in inventory:
                print ("USE", items["id"].upper(), "to attack the", name, "first")
            print("what would you like to do?")
            Player_Input = input(" ")
            Player_Input = normalise_input(Player_Input)
            player_input = "".join(Player_Input)
            for items in inventory:
                if items["id"] == player_input and player_input == "baton" or items["id"] == player_input and player_input == "baseball":
                    if randomiser() == True:
                        print("You have hit an enemy " + "'" + name + "'")
                        stats_dictionary["Max health"] = stats_dictionary["Max health"] - damage
                        health = health - 1
                    else:
                        print("You missed")
                elif items["id"] == player_input and player_input == "pistol":
                    if randomiser() == True:
                        print("You have hit an enemy " + "'" + name + "'")
                        stats_dictionary["Max health"] = stats_dictionary["Max health"] - damage
                        health = health - 2
                    else:
                        print("You missed")
                elif items["id"] == player_input and player_input == "stun":
                    inventory.remove(items_stun_gun)
                    if randomiser() == True:
                        print("You have hit an enemy " + "'" + name + "'")
                        stats_dictionary["Max health"] = stats_dictionary["Max health"] - damage
                        health = health - 4
                    else:
                        print("You missed")
    if health < 1:
        print("you have killed the", name,"anything the", name, "had would have dropped on the floor")
        current_room["enemies"] = []

def move(exits, direction):
    #This function will return all rooms and directions from them which the player will move into.

    # Next room to go to
    return rooms[exits[direction]]

def check_ticket():	
   try:	
       if(current_room == rooms["Station2"]):	
           inventory.remove(items_train_ticket)	
   except:	
        pass	
def stamina(stamina):	
   current_stamina = stamina - 1	
   return current_stamina
def randomiser():
    randoms = 0
    randoms = random.randint(1,stats_dictionary["Accuracy"])
    if randoms == 1:
        return True
    else:
        return False

def main():
    player_attributes()
    body_type()	
    update_stats()	
    stamina = stats_dictionary["Stamina"]
    # Main game loop
    while True:
        check_ticket()
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_room_people(current_room)
        if current_room["enemies"] != []:
            combat_menu(current_room["enemies"][0]["health"], current_room["enemies"][0]["base_health"], current_room["enemies"][0]["name"], current_room["enemies"][0]["damage"])
        if stats_dictionary["Max health"] <= 0:
            print("YOU HAVE DIED")
            break
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory, current_room["people"], current_room["enemies"])
        # Execute the player's command
        stamina = execute_command_stamina(command,stamina)
        game_over = False
        for items in inventory:
            if (items == items_serum_207):
                print("COMPLETED IT MATE")
                game_over = True
                break
        if game_over == True:
            break

if __name__ == "__main__":
    main()

