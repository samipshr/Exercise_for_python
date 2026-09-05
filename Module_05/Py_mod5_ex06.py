#rogram that asks the user how many random points to generate, and then calculates the approximate value of pi.

import random

num = int(input("How many random points to generate: "))
no = 0

for i in range(num):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        no = no + 1

pi = 4 * no / num

print("Approximation value of pi:", pi)
