radius = float(input("Enter the radius of the circle: "))
import math
area = math.pi * radius ** 2   #Either use radius ** 2 or pow(radius,2)
print(f"The area of the circle is: {round(area,3)}cm^2")