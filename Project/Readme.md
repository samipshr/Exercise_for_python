# PROJECT: making a game

** Game name: MUFU, \
creator: Samip Shrestha **

# Project_01: Created a separate folder and started the program

** Asks user for name and age **

# Project_02: made a menu with commands and an option to quit game

** gives responses to certain commands and if entered 'lopeta' it shuts down the game **

# Project_03: made main Menu Functions and “Inventory”

** can add items to inventory **

# Project 4 : Organize the Structure and Introduce Objects

** introduced objects (program) and new locations (game) **


# Game IDEA and Objective:

** A choice baseed game set in a limenal space. **
It's supposed to be about how some people give up some parts of themselves to save some space for others 
based on your choices you can get different endings, some you might like, others you may not
the player must decide on their own, there are no 'harmful' mosters.
choice based game

** !!! there is a SECRET ENDING ( not added yet )***

# Structure:

** The project is split into different files. **
├–– main.py            # the game loop.
├–– player.py          # Player class.
├–– room.py            # Room class.
├–– items.py           # Item class.
├–– save.py            # save_game, load_game, delete_save.
├–– coin_flip.py       # coin_flip()
├–– intro.txt          # printed at startup.
├–– instructions.txt   # printed at startup and by the help command.
└── saves              # save files as .txt

# Routes and goals:
** Any of these routs gives an ending: **
route 1: The humble route.
route 2: The Free spirit ending.
route 3: The Footless bird ending.
route 4: The Fools ending.
route 5: The truth and lies ending.
route 6: Return to 0 ending

# player actions:
look - observe surrounding
move - move to another room
collect - collect an item
item - inspect an item
list - check bucket list
give - give away an item
pray - perform the ritual
help - shows the instruction.txt file again
save - saves the game progress
lopeta - QUIT GAME
