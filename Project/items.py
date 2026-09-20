class Item:
    def __init__(self, name, weight, description):
        self.name = name
        self.weight = weight
        self.description = description
    def add_item(self):
        item = input("What item do you want to add to your bag? ")
        self.inventory.append(item)
        print(f"{item} has been added to your bag.")
    def show_items(self):
        print("You look inside your bag...")
        for item in self.inventory:
            print(f"- {item}")

    