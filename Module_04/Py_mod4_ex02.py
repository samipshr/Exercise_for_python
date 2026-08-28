#program that asks the user to enter the cabin class of a cruise ship

print("This cruise ship has Four cabin classes - LUX, A, B, C")
cabin_class = input("Enter your cabin class for this cruise: ")

if cabin_class == "LUX":
    print("You have selected LUX: upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("You have selected A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("You have selected B: windowless cabin above the car deck")
elif cabin_class == "C":
    print("You have selected C: windowless cabin below the car deck")
else:
    print("Invalid cabin class.")