#The attribute dictionary will store all of the skill points the player has chosen.
attribute_dictionary = {
    "Strength" : 0,
    "Intelligence" : 0,
    "Agility" : 0
    }
#Here all of the players stats would be stored, skill points the player have chosen would effect the character's statistics.
stats_dictionary = {
    "Max health" : 100,
    "Accuracy" : 0.25,
    "Stamina" : 5
    }
#This function is a creation menu, from here the player would be able to use their first 3 skill points on increasing their specific attributes.
def player_attributes():
    print("Here is the character creation menu, from here you can choose character's starter attributes.\nThrough out the game, you can find skill books which would increase your character's attributes.\nThey are strength, intelligence and agility.\n")
    print("Strength will increase your overall health.")
    print("Intelligence will increase your probability of hitting an enemy.")
    print("Agility increases your stamina and your character's energy levels, meaning that they will have to rest less.\n")
    print("You have 3 points to use.")
    skill_strength = 0
    skill_intelligence = 0
    skill_agility = 0
    
    skill_points = 3
    while True:
        first_input = input("Please enter how many points do you want to contribute towards your 'Strength' skill: ")
        try:
            first_input = int(first_input)
            if(first_input > skill_points):
                print("You cannot use that many skill points.")
            elif(first_input >= 0 or first_input <= 3):
                skill_points = skill_points - first_input
                print("Your remaining skill points: " + str(skill_points))
                skill_strength = skill_strength + first_input
            if(skill_points == 0):
                print("You have used all of your skill points.")
                print(str(skill_strength) + " : Strength.\n" + str(skill_intelligence) + " : Intelligence.\n" + str(skill_agility) + " : Agility.")
                for skill in attribute_dictionary:
                    if(skill == "Strength"):
                        attribute_dictionary["Strength"] = skill_strength
                    elif(skill == "Intelligence"):
                        attribute_dictionary["Intelligence"] = skill_intelligence
                    else:
                        attribute_dictionary["Agility"] = skill_agility
                break
        except:
            print("Please enter a number.")
        second_input = input("Please enter how many points do you want to contribute towards your 'Intelligence' skill: ")
        try:
            second_input = int(second_input)
            if(second_input > skill_points):
                print("You cannot use that many skill points.")
            elif(second_input >= 0 or second_input <= 3):
                skill_points = skill_points - second_input
                print("Your remaining skill points: " + str(skill_points))
                skill_intelligence = skill_intelligence + second_input
            if(skill_points == 0):
                print("You have used all of your skill points.")
                print(str(skill_strength) + " : Strength.\n" + str(skill_intelligence) + " : Intelligence.\n" + str(skill_agility) + " : Agility.")
                for skill in attribute_dictionary:
                    if(skill == "Strength"):
                        attribute_dictionary["Strength"] = skill_strength
                    elif(skill == "Intelligence"):
                        attribute_dictionary["Intelligence"] = skill_intelligence
                    else:
                        attribute_dictionary["Agility"] = skill_agility
                break
        except:
            print("Please enter a number.")
        third_input = input("Please enter how many points do you want to contribute towards your 'Agility' skill: ")
        try:
            third_input = int(third_input)
            if(third_input > skill_points):
                print("You cannot use that many skill points.")
            elif(third_input >= 0 or third_input <= 3):
                skill_points = skill_points - third_input
                print("Your remaining skill points: " + str(skill_points))
                skill_agility = skill_agility + third_input
            if(skill_points == 0):
                print("You have used all of your skill points.")
                print(str(skill_strength) + " : Strength.\n" + str(skill_intelligence) + " : Intelligence.\n" + str(skill_agility) + " : Agility.")
                for skill in attribute_dictionary:
                    if(skill == "Strength"):
                        attribute_dictionary["Strength"] = skill_strength
                    elif(skill == "Intelligence"):
                        attribute_dictionary["Intelligence"] = skill_intelligence
                    else:
                        attribute_dictionary["Agility"] = skill_agility
                break
        except:
            print("Please enter a number.")
#Body type function will call a menu from where the player can choose their character's body type. Depeding on what they choose, their character would be awarded with 2 additional skill points to a specific attribute branch.
def body_type():
    print("\nNow please choose your character's body type. Body types include 'Thin', 'Muscular' and 'Overweight'.")
    print("Depending on your choice, your character would get 2 additional skill points directed to specific attribute branch. e.g. Muscular body type will gain 2 strength skill points.\n")
    while True:
        weight = input("Please enter your character's body type by entering 'Thin', 'Muscular' or 'Overweight': ")
        if(weight.lower() == "thin"):
            attribute_dictionary["Agility"] = attribute_dictionary["Agility"] + 2
            print("As you have choosen your character to be " + weight.lower() + ", your character will have 2 bonus Agility skill points.\n")
            break
        elif(weight.lower() == "muscular"):
            attribute_dictionary["Strength"] = attribute_dictionary["Strength"] + 2
            print("As you have choosen your character to be " + weight.lower() + ", your character will have 2 bonus Strength skill points.\n")
            break
        elif(weight.lower() == "overweight"):
            attribute_dictionary["Intelligence"] = attribute_dictionary["Intelligence"] + 2
            print("As you have choosen your character to be " + weight.lower() + ", your character will have 2 bonus Intelligence skill points.\n")
            break
        else:
            print("Please enter an appropriate weight category.")
#The update function will update player's statistics depending on the attribute.
def update_attributes(attribute):
    if(attribute == "Strength"):
        stats_dictionary["Max health"] = stats_dictionary["Max health"] + 10
    elif(attribute == "Intelligence"):
        stats_dictionary["Accuracy"] = stats_dictionary["Accuracy"] + 0.10
    elif(attribute == "Agility"):
        stats_dictionary["Stamina"] = stats_dictionary["Stamina"] + 1
#This for loop would update all of the player's statistics using what skill points the player has chosen in player attributes and body type functions. 
for attribute in attribute_dictionary:
    if (attribute == "Strength" or attribute == "Intelligence" or attribute == "Agility"):
        counter = 0
        while True:
            if(counter == attribute_dictionary[attribute]):
               break
            update_attributes(attribute)
            counter = counter + 1
            
updated_stamina = stats_dictionary["Stamina"]
