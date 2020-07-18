# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
from player import Player

class Room:
    n_to = None
    s_to = None
    e_to = None
    w_to = None
    is_light = False
    items = []
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def drop(self, item):
        self.items.remove(item)
    
    def add(self, item):
        self.items.append(item)

    def __str__(self):
        return f'Room items: {self.items}'




if __name__ == '__main__':

    # Declare all the items

    item = {
    'candelabrum': Item("Candelabrum",
                        "Your way is illuminated, young luminary."),
    'bat': Item("Bat",
                "You have been infected with coronavirus.")
}
    
    room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



    # Link rooms together

    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

    # Place items in rooms
    room['foyer'].items = ['candelabrum']
    room['narrow'].items = ['bat']

    player_1 = Player(name='Serina', current_room=room['foyer'])

    print("Items in current room:", player_1.current_room.items)

    print("C put in room", player_1.current_room.drop('candelabrum'))
    print("Add c to player:", player_1.add('candelabrum'))

    print("No items in current room:", player_1.current_room.items)

    player_1.current_room.add('bat')
    print("Bat added to room:", player_1.current_room.items)
    player_1.current_room.drop("bat")
    player_1.add('bat')
    print("Player has bat:", player_1.items)
    print(player_1.current_room.is_light)

    

    if player_1.current_room.is_light == False and isinstance(player_1.items, LightSource) == False:
    
