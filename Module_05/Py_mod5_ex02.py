#program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

while True:
    inch = float(input("Enter your number(enter negative to end): "))
    if inch <= 0:
        break
    cm = inch * 2.54
    print(f"{inch} inches is equal to {round(cm,2)}")

print("PROGRAM END")

# Or
# inch = float(input("Enter your number: "))

# while not inch <= 0:  
#     cm = inch * 2.54
#     print(f"{inch} iches is equal to {(cm):2f}")
#     inch = float(input("Enter your number: "))

# print("PROGRAM END")