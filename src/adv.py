from room import Room
from player import Player
from item import Item, LightSource

# Declare all the items

item = {
    'armor': Item("armor",
                        "You're either very safe now or just very warm. Likely both."),
    'bat': Item("bat",
                "You are now infected with coronavirus. Best hurry now."),
    'candelabrum': LightSource("candelabrum",
                        "Your way is illuminated, young luminary."),
    'lamp': LightSource('lamp',
                        "The better to see all the cobwebs with.")
    }


# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", 
                    """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", 
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", 
                    """The narrow passage bends here from west to north. The smell of gold permeates 
                    the air."""),

    'treasure': Room("Treasure Chamber", 
                    """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
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
room['narrow'].items = ['bat', 'lamp']

room['foyer'].is_light = True
room['overlook'].is_light = True 
room['outside'].is_light = True


# Make a new player object that is currently in the 'outside' room.
player_1 = Player(name='Serina', current_room=room['outside'])

direction = None

intro = ("\nHello stranger. Good luck finding my treasure!")

print(intro)

what_to_do = ('\nTry and pick up or drop an item if you like by typing in [get item] or [drop item].',
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
                                f'{player_1.current_room.description}.')

    print('\n'.join(room_description_and_items))

    # If there are items in the current room, let the player know
    if player_1.current_room.items:
        print(f'The {player_1.current_room.name} contains these items: {player_1.current_room.items}')
    else:
        print("This room contains no objects to pick up.")

    # See if the current room is lit for the player or player has a lightsource item
    if player_1.current_room.is_light == False and isinstance(player_1.items, LightSource) == False:
        print("It's pitch black! Scared yet?")

    # Waits for user input and decides what to do.
    command = input('\n'.join(what_to_do))
    
    # Assess input length to see if player wants to move or do an item-related task
    if len(command.split(" ")) == 1:

        if command == 'i':
            if player_1.items:
                print(f"Inventory: {player_1.items}")
            else:
                print("Your pockets are turned out. A fly buzzes away into the darkness.")
            

        # If the user enters a cardinal direction, attempt to move to the room there.
        else:
            try:
                player_1.move(command)
            except:
                "Unknown error occurred"

    # If player wants to do something with an item
    elif len(command.split(" ")) == 2:

        #Split item-related command
        verb_object = command.split(" ")

        verb = verb_object[0]

        obj = verb_object[1]

        # If the user enters 'drop' followed by an item name
        if verb.lower() == 'drop':

            # Look at the inventory of the current player to see if the item is there
            if obj.lower() in player_1.items:

                # Since it is, remove item from player
                player_1.drop(obj)
                
                # And put it in the room
                player_1.current_room.add(obj)

                # Let the player know they have dropped the item
                item[obj].on_drop(obj)

        # If the user enters 'get' or 'take' followed by an item name
        elif verb.lower() == 'get' or 'take':

            # Look at the contents of the current room to see if the item is there
            if obj.lower() in player_1.current_room.items:

                # Since it is, remove item from room
                player_1.current_room.drop(obj)

                # And add the item to the player
                player_1.add(obj)

                # Let the player know they have picked up the item
                item[obj].on_take(obj)

            # If the item is not in the room
            else: 
                print("That is not a valid entry!")





    
        
