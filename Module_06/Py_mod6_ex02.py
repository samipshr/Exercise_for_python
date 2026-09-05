#program that asks the user to enter numbers until they input an empty string to quit
#At the end, the program prints out the five greatest numbers sorted in descending order

numbers = []

while True:
    num = input("Enter any number(press enter to stop): ")
    if num == "":
        break
    numbers.append(int(num))
numbers.sort(reverse=True)
print("five greatest entered numbers: ")

for num in numbers[:5]:
    print(num)
