from map import rooms
from player import *
from items import *
from gameparser import *



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
    

def execute_command(command):
    #This function will check if user types in go, take or drop and will call appropriate execute functions.
    if 0 == len(command):
        return

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

    else:
        print("This makes no sense.")


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

