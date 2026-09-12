#function that returns a random dice roll between 1 and 6 unil you get a 6

import random

def dice():
    return random.randint(1, 6)
roll = 0

while True:
    result = dice()
    roll += 1
    print("Roll:", result)
    if result == 6:
        break

print(f"It took {roll} rolls to get a 6")