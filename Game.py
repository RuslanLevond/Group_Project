from Map import rooms
from Player import *
from items import *
from Gameparser import *



def list_of_items(items):
    #This function puts items into the list.
    string = ''
    new_list = []
    for item in items:
        new_list.append(item["name"])
        string = ", ".join(new_list)
    return string
def print_room_items(room):
    #This function takes a room as an input and prints all of the items.
    list_items = list_of_items(room["items"])
    if(list_items == ""):
        pass
    else:
        print("There is " + list_items + " here.\n")

def print_inventory_items(items):
    #This function takes a list of player's inventory items and prints them.
    list_items = list_of_items(items)
    if (list_items == ""):
        pass
    else:
        print("You have " + list_items + ".\n")

def print_room(room):
    #This function prints out the current room with description and items.
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    if(room["items"] != []):
        print_room_items(room)
        
def exit_leads_to(exits, direction):
    #This function takes a dictionary of exits and a direction, returns the exits from the current room.
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    #This function prints out where the player can go, the direction and the exit it leads to.
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):
    #This function calls print_exit and exit_leads_to functions which outputs player navigation options. As well, it prints out what items the player can take and drop.
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop your " + item["name"] + ".")
    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    #This function checks if the exit the player has inputted is valid.
    return chosen_exit in exits

def weight_ok(item_id):
    #This function checks if the weight of the inventory does not exceed player's item weight limit.
    total_mass = 0
    for item in inventory:
        total_mass = total_mass + item["mass"]
    total_mass = total_mass + items[item_id]["mass"]
    if (total_mass < 3):
        return True
    else:
        return False

def execute_go(direction):
    #This function calls is_valid_exit function which would check if the exit is valid and then if the exit is valid, it would update the current room.
    global current_room
    if (is_valid_exit(current_room["exits"], direction) == True):
        new_room = move(current_room["exits"], direction)
        current_room = new_room
    else:
        print("You cannot go there.")
    


def execute_take(item_id):
    #This function will check if the item is in the room and will put it in the player's inventory only in the case if the weight is ok and the item is in the room.
    item_succeed = False
    for item in current_room["items"]:
        if(item["id"] == item_id):
            item_succeed = True
    if(item_succeed and weight_ok(item_id) == True):
        items_id = items[item_id]
        inventory.append(items_id)
        current_room["items"].remove(items_id)
    elif(item_succeed == False):
        print("You cannot take that.")
    elif(weight_ok(item_id) == False):
        print("You are carrying too much.")

    

def execute_drop(item_id):
    #This function works just like execute_take function, it will check if the item is in inventory and then drop it into the room's items.
    item_succeed = False
    for item in inventory:
        if(item["id"] == item_id):
            item_succeed = True
    if(item_succeed):
        items_id = items[item_id]
        current_room["items"].append(items_id)
        inventory.remove(items_id)
    else:
        print("You cannot drop that.")

def execute_stats(attribute):
    #This function will show current player's stats, all of the attributes they have picked. The attribute parameter is going to be attribute_dictionary.
    print("Your current stats are:")
    print("Strength - " + str(attribute["Strength"]))
    print("Intelligence - " + str(attribute["Intelligence"]))
    print("Agility - " + str(attribute["Agility"]))

def execute_buy():
    #This function will be used in the train station to buy a ticket for the train. The player can go to the train station two only with the ticket.
    print("You bought a ticket for the train. Now you can go on the train.")
    inventory.append(items["id"]["ticket"])

def execute_pin(user_pin)
    #This function will check if the user has entered a valid pin number for the elevator. If not, then the enter_pin function will be executed where the player will be asked to enter a pin number again. Otherwise, the player can use the elevator.
    #Here are two new variables which would need to be declared. elevator_pin variable will be used as a reference to the user's pin, it will check if they have entered a correct pin. Also, use_elevator variable which will be used to allow the users to use the elevator or not.
    print("You are entering a pin number to use the elevator...")
    if(user_pin == elevator_pin):
        print("You have entered correct pin number.")
        use_elevator = True
    else:
        print("You have entered a wrong pin number, please enter a correct pin number")
        enter_pin()
        
def enter_pin():
    #This function will execute only if the current room is elevator, it will ask the player to enter a pin number. It will return a pin number the user has entered.
    #The code to check if the current room is elevator. if(current_room == rooms["room_elevator"])
    #This function will need to be checked as an input for the validation.
    pin = input("Please enter a pin number to use the elevator: ")
    return pin

def execute_rest(max_rest):
    #This function will regain player's stamina by resting. The player will not be able to rest if there is an enemy in the room. It will put player's stamina back to the default which is effected by the attributes using updated_stamina variable as max_rest parameter which is declared in the Player.py
    if (current_room["enemy"] == "")
        print("You are resting...")
        stats_dictionary["Stamina"] = max_rest
        print("You have rested, now you stamina is back to usual.")
        print("Stamina : " + str(stats_dictionary["Stamina"]))
    else:
        print("You cannot rest here, there is an enemy nearby.")

def execute_command(command):
    #This function will check if user types in go, take or drop and will call appropriate execute functions.
    #Not sure if this line was necessary as we will be using 0 length commands. if 0 == len(command):
        #return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "stats":
        execute_stats(attribute_dictionary)
        
    elif command[0] == "pin":
        if len(command) > 1:
            execute_pin(command[1])
        else:
            print("Please enter a pin number!")

    elif command[0] == "buy":
        execute_buy()

    elif command[0] == "rest":
        execute_rest()

def menu(exits, room_items, inv_items):
    #This function will display the main menu, read player's input, normalise it and then return normalised user's input.
    
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    #This function will return all rooms and directions from them which the player will move into.

    # Next room to go to
    return rooms[exits[direction]]

def main():
    # Main game loop
    while True:
        if(player_win() == True):
            break
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

if __name__ == "__main__":
    main()

