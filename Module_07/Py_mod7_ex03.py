#function that gets the quantity of gasoline in American gallons and returns the number converted to litres
#main program that asks for a volume in gallons from the user and converts the value to liters
# if user enters negative, program ends

def gal(amount):
    return amount * 3.78541

while True:
    amount = float(input("Enter the amout of gallons to convert to litres (Enter a negative to quit): "))
    if amount < 0:
        break
    lit = gal(amount)
    print(f"{amount} gallons is equal to {lit} litres")
    