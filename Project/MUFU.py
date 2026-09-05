#Game
#project-01 : program that asks for the player’s name and age, stores them in variables, and prints them to the console.
print("Hello Player.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"player name: {name}")
print(f"player age: {age}")

#project-02 : 

if age < 12:
    print("You are a minor. Game is shutting down")
else:
    print("Welcome to the game...")

    while True:
        print("\n___MAIN MENU___")
        print("command options:\nlook- observe surrounding\nitem- check items in bag\nlist- check bucket list\nlopeta- QUIT GAME")

        command = input("- Enter a command: ")

        if command == "lopeta":
            print("until next time.")
            break
        if command == "look":
            print("you look around, your eyes feeling heavy and find yourself in the cabin.")
            print("seems like you were out cold after statyig up all night,")
            print("quite the experience for your first time camping.")
            print("beside you, your black cat MUFU is sleeping with a noticeably large belly")
            print(f"{name}- 'this fur ball ate too much fish yesterday...'")
            print(f"{name}- 'well i suppose i kinda went over my limit as well'")
        elif command == "item":
            print("you look around in your pocket...")
            print("- 1€")
            print("- phone case")
            print("it seems you left your phone outside, hope MUFU didn't scratch it or anything...")
        elif command == "list":
            print("You take out a small piece of paper, few words are written in it:")
            print("-party all night")
            print("-catch your first fish")
            print("-Have Fun (very important!)")
            print(f"{name}- 'God did i really write this? it sounds so cringe... '")
            print(f"{name}-...\n{name}-'well at least i did do one of these three yesterday.'")
        elif command == "lopeta":
            print(f"Until next time ")
            break
        else:
            print("UNKNOWN COMMAND - Try Again with given commands")