#program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti)
#Result: program converts the input to full kilograms and grams.

talents = float(input("Enter the mass for talents:" ))
pounds = float(input("Enter the mass for pounds:" ))
lots = float(input("Enter the mass for lots:" ))

#Greek Attic talents = 25.8 kg, pounds = 0.45 kg, lots = 0.0128 kg

kilograms = (talents * 25.8) + (pounds * 0.5) + (lots * 0.0128)
grams = kilograms * 1000

print(f"The weight in modern units is:\
       {round(kilograms, 2)}Kg or {round(grams, 2)} grams.")