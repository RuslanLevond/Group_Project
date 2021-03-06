#places
from Items import *
from People import *
from Enemies import *

#Basement(rooms)
cell_room = {
    
    "name": "Agent 21 cell",
    
    "description": 
    """
You have been in this cell for weeks. Behind the cell doors
you will find the security room. The cell doors are facing north.""",

    "exits": {"north":"Securityroom1"},

    "items":[items_hair_pin],

    "enemies":[],

    "people": []
}

security_room = {
    
    "name": "Security room",

    "description":
    """ 
A guard has seemingly passed out next to his desk, how convenient. You better
check this room carefully, there could be useful items here. The staircase is
to the west of the security room.""",

    "exits": {"south": "Cell1", "west": "Stairsone1"},

    "items":[items_security_baton, items_b1_keycard],

    "enemies":[],

    "people": []

}

staircase_1 = {
    
    "name": "Basement staircase",

    "description":
    """ 
This seems to be the only way to get to the floor above. 
Go up to enter the ground floor or go east to enter the security room again. """,

    "exits": {"up":"Stairstwo1", "east": "Securityroom1"},

    "items":[],

    "enemies":[],

    "people": []
}


#Ground floor(rooms)
staircase_2 = {
    
    "name": "Ground floor staircase",

    "description":
    """ 
Going down will bring you to the basement floor. Going up will bring
you to the first floor. To enter the reception room go east """,

    "exits": {"up":"Stairsthree1", "down": "Stairsone1" , "east": "Reception1"},

    "items":[],

    "enemies": [],

    "people": []
}

reception_room = {
    
    "name": "Reception",

    "description":
    """ 
This is the reception room. The entrance to the building is north.
However, you will need promision from the control room. To get back to the 
staircase go west.""",

    "exits": {"north": "Building1", "west":"Stairstwo1"},

    "items": [items_strength_book],

    "enemies": [],

    "people": []
}

#First floor(rooms)
staircase_3 = {
    
    "name": "First floor stairs",

    "description":
    """
Going down will bring you back to the ground floor.
Going up will bring you to the roof. To enter the lobby go east.""",

    "exits": {"up": "Roof1", "down": "Stairstwo1", "east": "Lobby1"},

    "items":[],

    "enemies": [],

    "people": []
}

lobby_room = {
    
    "name": "The lobby",

    "description":
    """ 
You are at the lobby on floor one. Go south to enter the control room.
You wont be able to enter unless you have the key card.
To get back to the staircase go west.""",

    "exits": {"west":"Stairsthree1", "south": "Control1"},

    "items":[],

    "enemies": [],

    "people": []
}

control_room = {
    
    "name": "Control room",

    "description":
    """
This is the control room. You have unlocked the front doors in recepetion.
To go back to the lobby go north. However, your keycard got stuck and you
won't be able to use it again to enter the control room.""",

    "exits": {"north": "Lobby1"},

    "items":[],

    "enemies": [],

    "people": []
}



#Roof1
roof_floor = {
    
    "name":"Building one Roof",

    "description":
    """ 
You are on the roof. Its too high to jump down. Take the rope to get down.
To go back to the first floor go down.""",

    "exits": {"down": "Stairsthree1", "north": "Building1"},

    "items":[items_rope],

    "enemies": [],

    "people": []

}



### STREET MAP





place_building_one = {
    "name": "front of the bombed building",
    
    "description":
    """You have succesfully exited the building where you were imprisoned and now you
are standing in front of it. Police and other emergency services are probably on their way
to the building already.
Now you need to go after your targets. You have two safe choices from the place where you are now.
You can either go east to the garden or go west to an abandoned building
to avoid dealing with police, get some rest and pick up items.""",
    
    "exits": {"east": "Garden", "west": "Abandoned"},

    "items": [],

    "enemies": [],

    "people": []
    
#name of the street, a street id, items in the streets, a
#description of the street
#and all of the exits from this street to the others
}

place_abandoned_building = {
    "name": "the abandoned building",

    "description":
    """You have entered the abandoned building. There seems to be nothing
useful when you first entered. You can either search for items or leave the building from the south side.""",

    "exits": {"south": "Pharmacy"},

    "items":[items_intelligence_book],

    "enemies": [],

    "people": [people_junkie]
##int skillbook
}

place_garden = {
    "name": "the garden",

    "description":
    """You have entered the city garden. It is a very large garden with
variety of flowers, trees and fields. There are also a lot of benches and
historical statues. This garden leads to the train station. You see a strenght
skillbook on the floor. You can pick it up, or go south to the train station.""",

    "exits": {"south": "Station1", "west": "Building1"},

    "items": [items_strength_book],

    "enemies": [],

    "people": [people_old_lady]
##str skillbook
}

