#program that asks a fisher the length of a zander in centimeters
#If the zander does not fulfill the size limit, notifies the fisher that the zander must be released

length = float(input("Enter the length of the Zander : "))

if length >= 42:
    print("The Zander is legal to keep.")
elif length <42:
    print("The Zander is smaller than the legal size limit and must be released.")
    print(f"The Zander is {round(42 - length, 2)}cm below the size limit. ")