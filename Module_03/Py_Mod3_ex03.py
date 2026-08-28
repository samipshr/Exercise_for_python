#program to calculate the perimeter and area of a rectangle.\
# (The perimeter of a rectangle is the sum of the lengths of each four sides)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print(f"The perimeter of the rectangle is: {round(perimeter,2)}cm")
print(f"The area of the rectangle is: {round(area,2)}cm^2") 