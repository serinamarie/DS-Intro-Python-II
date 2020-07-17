from room import Room
from player import Player
from item import Item
import sys

# Declare all the items

item = {
    'candelabrum': Item("candelabrum",
                        "Your way is illuminated, young luminary."),
    'bat': Item("bat",
                "You have been infected with coronavirus.")
}

# Declare all the rooms

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
room['foyer'].items = item['candelabrum']
room['narrow'].items = item['bat']


# Make a new player object that is currently in the 'outside' room.
player_1 = Player(name='Serina', current_room=room['outside'])

direction = None

intro = ("\nHello stranger. Good luck finding my treasure!")

print(intro)

what_to_do = ('\nTry and pick up an item if you like by typing in [get item].',
 'For example, [get apple] would attempt to pick up an apple if it was in this room.',
 '\nOtherwise, choose a direction to travel in order to find the treasure.', 
f'But beware, there are many wrong paths to take:\n'
'[n] North  [s] South  [e] East  [w] West  [i] Inventory [q] Quit\n')

# Write a loop that:

# If the user enters "q", quit the game.
while not direction == 'q': 

    # Prints the current room name. 
    # Prints the current description (the textwrap module might be useful here).
    room_description_and_items = (f'\nYou are in the {player_1.current_room.name}.',
                                f'{player_1.current_room.description}.',
                                f"Items you posess: {player_1.items}")

    print('\n'.join(room_description_and_items))

    if player_1.current_room.items:
        print(f'The {player_1.current_room.name} contains these items: {player_1.current_room.items.name}')
    else:
        pass

    # Waits for user input and decides what to do.
    command = input('\n'.join(what_to_do))
    
    # Assess input length to see if direction or item-related
    if len(command.split(" ")) == 1:

        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        player_1.move(command)

    elif len(command.split(" ")) == 2:

        #Split item-related command
        verb_object = command.split(" ")

        # If the user enters get or take followed by an Item name, 
        if verb_object[0].lower() == 'get' or 'take':
            print(verb_object[0], verb_object[1])

            # Look at the contents of the current Room to see if the item is there
            if verb_object[1] in player_1.current_room.items.name:

                player_1.current_room.remove(verb_object[1])
                player_1.add(verb_object[1])


            else: 
                print("That item isn't in this room. Wish all you want!")
        else:
            print("Not a valid verb to pick up object")

        # If the user enters get or take followed by an Item name, 
        if verb_object[0].lower() == 'drop':

            # Look at the contents of the current Room to see if the item is there.
            item = verb_object[1]

            if item.lower() in player_1.items:

                player_1.remove(item)
                player_1.add(item)
                player_1.on_take(item)
                

            else: 
                print("That item isn't in this room. Wish all you want!")

                




    
        
