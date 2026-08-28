#program that asks the user for three integer numbers.
#Result: program prints out the sum, product, and average of the numbers.
no1 = int(input("Enter the first integer no: "))
no2 = int(input("Enter the second integer no: "))
no3 = int(input("Enter the third integer no: "))

sum = no1 + no2 + no3
product = no1 * no2 * no3
average = sum / 3

print(f"The sum of the three integers is: {sum}")
print(f"The product of the three integers is: {product}")
print(f"The average of the three integers is: {round(average,2)}")