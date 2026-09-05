#program that asks the user to enter the names of five cities and prints put the names one by one.

cities = []

for i in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)
print("cities:")

for city in cities:
    
    print(city)