from items import *


#Basement(rooms)
cell_room = {
    
    "name": "Agent 21s cell",
    
    "description": 
    """
    You have been in this cell for weeks. Behind the cell doors
    you will find the security room. The cell doors are facing north.""",

    "exits": {"north":"Securityroom"},

    "furniture": {"bed":[items_hair_pin]},

    "items":[],

    "enenmies":[]
}

security_room = {
    
    "name": "Security room",

    "description":
    """ 
    The staircase is to the west of the security room. But, you better
    check this room carefully, there could be useful items here.""",

    "exits": {"south": "Cell", "west": "Stairsone"},

    "furniture": {"desk": [items_b1_keycard]},

    "items":[items_security_baton],

    "enenmies":[]

}

staircase_1 = {
    
    "name": "Basement staircase",

    "description":
    """ 
    This seems to be the only way to get to the floor above. 
    Go up to enter the ground floor. """,

    "exits": {"up":"Stairstwo", "east": "Securityroom"},

    "furniture":[],

    "items":[],

    "enenmies":[]
}


#Ground floor(rooms)
staircase_2 = {
    
    "name": "Ground floor staircase",

    "description":
    """ 
    Going down will bring you to the basement floor.
    going up will bring you to the first floor. """,

    "exits": {"up":"Stairsthree", "down": "Stairsone" , "east": "Reception"},

    "furniture":[],

    "items":[],

    "enenmies": []
}

reception_room = {
    
    "name": "Reception",

    "description":
    """ 
    This is the reception room. The entrance to the building is north.
    However, you will need promision from the control room. To get back to the 
    staircase go west.""",

    "exits": {"north": "Building1", "west":"Stairstwo"},

    "furniture":{"table":[items_strength_book]}, 

    "items": [],

    "enenmies": []
}

#First floor(rooms)
staircase_3 = {
    
    "name": "First floor stairs",

    "description":
    """
    Going down will bring you back to the ground floor.
    Going up will bring you to the roof.""",

    "exits": {"up": "Roof", "down": "Stairstwo", "east": "Lobby"},

    "furniture":[],

    "items":[],

    "enenmies": []
}

lobby_room = {
    
    "name": "The lobby",

    "description":
    """ 
    You are at the lobby on floor one. To enter the control room go south.
    To get back to the staircase go west.""",

    "exits": {"west":"Stairsthree", "south": "Control"},

    "furniture": {"sofa":[]},

    "items":[],

    "enenmies": []
}

control_room = {
    
    "name": "Control room",

    "description":
    """
    This is the control room. You are able to unlock the main doors from here.
    To go back to the lobby go north.""",

    "exits": {"north": "Lobby"},

    "furniture":[],

    "items":[],

    "enenmies": []
}



#Roof
roof_floor = {
    
    "name":"Building one Roof",

    "description":
    """ 
    You are on the roof. Its too high to jump down. 
    To go back to the first floor go down.""",

    "exits": {"down": "Stairsthree", "north": "Building1"},

    "furniture":[],

    "items":[items_rope],

    "enenmies": []

}

#Building One
building_one = {

    #basement
    "Cell": cell_room,
    "Securityroom": security_room,
    "Stairsone": staircase_1,

    #ground floor
    "Stairstwo": staircase_2,
    "Reception": reception_room,

    #first floor
    "Stairsthree": staircase_3,
    "Lobby": lobby_room,
    "Control": control_room,

    #roof
    "Roof": roof_floor


}
