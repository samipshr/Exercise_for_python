#function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros
#function calculates and returns the unit price of the pizza per square meter

import math

def price(diameter, price):
    radius = diameter / 200
    area = math.pi * radius ** 2
    return price / area


diameter1 = float(input("Enter diameter of pizza 1 : "))
price1 = float(input("Enter price of pizza 1 (€): "))

diameter2 = float(input("Enter diameter of pizza 2 : "))
price2 = float(input("Enter price of pizza 2 (€): "))

unit1 = price(diameter1, price1)
unit2 = price(diameter2, price2)

print("Pizza 1 unit price:", unit1, "€/m²")
print("Pizza 2 unit price:", unit2, "€/m²")

if unit1 < unit2:
    print("Pizza 1 provides better value for money.")
elif unit2 < unit1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")