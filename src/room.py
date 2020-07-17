# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    n_to = None
    s_to = None
    e_to = None
    w_to = None
    items = None
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def remove(self, item):
        self.items.remove(item)
    
    def add(self, item):
        self.items.add(item)

    def __str__(self):
        return f'Room items: {self.items}'




if __name__ == '__main__':
    
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

# Declare all the items

item = {
    'candelabrum': Item("Candelabrum",
                        "Your way is illuminated, young luminary."),
    'bat': Item("Bat",
                "You have been infected with coronavirus.")
}
