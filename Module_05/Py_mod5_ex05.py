#program that asks the user for a username and password

user_name = input("Enter your Username: ")
password = input("Enter your Password: ")
tries = 1
while True:
    if user_name == "python" and password == "rules":
        print("Welcome")
        break
    if user_name != "python" or password != "rules":
        print("username or password wrong")
        print("Please Enter again")
    user_name = input("Enter your Username: ")
    password = input("Enter your Password: ")

    tries = tries + 1
    if tries == 5:
     print("Access denied")
     break
   