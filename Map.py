#places

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

    "items": []
    
#name of the street, a street id, items in the streets, a
#description of the street
#and all of the exits from this street to the others
}

place_abandoned_building = {
    "name": "the abandoned building",

    "description":
    """You have entered the abandoned building. There seems to be nothing
useful when you first entered. After researching around,
you see an intelligence skillbook and a knife on the floor.
You can either pick up the items or leave the building from the south side.""",

    "exits": {"south": "Pharmacy"},

    "items":[]
##knife, int skillbook
}

place_garden = {
    "name": "the garden",

    "description":
    """You have entered the city garden. It is a very large garden with
variety of flowers, trees and fields. There are also a lot of benches and
historical statues. This garden leads to the train station. You see a strenght
skillbook on the floor. You can pick it up, or go south to the train station.""",

    "exits": {"south": "Station1"},

    "items": []
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

    "items": []
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

    "items": []
##str skillbook
}

place_train_station_one = {
    "name": "the NORTH train station",

    "description":
    """You are at the NORTH train station. The next train is already loading and leading
to the south station. You can either find a ticket to get on the train and go south
or you can go back to the garden from the north exit.""",

    "exits": {"north": "Garden", "south": "Station2"},

    "items": []
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

    "exits": {"north": "Station1", "west": "Centre", "east": "Parking"},

    "items": []
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

    "items": []
##nothing
}

place_parking = {
    "name": "the train station parking",

    "description":
    """You have come to the train station parking. It is almost full but you don't see
nobody around. It is very quiet. You can only see an agility skillbook next to the barrier at
the parking entrance. You can pick it up, or go back to the train station from the west exit. """,

    "exits": {"west": "Station2"},

    "items": []
##agi skillbook
}

place_church = {
    "name": "the church",

    "description":
    """You are currently in the church area. It is a very quiet area. It is not very busy at
the moment. There is an intelligence skill book at the entrance of the church. You can pick it up,
go north back to the city centre or you can continue south and go in front of the final building.""",

    "exits": {"north": "Centre", "south": "Building2"},

    "items": []
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

    "exits": {"north": "Church"},

    "items": []
}



rooms = {
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
}