place_pharmacy = {
    "name": "the pharmacy",

    "description":
    """You have just entered the pharmacy. There are a lot of people browsing
and the ques is very long as it is the only pharmacy in this area.
You can only leave the pharmacy through its exit door which is on the east side and
leads to the toys store across the road.""",
    
    "exits": {"east": "Toys"},

    "items": [items_strength_book],

    "enemies": [],

    "people": []
##nothing
}

place_toys_shop = {
    "name": "the toys shop",

    "description":
    """You have now entered the toys shop. There is nobody inside the store and
the employee seems not to respond on your visit, but just look at their phone.
You see a strenght skillbook on the floor, which could be picked up. The nearest exit is
on the north side of the store and is leading outside the building you were
improsened earlier""",

    "exits": {"north": "Building1"},

    "items": [items_stun_gun],

    "enemies": [],

    "people": [people_child]
##str skillbook
}

place_train_station_one = {
    "name": "the NORTH train station",

    "description":
    """You are at the NORTH train station. The next train is already loading and leading
to the south station. You can either find a ticket to get on the train and go south
or you can go back to the garden from the north exit.""",

    "exits": {"north": "Garden", "south": "Station2"},

    "items": [],

    "enemies": [],

    "people": []
##ticket == false
##if ticket < 0, ticket==true
##ticket
}

place_train_station_two = {
    "name": "the SOUTH train station",

    "description":
    """You are at the SOUTH train station. The next train is already loading and leading
to the north station. You can either find a ticket to get on the train
and go back to the north train station
or you can leave the train station from one of the exits, east or west.""",

    "exits": {"west": "Centre", "east": "Parking"},

    "items": [],

    "enemies": [],

    "people": []
##ticket
}

place_city_centre = {
    "name": "the city centre",

    "description":
    """You are in the middle of the town. There are a lot of people
and events going on. It is very loud and crowded. It would be
difficult to recognize the target even if they are around here.
You have two options, to go east back to the train station or to go south
to the church.""",

    "exits": {"south": "Church", "east": "Station2"},

    "items": [items_baseball_bat],

    "enemies": [],

    "people": [people_mafia]
##nothing
}

place_parking = {
    "name": "the train station parking",

    "description":
    """You have come to the train station parking. It is almost full but you don't see
nobody around. It is very quiet. You can only see an agility skillbook next to the barrier at
the parking entrance. You can pick it up, or go back to the train station from the west exit. """,

    "exits": {"west": "Station2"},

    "items": [items_agility_book, items_pistol],

    "enemies": [],

    "people": []
##agi skillbook
}

place_church = {
    "name": "the church",

    "description":
    """You are currently in the church area. It is a very quiet area. It is not very busy at
the moment. There is an intelligence skill book at the entrance of the church. You can pick it up,
go north back to the city centre or you can continue south and go in front of the final building.""",

    "exits": {"north": "Centre", "south": "Building2"},

    "items": [items_intelligence_book],

    "enemies": [],

    "people": [people_priest]
##int skillbook
}

place_final_building = {
    "name": "front of the final building",

    "description":
    """You are now in front of the final building. It is a high, modern building in which your
traget could be hidning somewhere inside. This building has security guards and you don't know
where exactly your target is. You are now evaluating your options of entering the building and finding
your target, however you can go back to the church if you don't think the target is here or,
after the evaluation you feel like you need to pick up more items and want to go back and check if you
have missed something useful.""",

    "exits": {"north": "Church", "inside": "Reception"},

    "items": [],

    "enemies": [enemy_guard_outside],

    "people": []
}

#BUILDING FINAL

#from Items import *
#from enemies import *


room_reception = {
    "name": "Reception",

    "description":
    """You walk in from outside into *Building name*. To your west is what appears to
be a Meeting room. There are toilets to the south and stairs to your east. You approach
the receptionist and they ask for your ID card.""",

    "exits": {"east": "Stairs 0", "west": "Meeting Room", "south": "Toilet", "north": "Building2"},

    "items": [],

    "enemies" : [enemy_receptionist],

    "people": []
}
room_meeting = {
    "name": "Meeting Room",

    "description":
    """You are in the Meeting room. You see a computer at the back of the room, with a
card next to it. You wonder what the card is used for. The reception is to the east.""",

    "exits": {"east": "Reception"},

    "items": [], # items_visitors_pass

    "enemies" : [],

    "people": []
}
room_toilet = {
    "name": "Toilet",

    "description":
    """You are standing in the toilets and decide to search around to try and find
something useful. You begin searching when you find a someone unconscious. The reception
is to the north.""",

    "exits": {"north": "Reception"},

    "items": [items_pistol, items_intelligence_book], # The ammunition and a pistol would be dropped when the player kills the enemy.
 
    "enemies" : [enemy_guard_toilet],

    "people": []
}
room_stairs_0 = {
    "name": "Stairs Ground Floor",

    "description":
    """You are standing on the stairs, you see a book on the floor. Going up the
stairs will take you to the 1st Floor.""",

    "exits": {"up": "Corridor", "west": "Reception"},

    "items": [items_agility_book],

    "enemies" : [],

    "people": []
}

