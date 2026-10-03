#Game
#project-04: Organize the Structure and Introduce

from pathlib import Path
from player import Player
from room import Room
from items import Item
from save import save_game, load_game, delete_save

path = Path(__file__).parent
SAVE = path/"saves"

def read_file(filename):
    try:
        with open(path / filename, "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"{filename} not found in {path}")

print("\n\n")
read_file("intro.txt")
print("\n\n")
read_file("instructions.txt")
print("\n\n")

cabin = Room("Cabin")
outside = Room("Outside")
north = Room("North")
west = Room("West")
east = Room("East")
south = Room("South")
stuff = []
book = Item(
    "Book",
    "- It's cover is White in the front and black in the back, gilded with a golden vine pattern."\
    "it won't open"
    )
fish = Item(
    "Fish",
    "- A freshly caught fish from the river. MUFU would probably love it.")
trinket = Item(
    "Trinket",
    "- A small oval jewelry with an word carved into it. You cannot understand it")
ichor = Item(
   "Strange Fruit",
   "- It seems to reflect a golden surface, maybe metallic? \nbut upon closer inspection you can see it is transparent")
candle = Item(
   "candle",
   "- It is a stange candle, spiraling like a snake. Creepy...")

rooms = {r.name: r for r in [cabin, outside, north, west, east, south]}
items = {i.name.lower(): i for i in [book, fish, trinket, ichor, candle]}

cabin.item = book
outside.item = fish
east.item = trinket
west.item = ichor

print("Hello Player.")
name = input("Enter your name: ")
player = None
stuff = []
loaded = load_game(name, rooms, items)
if loaded and input("Saved game found. Continue? (y/n): ").lower() == "y":
    player, age, stuff, bucket_list = loaded
    print(f"Welcome back, {name}...")
else:
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a number.")
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
        print("give - give away an item")
        print("pray - perform the ritual")
        print("help - shows the instruction.txt file again")
        print("save - saves the game progress")
        
        print("lopeta - QUIT GAME")
        command = input("- Enter a command: ").lower()
        print("\n")
        if command == "lopeta":
            print("until next time.")
            break

        elif command == "look":
            print(f"You are in the {player.location.name}.")
            if player.location == cabin:
                if cabin.times_entered == 0:
                 print("you look around, your eyes feeling heavy and find yourself in the cabin.")
                 print("seems like you were out cold after staying up all night,")
                 print("quite the experience for your first time camping.")
                 print("beside you, your black cat MUFU is sleeping with a noticeably large belly")
                 print(f"{name} - 'this fur ball ate too much fish yesterday...'")
                 print(f"{name} - 'well i suppose i kinda went over my limit as well'")
                else:
                 print("This room has changed, its different.")
                 print("MUFU is still there, now sitting on the chair.")
                 print("Waiting for you to come back patiently.") 
                 print("No, its just her hollow husk.")   

            elif player.location == outside:
                if outside.times_entered == 0:
                 print("the first thing you see is a luscious forest that should be full of life,")
                 print("but you only find silence in this place covered by a gray sky.")
                 print("You see flowers and a... and a barrel?")
                else:
                 print("Outside the cabin, there's now a bonfire in the dark,")
                 print("Burning bright, it gives you warmth and comfort.")
                 print("The layout has changed.")
                 print("The sky is no longer gray but covered with a cloudy band of stars,")
                 print("You sit near the fire and enjoy the moment.")
                
            elif player.location == north:
                if north.times_entered == 1:
                 print("It is dark.")
                 print("... its snowing ...")
                 print(f"{name} - am i... dreaming? No... i can feel the cold.")
                 print(f"{name} - whats happening?...")
                 print(f"??? - oh if it isn't {name}.")
                 print(f"A tall figure stands beside you. Looking down at you")
                 print(f"{name} - oh hi, got anything to keep warm?")
                 print("You ask him as you start to shiver in the cold")
                 print(f"??? - hmm go east, you'll find what you need...")
                 print("         ___CLUE__OBTAINED___")
                 print("Please check your list")
                 bucket_list.append("go get the item form the east")
                elif north.times_entered >= 1 and any(item == trinket for item in player.inventory):
                  north.item = candle
                  print("You don't feel the cold now,")
                  print("as you walk further from your last visit, you see an inhuman staue.")
                  print("It is a surprisingly detailed figure of a creature that seems to have a human face but a snakes body.")
                  print("You feel as though you need to leave, this place just doesn't feel right.")                 
                else: 
                 if north.times_entered >=2:
                  print("It's cold here, best return after you prepare yourself")

            elif player.location == east:
               if east.times_entered == 1:
                 print("You walk from a green Flora into a warm golden forest.")
                 print("It's like the season of autumn is back again out of nowhere")
                 print("But it doesn't surprise you")
                 print(f"{name} - Hm, seems like a nice place to relax")
               elif east.times_entered >= 2:
                 print("The cool breeze with a warm sun")
                 print("you take a seat on a flat rock, and relax")
            elif player.location == west:
              if west.times_entered == 1:
                 print("A vast plain and humid land with colourful dots all around, best way to describe this place.")
                 print("It's covered with unripe berries, too sour to eat right now.")
                 print("However there's something usual about this place,")
                 print("There is a tree with no leaves, its bark completely white")
                 print("And a couple of dark fruits hanging from it.")
                 print("??? - You may take one...")
              elif west.times_entered >= 2:
                 print("This land has changes, no berries remain on these plains and the tree is also gone,")
                 print("Its now replaced by a gray flat desert, with no sign of life on sight.")
            elif player.location == south:
              if south.times_entered == 1:
                print("A large temple of glass sits ahead of you, an altewr in the middle.")
                print("With nothing but a white plain that stretches beyong the horizon, 'IT' waits")
              elif south.times_entered >= 2:
                print("'IT' is still there.")
                print("Make your choice.")

            if player.location.item is not None:
                print(f"You see a {player.location.item.name}.")

        elif command == "move":
            if player.location == cabin:
               player.move(outside)
               print("\nYou are now outside the cabin.")
               print("You can go:")
               print("- north")
               print("- west")
               print("- east")
               print("- cabin")
               print("- south")
            elif player.location == outside:
               print("\nWhich direction do you want to go?")
               print("- north")
               print("- west")
               print("- east")
               print("- cabin")
               print("- south")
               direction = input("Choose a direction: ").lower()
               if direction == "north":
                player.move(north)
                north.times_entered += 1
               elif direction == "west":
                player.move(west)
                west.times_entered += 1
               elif direction == "east":
                player.move(east)
                east.times_entered += 1
               elif direction == "cabin":
                player.move(cabin)
                cabin.times_entered += 1
               elif direction == "south":
                player.move(south)
                south.times_entered += 1
               else:
                print("Unknown direction.")
            else:
             print("\nWhich direction do you want to go?")
             print("- back")
             direction = input("Choose a direction: ").lower()
             if direction == "back":
              player.move(outside)
             else:
              print("You can't go that way.")

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
            print(f"{name} - 'Ughh did i really write this?")
            print(f"it sounds so cringe... ")
            print(f"{name} -...")
            print("you say that, yet there's joyous smile on your face")
            print(f"{name} - 'well at least i did do one out of these three yesterday.'")

        elif command == "help":
            print("\n")
            read_file("instructions.txt")

        elif command == "save":
            save_game(player, name, age, stuff, bucket_list, rooms)       

        elif command == "give":
            if player.location != south:
              print("You shouldn't give away carelessly.")
            elif player.location == south:
             player.show_items()
             if len(player.inventory) > 0:
                item_name = input("Which item do you want to give to the deity? ")
                found = False
                for item in player.inventory:
                    if item.name.lower() == item_name.lower():
                        print("You approach the altar.")
                        print(f"You place the {item.name} on the altar.")
                        print("'IT' slowly reaches toward it.")
                        print("The item disappears.")
                        player.inventory.remove(item)
                        stuff.append(item)
                        found = True                        
                        break
                    if not found:
                     print("'IT' looks at you as you search for something that doesn't exist.")
                else:
                 print("'IT'is unmoved.")

        elif command =="pray":
          if player.location != south:
            print("You cannot pray here.")
          elif player.location == south:          
             offer = {item.name.lower() for item in stuff}
             print("\nYou kneel before IT...")
             if {"book", "trinket", "fish", "strange fruit", "candle"} <= offer:
               print("IT accepts your offerings."\
                     "\nThe glass temple begins to glow in all colours."\
                     "\nYou feel a strange warmth surrounding you.")
             elif {"book", "trinket", "fish", "strange fruit"} <= offer:
               print(f"IT stares at the items."\
                     "\nYou realize that something was left behind.")
             elif {"book", "trinket", "fish"} <= offer:
               print("IT looks at the trinket."\
                     "\nThe deity remains silent.")
             elif {"book", "trinket"} <= offer:
               print("something of mundane life")
             elif {"book"} <= offer:
               print("a quitet one")
             elif {""} <= offer:
               print("last?")
             else:
               print("IT does not respond.")
               print("The white plain remains completely silent.")
             print("\n___THE END___")
             break

        else:
            print("UNKNOWN COMMAND - Try Again with given commands")
