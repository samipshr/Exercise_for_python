#program that asks the user to enter a year and notifies the user whether the input year is a leap year.

print("This program will let you know if the given year is a leap year or not.")
year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year. ")
else:
    print(f"{year} is not a leap year. ")