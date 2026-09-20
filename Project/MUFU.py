#Game
#project-01 : program that asks for the player’s name and age, stores them in variables, and prints them to the console.

from player import Player
from room import Room
from items import Item

cabin = Room("Cabin")
outside = Room("Outside")
north = Room("North")
west = Room("West")
east = Room("East")
back_of_cabin = Room("Back of Cabin")

phone = Item(
    "phone",
    0.2,
    "Your phone. You seem to have left it outside.")
fish = Item(
    "fish",
    0.5,
    "A freshly caught fish from the river. MUFU would probably love it.")

cabin.item = phone
outside.item = fish

print("Hello Player.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"player name: {name}")
print(f"player age: {age}")
if age < 12:
    print("You are a minor. Game is shutting down")
else:
    print("Welcome to the game...")
    player = Player(name, age, cabin)
    bucket_list = [
        "Enjoy the Trip",
        "catch your first fish",
        "Have Fun (very important!)"
    ]
    while True:
        print("\n___MAIN MENU___")
        print("command options:")
        print("look - observe surrounding")
        print("move - move to another room")
        print("collect - collect an item")
        print("item - inspect an item")
        print("list - check bucket list")
        print("lopeta - QUIT GAME")
        command = input("- Enter a command: ")
        print("\n")
        if command == "lopeta":
            print("until next time.")
            break
        elif command == "look":
            print(f"You are in the {player.location.name}.")
            if player.location == cabin:
               print("you look around, your eyes feeling heavy and find yourself in the cabin.")
               print("seems like you were out cold after statyig up all night,")
               print("quite the experience for your first time camping.")
               print("beside you, your black cat MUFU is sleeping with a noticeably large belly")
               print(f"{name}- 'this fur ball ate too much fish yesterday...'")
               print(f"{name}- 'well i suppose i kinda went over my limit as well'")
            elif player.location == outside:
                print("You are outside the cabin.")
                print("You see trees and a river nearby.")
            if player.location.item is not None:
                print(f"You see a {player.location.item.name}.")
        elif command == "move":
            if player.location == cabin:
                player.move(outside)
            else:
                player.move(cabin)
        elif command == "collect":
            player.collect_item()
        elif command == "item":
            player.show_items()
            if len(player.inventory) > 0:
                item_name = input("\nWhich item do you want to inspect? ")
                player.inspect_item(item_name)
        elif command == "list":
            print(f"You take out a small piece of paper,")
            print(f"few words are written in it:")
            for item in bucket_list:
                print(f"- {item}")
            print(f"{name}- 'Ughh did i really write this?")
            print(f"it sounds so cringe... ")
            print(f"{name}-...")
            print("you say that, yet there's joyous smile on your face")
            print(f"{name}- 'well at least i did do one out of these three yesterday.'")
        else:
            print("UNKNOWN COMMAND - Try Again with given commands")