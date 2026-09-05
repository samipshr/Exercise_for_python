#Game program - guess the number

import random 

random_integer = int(random.uniform (1, 10))
num = int(input("Enter an integer from 1-10: "))
while True:
    if num == random_integer:
        break
    print("INCORRECT GUESS")
    if num > random_integer:
        print("Too High")
    elif num < random_integer:
        print("Too Low")
    num = int(input("Enter an integer from 1-10: "))
    
if num == random_integer:
    print("Correct! you won!")