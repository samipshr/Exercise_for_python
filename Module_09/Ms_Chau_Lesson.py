class ShoppingList:

    def __init__(self):
        self.items =[]

    def add_item(self, item: str):
        if not item in self.items:
            self.items.append(item)

    def print_list(self):
        for item in sorted(self.items):
            print(item)

    def longest_name(self):
        helper1=""
        helper2=0
        for item in self.items:
            if len(item) > helper2:
                helper2=len(item)
                helper1=item
        return helper1
   

veget = ShoppingList()
veget.add_item("tomato")
veget.add_item("spaghetti")
veget.add_item("paramesan")
veget.print_list()
print(f"The item with the longest name is:{veget.longest_name()}")