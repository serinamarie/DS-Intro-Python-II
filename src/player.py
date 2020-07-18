
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    items = []

    def __init__(self, name, current_room, direction=None):
        self.name = name
        self.current_room = current_room
        self.direction = direction

    def add(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def inventory(self, inv):
        i

    def move(self, direction):

        congratulatory_message = ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "You're getting closer to the treasure! Or maybe further away. Don't get lost now :)",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        if direction == 'n':
            if self.current_room.n_to == None:
                error_message = ("-------------------------------------------------------------",
                "Wrong way, cowboy. You can't go north here.",
                "Try a new direction!",
                "-------------------------------------------------------------\n")
                print('\n'.join(error_message))
            else:
                self.current_room = self.current_room.n_to
        
        elif direction == 's':
            if not self.current_room.s_to:
                error_message = ("-------------------------------------------------------------",
                "Uh oh. There's no way to go south here so keep your pants on.",
                "Try a new direction!",
                "-------------------------------------------------------------\n")
                print('\n'.join(error_message))
            else:
                self.current_room = self.current_room.s_to
                print('\n'.join(congratulatory_message))
        
        elif direction == 'e':
            if not self.current_room.e_to:
                error_message = ("-------------------------------------------------------------", 
                "East, you say? You sure know how to walk into a wall.",
                "Try a new direction once your headache wears off.",
                "-------------------------------------------------------------\n")
                print('\n'.join(error_message))
            else:
                self.current_room = self.current_room.e_to
                print('\n'.join(congratulatory_message))
        
        elif direction == 'w':
            if self.current_room.w_to == None:
                error_message = ("-------------------------------------------------------------",
                "Going west? You're the best. Just not at this game. Hm. I have to say I expected more.",
                "-------------------------------------------------------------\n")
                print('\n'.join(error_message))
            else:
                self.current_room = self.current_room.w_to
                print('\n'.join(congratulatory_message))
        else:
            # Print an error message if the movement isn't allowed.
            error_message = ("\nWho do you think you are? A bishop or a knight who can move diagonally or in an L?",
                "You are but only a pawn. Choose a cardinal direction.")
            print('\n'.join(error_message))

if __name__ == "__main__": 
    player_1 = Player(name='Serina', current_room='outside')
    print(player_1.move('n'))
 