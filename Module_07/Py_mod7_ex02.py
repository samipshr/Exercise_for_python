#modified function that returns a random dice roll between 1 and the input number until it gets the input number.

import random

def dice(side):
    return random.randint(1, side)
rolls = 0
side = int(input("Enter the no of sides on the dice: "))

while True:
    result = dice(side)
    rolls += 1
    print("Roll:", result)
    if result == side:
        break

print(f"it took {rolls} rolls to get a {side}")