room_corridor = {
    "name": "Corridor",

    "description":
    """You are standing in the corridor on the 1st Floor. There is a guard waiting for you.
You see there are rooms to your south and west.""",

    "exits": {"south": "Room 2", "east": "Stairs 1", "west": "Room 1", "down": "Stairs 0"},

    "items": [], # Guard drops this item (items_b2_keycard)

    "enemies" : [enemy_guard_floor1],

    "people": []
}
room_room1 = {
    "name": "Storage room",

    "description":
    """You are standing in the storage room, you see a pistol and a Garotte wire. The corridor is
to the east.""",

    "exits": {"east": "Corridor"},

    "items": [items_pistol],

    "enemies" : [],

    "people": []
}
room_room2 = {
    "name": "Kitchen",

    "description":
    """You are standing in the kitchen, you see a box on the floor and wonder what is inside.
To your north is the corrirdor.""",

    "exits": {"north": "Corridor"},

    "items": [items_first_aid_box, items_intelligence_book],

    "enemies" : [],

    "people": []
}
room_stairs_1 = {
    "name": "Stairs 1st Floor",

    "description":
    """You are standing on the stairson the 1st Floor. Going up the
stairs will take you to the 2nd Floor. """,

    "exits": {"up": "Main Room", "east": "Corridor"},

    "items": [],

    "enemies" : [],
    
    "people": []
}

room_main = {
    "name": "Secretary office",

    "description":
    """You walk in from stairs and see a Guard sitting on a sofa. He hasn't seen you.
If you go south you can go to the conference, north to the security room or west to the
elevator""",

    "exits": {"down": "Stairs 1", "south": "Conference Room", "west": "Elevator", "north": "Security Room"},

    "items": [],
 
    "enemies" : [],

    "people": []
    }
room_security = {
    "name": "Security Room",

    "description":
    """You are in the security room. There is a guard here. The Main room is to the east.""",

    "exits": {"east": "Main Room"},

    "items": [], # They will drop if the kill the enemy.

    "enemies" : [enemy_guard_security],

    "people": []
}
room_conference = {
    "name": "Conference Room",

    "description":
    """You walk into the Conference room. You see a book on the table. You open the book and you find a pin code for the elevator '179535'""",

    "exits": {"north": "Main Room"},

    "items": [],

    "enemies" : [],

    "people": []
}
room_elevator = {
    "name": "Elevator",

    "description":
    """You press the button on the elevator. It opens, you enter, but it needs a code.
The main room is to the east""",

    "exits": {"east": "Main Room", "up": "Main Office"}, # Players will use pin_execute function here which will teleport the player into main office.

    "items": [items_strength_book],

    "enemies" : [],

    "people": [],
    
    "allowed": False
}

room_main_office = {
    "name": "Main Office",

    "description":
    """You walk out of the elevator into the the Main Office. You see the BOSS 
(The man who gave the order for the building you were trapped earliear at, to be bombed) and
wonder how you are going to kill him and get Serum 207""",

    "exits": {},
    
    "items": [items_serum_207], # Boss will drop this item.

    "enemies" : [enemy_BIGBOSS],

    "people": []
}


####END


rooms = {
#basement
    "Cell1": cell_room,
    "Securityroom1": security_room,
    "Stairsone1": staircase_1,

    #ground floor
    "Stairstwo1": staircase_2,
    "Reception1": reception_room,

    #first floor
    "Stairsthree1": staircase_3,
    "Lobby1": lobby_room,
    "Control1": control_room,

    #roof
    "Roof1": roof_floor,

## STREET MAP
    "Building1": place_building_one,
    "Abandoned": place_abandoned_building,
    "Garden": place_garden,
    "Pharmacy": place_pharmacy,
    "Toys": place_toys_shop,
    "Station1": place_train_station_one,
    "Station2": place_train_station_two,
    "Centre": place_city_centre,
    "Parking": place_parking,
    "Church": place_church,
    "Building2": place_final_building,

##BUILDING 2
    "Reception": room_reception,
    "Meeting Room": room_meeting,
    "Toilet": room_toilet,
    "Stairs 0": room_stairs_0,
    "Corridor": room_corridor,
    "Room 1": room_room1,
    "Room 2": room_room2,
    "Stairs 1": room_stairs_1,
    "Main Room": room_main,
    "Security Room": room_security,
    "Conference Room": room_conference,
    "Elevator": room_elevator,
    "Main Office": room_main_office
}


## ADD DESCRIPTIONS, SEARCH
