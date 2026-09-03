# #PYTHON WEEK 3 - CLASS LESSON
# # create an empty list:
# list1 = []
# # create a list with some items:
# list2 = [9,8,2]
# # access a single item from the list:                                      
# print(list2[0])
# print(list2[1])
# print(list2[2])

# print("the sum of all items in list2 is", list2[0] + list2[1] + list2[2])

# #tip - press cmmd + / to a line of code to comment it, or to uncomment it

shopping_list = ["bread", "milk", "eggs", "butter", "cheese"]
print(shopping_list)
shopping_list[2] = "tomatoes"
print(shopping_list)
shopping_list.append("yogurt")
print(shopping_list)
shopping_list.insert(1, "butter")
print(shopping_list)

# slice the list from the beginning to a certain index:
print(shopping_list[:3])       #it will print the items after index 3 (won't include the item at index 3)
print(shopping_list[2:])       #it will print the items from index 2 (won't include the items before index 2)

#remove an item usig pop():
shopping_list.pop(4)          #it will remove the item at index 4
print(shopping_list)

#remove an item using remove():
shopping_list.remove("butter")  #it will remove the item "butter"
print(shopping_list)

#extend a list:
shopping_list2 =["cookies", "rice"]
shopping_list.extend(shopping_list2)   # adds items from another list to the end of the first list
print(shopping_list)

#check if an item exists in the list:
if "bread" in shopping_list:
    print("Hmm, sandwich ")
else:
    print("There is no bread, there is no buttter, and there is no Grilled Cheese Sandwich")

#to sort the items in either alphabetical or numerical order:
shopping_list.sort()   #sorts the list in alphabetical order
print(shopping_list)

for number in range(0, 11):  #this will print the numbers from 0 to 10
    print(number)

for number in range(6):  #this will print the item print("POSITIVE VIBES!") 6 times
    print("POSITIVE VIBES!")

#to know the number of items in a list, use the len() function:
total_items = len(shopping_list)
print("total_items:", total_items)

# Example-1:
# name = input("Enter your name: ")
# for character in name:
#     print(f"{character}")

# Example-2:
# number = int(input("Give me a number: "))
# if number <= 0:
#     print("This negative number shall not pass! Enter a positive number next time")
# else:
#     total_sum = 0
#     # for i in range(0,number+1, 2):    # "i" is a helper variable but you can use whatever
#     #     print(i)
#  #or
#     for i in range(number+1): 
#       if i % 2 == 0:
#          print(i)
#          total_sum = total_sum + i  # OR, total_sum += i 
#     print("sum of all Even numbers: ", total_sum)

# Example-3:
# number_list = []
# while True:
#     entry_num = input("Enter a number ")
#     if entry_num == " ":
#         break
#     number_list.append(int(entry_num))

# printed_list = []
# for number in number_list:
#     if number > 100 and number not in printed_list:
#         print(number)
#         printed_list.append(number)

# Example-4:
# sentence = input("Enter a sentence: ")
# sentence = " " + sentence
# for index_num in range(1, len(sentence)):
#     if sentence[index_num] == " " and sentence[index_num] != " ":
#         print(sentence[index_num])
#     index_num += 1
    