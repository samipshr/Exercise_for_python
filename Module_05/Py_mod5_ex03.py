#program that asks the user to enter numbers until they enter an empty string to quit,
# Finally, the program prints out the smallest and largest number from the numbers it received.

smallest = 0
largest = 0

while True:
     value = input("Enter your number")
     if value == "": 
        break
     num = float(value)
     if smallest == 0 or num < smallest:
        smallest = num
     if largest == 0 or num > largest:
        largest = num
     

if smallest != "" and largest != "":
  print(f"Smallest number: {smallest}")
  print(f"largest number: {largest}")
