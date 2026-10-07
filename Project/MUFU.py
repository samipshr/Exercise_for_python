#Game
#project-05: File handeling

from coin_flip import coin_flip
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

# Introduction and checking for previous saves.

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
    if player is None:
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
# Commands to execute and perform actions, some require the player to go through locations twice.
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
                 print("You don't want to stay here anymore.")   

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
                 if "go get the item from the east" not in bucket_list:
                    bucket_list.append("go get the item from the east")
                elif north.times_entered >= 2 and any(item == trinket for item in player.inventory):
                  have_it = candle in player.inventory or candle in stuff
                  if not have_it:
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
                print("\n")
                print(f"You see a {player.location.item.name}. (You may add it to your inventory)")

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
            print(f"hmm, i don't remember writing these.")
            print(f"{name} -...")
            print("you look at the note as a joyous smile forms on your face")
            print(f"{name} - 'well at least i did do one out of these, though i don't know when exactly.'")

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
                     "\nYou feel a strange warmth surrounding you."
                     "\n"
                     "\n   You wake up to a dim and cold room, held by gentle hands."
                     "\n New to this world, your first experience is of a warm embrace."
                     "\n Even in this cold dark place, you feel safe."
                     "\n"
                     "\n ... 15 years later ..."
                     "\n - you are a student in school, studying."
                     "\n - well... let's just say you aren't the sharpest tool in the shed,"
                     "\n   but you pull through with your efforts."
                     "\n - It was hard but you pass your classes and do rank quite high in class."
                     "\n   Because you spend most of your time putting in effort for your lack of smarts,"
                     "\n   your childhood went by quietly. Still you did make friends you could truly trust."
                     "\n"
                     "\n ... 7 years pass by ..."
                     "\n - You started working in a business, for the first few months you didn't really make much"
                     "\n   and your mother still had to go work to support the family."
                     "\n - Your relationship with her became quite distant even though you are her child,"
                     "\n   but you didn't care and loved her till the end."
                     "\n - After a few years though you did get a promotion, finally letting your mom take a rest after so long."
                     "\n - You start investing for your future and spend time with your mom."
                     "\n - Those moments, although they felt short were truly wonderful."
                     "\n"
                     "\n - ... 9 Years go by ..."
                     "\n - You retire from your job due to a severe illness and rest at home unable to do anything."
                     "\n - You sit in a chair under he porch and relax yourself, this life... although harsh was good."
                     "\n"
                     "\n"
                     "\n ......."
                     "\n [IT] - You were born to single mother at the bottom of this worlds hierarchy"
                     "\n [IT] - You did everything you could to make her proud... make her life better even if it was only by a bit."
                     "\n [IT] - Regardless you did fill her with pride, you lived a good life after all."
                     "\n [IT] - Starting at the bottom, though you didn't make it to the top, you were happy." \
                     "\n [IT] - You survived, grew old and found peace."
                     "\n [IT] - 'I' wonder what you will show me in your next story...")
             elif {"book", "trinket", "fish", "strange fruit"} <= offer:
               print(f"IT stares at the items."
                     "\nThe temple lets out a hazy purple mist as you are consumed by it."
                     "\n"
                     "\n        It's cold, your body is frail and weak wrapped in white cloth"
                     "\n - It gets warmer after a while but the first thing you felt was definitly that of a cold touch."
                     "\n - You find comfort in the warmth."
                     "\n"
                     "\n ... 22 years go by ..."
                     "\n - You did absolutely terrible in your academics, but since you were good with painting"
                     "\n   you were able to make a living with what you could earn. It was something new and you liked it."
                     "\n"
                     "\n ... 7 Years later ..."
                     "\n - You left your field of studies and started doing full time commisions on paintings."
                     "\n   At first you only did it to financially support yourself for a while but over time as you got better at it" 
                     "\n   you started to sell more and made a fortune on some of your pieces,"
                     "\n   but you can't keep doing these things forever. You wanted to discover yourself, experience the world."
                     "\n - So with the money you had collected over the years, you say your goodbyes to your parents and go"
                     "\n   on a journey around the world"
                     "\n"
                     "\n ... 12 years later ..."
                     "\n - 12 years. You travelled the world for 12 whole years,"
                     "\n   you made many friends, met many people, experienced the joys, the culture and the scenes that remain in your heart."
                     "\n - You have done so much yet you still desire to see more, but maybe it's time to take some rest."
                     "\n - You buy a small property in a frosty forest, you don't know why you really bought it,"
                     "\n   it's cold, you have to stuff yourself in layers of clothing to stay warm and you can't really talk with anyone else"
                     "\n   since you are alone out here."
                     "\n   Dispite all that, you like it here. It's quiet, theres might be no one to talk to but theres" 
                     "\n   also no one to judge you. A place where you can do whatever you want."
                     "\n - well, at least until you get another calling to do something new."
                     "\n"
                     "\n"
                     "\n [IT] - Oho, you were quite the passionate character in this story,"
                     "\n [IT] - Your drive to explore didn't really flourish among others, repeating and listening to words"
                     "\n        of the teachers were boring to you but yet you still pressed upon it for so long until,"
                     "\n        you tried something new, something different that you weren't really taught."
                     "\n [IT] - That sparked a flame in you that just kept buring till the end, unwavering and bright."
                     "\n [IT] - This wasn't the best story, a bit selfish but not bad.")
             elif {"book", "trinket", "fish"} <= offer:
               print("IT looks upon the skies."
                     "\nTrees of glass sprout from aroud the temple as it raises itself to the skies."
                     "\n"
                     "\n        You are falling"
                     "\n     but you don't feel fear"
                     "\n - You instinctively spread your wings and glide upon the eastern winds."
                     "\n - How do you know this? how did you know these winds were from the east? why did you not feel fear?"
                     "\n - Is it because you were just born? No, you don't even see the ones who created you, you are alone in the skies."
                     "\n   well, you don't have eyes to begin with. Your body is that of a bird without legs and made of paper."
                     "\n - Weak, fragile and incredibly fast. It would be wonderful to be able soar through the sky"
                     "\n   but when your body is made of paper its more of a curse than a blessing."
                     "\n - Nevertheless you fly and try to find clues to what you even are."
                     "\n   Maybe some kind of failed experiment that escaped its creator,"
                     "\n   or perhaps a piece of paper that gained sentience through some strong obsession?"
                     "\n"
                     "\n ...70 years later..."
                     "\n - You think to yourself, does if really matter if you find an answer to that question?"
                     "\n   70 years. You searched for 70 years to find even a clue of why you even exist."
                     "\n - Instead of this meaningless search you decide to find a way to get rid of this frail body of yours,"
                     "\n   so far in your long life you were able to glide the gentle winds and avoid harsh mountains and valleys."
                     "\n   But you have long grown tired of this, you want to soar across mountains and seas."
                     "\n - You wish you had a place to stay and think of how you could change your physical body however,"
                     "\n   being a bird with no legs with a body of paper, you can't just rest anywhere"
                     "\n - You start thiking of ideas on the go, for now this is all you can do"
                     "\n"
                     "\n ...200 years later..."
                     "\n - you are old and have seen many things, wars, disasters, revoloutions, the changing of seasons."
                     "\n   You too have grown not just in terms wisdom but also physically."
                     "\n - After so long you found that the properties of your body had changed to that of wood,"
                     "\n   you are now stronger, more durable and more importantly, you can now soar through the mountain and seas,"
                     "\n   through the valleys of the east and the peaks of the west"
                     "\n - You enjoy this new found freedom but curiosity pulls you to be more."
                     "\n"
                     "\n ... 600 years later ..."
                     "\n - These past 600 years... were not kind to you."
                     "\n   On your journey to strengthen yourself, you were burned by the sun,"
                     "\n   that itself was not the problem, you flew too close to the giant ball of flame. It was your mistake."
                     "\n - The real problem was the fact that you couldn't fly because now you were a bird made of charcoal."
                     "\n   This was worse than having a paper body, you couldn't do the one thing you were capable of doing"
                     "\n   and now here you were on the ground, burned, scared and far from the skies."
                     "\n - But you wouldn't give up, so what if were burned? so what if you can't fly now?"
                     "\n   You will figure something out, eventually."
                     "\n"
                     "\n ...2000 years later..."
                     "\n - A buring star flies through the night sky."
                     "\n   Its figure magnificent and its wings reaching the horizon."
                     "\n - You had found the way to fly 1900 years ago, you had to burn yourself."
                     "\n   It was a completely irrational decision, a painful one at that,"
                     "\n   but pain can eventually pass away unlike regret that will eat away your heart."
                     "\n - It hurt you more than anything in your life but you couldn't imagine spending the rest of your life"
                     "\n   as a flightless bird who would turn to nutrients for the plants."
                     "\n - So you burned and took that gamble, and went for it."
                     "\n   regardless, you survived and thrived. The first 900 years were hard to get used to,"
                     "\n   you were not exactly a pheonix after all."
                     "\n - After another 1000 years, those flames were finally starting to be cleansed."
                     "\n   And underneath those flames hid a transparent bird made of thousands of strands of clear glass,"
                     "\n   each represented a moment when you were about to give up, and everytime you refused such an outcome"
                     "\n   another new strand of glass was added."
                     "\n - Now you soar through skies, from the mountains to the seas and eventually along the golden breeze"
                     "\n - All that was left to see was the ball of fire in the sky, it blinded whoever daring to stare at it."
                     "\n   Not you though, you fell to it once now never again."
                     "\n   This time you will go beyond it and reach even higher skies."
                     "\n - So you moved your wings and aimed beyond the burning ring of flame."
                     "\n"
                     "\n"
                     "\n [IT] - What a long you had..."
                     "\n [IT] - and what a beautiful dream you had achieved."
                     "\n [IT] - It was truly a wonderful tale...")
             elif {"book", "trinket"} <= offer:
               print(f"IT looks at you"
                     "\n you are pulled away by ribbons of crimson red."
                     "\n"
                     "\n   you wake up as a red fish"
                     "\n You are with your sibilings, numbering in the thousands,"
                     "\n You don't have a sense of time but your instincts tell you to rush through the river."
                     "\n - You swim as fast as you can, rushing through the waters and take a leap though the air."
                     "\n   However instead of landing back in water, you are grabbed by an Giant red bird."
                     "\n"
                     "\n"
                     "\nIT - hmm...."
                     "\n   IT bursts out in laughter"
                     "\nIT - oh what is this tale? its so short yet why is it so amusing?"
                     "\n   IT seems to happier than ever seeing your misery"
                     "\nIT - well, may luck be by your side next time.")
             elif "book" in offer:
               print("'IT' tilts its head - 'Shall we gamble for the truth?'")
               if coin_flip():
                  print(f"IT - You win..."
                        "\nIT - fine then, i shall reveal you the truth of this world."
                        "\n     well, about ourselves actually."
                        "\nIT - This world is a realm between the living and the dead."
                        "\n     And i am the one who guaards it."
                        "\nIT - Naturally being the guardian i cannot leave, no matter what i tried i couldn't leave."
                        "\n     So i made you, you can experience what i couldn't, feel what i cannot touch but"
                        "\n     ....."
                        "\nIT - You became someone different, someone else entirely."
                        "\n     So i looked at your 'stories' instead. To fulfill my own desires."
                        "\nIT - That is it, thats the truth of your existence."
                        "\n     ....."
                        "\nIT - well i suppose that is it."
                        "\n"
                        "\n A white mist grabs you as you succumb to it."
                        "\n You return to the cabin, repeating your aventures once again with no memory of the past"
                        "\n as you are transported there words are written in the Book, indescribable yet profound."
                        "\n However after it is written, it closes, and cannot be opened. Not by you at least.")
               else:
                  print(f"IT - Ah you lose..."
                        "\n IT grabs you as you try to resist but..."
                        "\n you succumb to it."
                        "\n You return to the cabin, repeating your aventures once again with no memory of the past"
                        "\n as you are transported there words are written in the Book, indescribable yet profound."
                        "\n However after it is written, it closes, and cannot be opened. Not by you at least.")   
             else:
               print("IT does not respond."
                     "\nThe white plain remains completely silent."
                     "Your car puts its paws on your head, time reverts back as you start over with no memory.")
             print("\n___THE END___")
             break                     
        else:
            print("UNKNOWN COMMAND - Try Again with given commands")
