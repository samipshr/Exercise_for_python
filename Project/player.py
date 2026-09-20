class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.inventory = []
        self.location = location
    def move(self, new_location):
        self.location = new_location
        print(f"You moved to the {self.location.name}.")
    def collect_item(self):
        if self.location.item is not None:
            item = self.location.item
            self.inventory.append(item)
            self.location.item = None
            print(f"{item.name} has been added to your bag.")
        else:
            print("There is no item here.")
    def show_items(self):
        print("You look inside your bag...")
        if len(self.inventory) == 0:
            print("Your bag is empty.")
        else:
            for item in self.inventory:
                print(f"-{item.name}")
    def inspect_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
             print(f"\n{item.name}")
             print(f"Description: {item.description}")
             print(f"Weight: {item.weight} kg")
             return
    print("You don't have that item.")