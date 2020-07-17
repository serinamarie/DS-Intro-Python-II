class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, name):
        print(f"\nYou have picked up a {self.name}! {self.description}")

    def on_drop(self, name):
        print(f"\nYou have dropped a {self.name}. Hope you didn't need that.")