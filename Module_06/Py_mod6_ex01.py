#program that asks the user how many dice to roll.
#program rolls all the dice once and prints out the sum of the numbers

import random

dice = int(input("How many dice would you like to roll: "))
total = 0

for i in range(dice):
    roll = int(random.uniform(1, 6))
    total = total + roll
print(f"sum of the numbers:{total}")