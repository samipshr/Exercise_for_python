class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def add_item(self):
        item = input("What item do you want to add to your bag? ")
        self.inventory.append(item)
        print(f"{item} has been added to your bag.")
