#Game
#project-01 : program that asks for the player’s name and age, stores them in variables, and prints them to the console.
print("Hello Player.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"player name: {name}")
print(f"player age: {age}")

#project-02 & 03 modified: 
if age < 12:
    print("You are a minor. Game is shutting down")
else:
    print("Welcome to the game...")

    inventory = ["1€", "phone case"]

    bucket_list = [
        "Enjoy the Trip",
        "catch your first fish",
        "Have Fun (very important!)"
    ]

    # TO look around
    def look():
        print("you look around, your eyes feeling heavy and find yourself in the cabin.")
        print("seems like you were out cold after statyig up all night,")
        print("quite the experience for your first time camping.")
        print("beside you, your black cat MUFU is sleeping with a noticeably large belly")
        print(f"{name}- 'this fur ball ate too much fish yesterday...'")
        print(f"{name}- 'well i suppose i kinda went over my limit as well'")

    # add items to Inventory
    def add_item():
        item = input("What item do you want to add to your bag? ")
        inventory.append(item)
        print(f"{item} has been added to your bag.")

    # to show the inventory
    def show_items():
        print("You look inside your bag...")
        
        for item in inventory:
            print(f"- {item}")

        print("It seems you left your phone outside, hope MUFU didn't scratch it or anything...")

    # the bucket list
    def show_bucket_list():
        print("You take out a small piece of paper, few words are written in it:")

        for item in bucket_list:
            print(f"- {item}")

        print(f"{name}- 'God did i really write this? it sounds so cringe... '")
        print(f"{name}-...")
        print(f"{name}- 'well at least i did do one of these three yesterday.'")


    while True:
        print("\n___MAIN MENU___")
        print("command options:")
        print("look - observe surrounding")
        print("item - check items in bag")
        print("add - add an item to bag")
        print("list - check bucket list")
        print("lopeta - QUIT GAME")

        command = input("- Enter a command: ")
        print("\n")

        if command == "lopeta":
            print("until next time.")
            break

        elif command == "look":
            look()

        elif command == "item":
            show_items()

        elif command == "add":
            add_item()

        elif command == "list":
            show_bucket_list()

        else:
            print("UNKNOWN COMMAND - Try Again with given commands") 
