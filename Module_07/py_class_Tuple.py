# #TUPLE
# grades = (5,4,3,2,1)
# print(len(grades))
# print(grades[0])
# print(grades[2])
# #grades[0] = 4
# grades2 = (7,8,9)
# print(grades + grades2)
# print(grades*3)
# print(3 in grades)
# for i in grades:
#     print()

# def minmax (number_tuple):
#     return min(number_tuple), max(number_tuple)

# number_tuple1 = (1,4,62,45,8,12,0)
# min_num = minmax(number_tuple1)
# max_num = minmax(number_tuple1)
# #min_num, max_num = minmax(number_tuple1)

# print(f"the smallest number is{min_num} and the greatest number is {max_num}")

#SET

# shopping_list = set()
# shopping_list.add("mushroom")
# shopping_list.add("heavy cream")
# shopping_list.add("2 onions")
# print(shopping_list)
# shopping_list.add("2 onions")        #items must be unique or else it won't be shown
# print(shopping_list)
# shopping_list.remove("mushroom")
# print(shopping_list)
# shopping_list.discard("2 onions")
# print(shopping_list)

# #dictionary
# my_dictionary = {}
# my_dictionary["name"] = "address"
# my_dictionary["osoite"] = "address"
# my_dictionary["puh"] = "phone no"
# print(my_dictionary)
# my_dictionary["puh"] = "mobile number"         #changes the item
# print(my_dictionary)

# #access the value of a specific key
# print(my_dictionary["osoite"])

# #check the keys of a dictionary
# print(my_dictionary.keys())
# #check the keys of a dictionary
# print(my_dictionary.values())

# my_dictionary.pop("name")
# print(my_dictionary)

#practice exercise:
#Ex1: Input 3 fruits and print out a dictionary of the fruits
# fruits = {}

# for i in range(3):
#     name = input("Enter a fruit name: ")
#     amount = float(input("Enter the amount in kg: "))
#     fruits[name] = amount
# print(fruits)

#Ex2: inpout numbers until 0, add to a list and print out unique numbers

# numbers = []

# while True:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         break
#     numbers.append(num)

# print(numbers)
# unique_nums = list(set(numbers))
# print(unique_nums)

#Ex3: create a dictionary phonebook

phonebook = {}

while True:
    print("welcome to the phone book program! Here is the menu: ")
    print("a. Add a contact")
    print("b. Search for a contact")
    print("c. Quit")
    choice = input("Choose a,b,c: ")

    if choice == "a":
        name = input("Enter a contact's name: ")
        phone = input("Enter a phone number: ")
        phonebook[name] = phone
        print(f"{name} is now added to the phonebook!")
    elif choice == "b":
        name = input("Enter the name of the contact to search for: ")
        if name in phonebook:
            print(f"{name}'s phone number is {phonebook[name]}")
        else:
            print(f"No contact named {name} is found")
    elif choice == "c":
        print("Bye bye")
        break
    else:
        print("Invalid input: plase enter a,b,c")

#2nd extended version of the phonebook
# create functions to add, to search and phonebook is a list includes
#Each contact is a dictionary

phonebook = []

def add_contact():
    name = input("Enter a contact's name: ")
    id = input("Enter a contact's ID: ")
    dob = input("Enter a contact's Date of birth: ")
    phone = input("Enter a contact's phone number: ")

    contact = {
        "name": name,
        "id": id,
        "dob": dob,
        "phone_num": phone,
    }
    phonebook.append(contact)
    print(f"{name} is now added to the phonebook!")

def search_contact():
    search_name = input("Enter the name of the contact to search for: ")

    for contact in phonebook:
        if contact["name"] == search_name:
            print(f"Name: {contact["name"]}")
            print(f"ID: {contact["id"]}")
            print(f"Date of birth: {contact["dob"]}")
            print(f"Phone number: {contact["phone_num"]}")
        print(f"No contact named {search_name} ")

while True:
    print("___________________________")
    print("Welcome to the phonebooth program! Here is the menu")
    print("a. Add a contact")
    print("b. Search for a contact")
    print("c. Quit")
    choice = input("choose a,b,c: ")
    if choice =="a":
        add_contact()
    elif choice == "b":
        search_contact()
    elif choice == "c":
        print("Bye bye!")
        break
    else:
        print("Invalid input, please type a/b/c")
