#program for fetching and storing airport data


airports = {}

while True:
    print("\nOptions:")
    print("1 - Enter a new airport")
    print("2 - Fetch airport information")
    print("3 - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        code = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")

        airports[code] = name
        print("Airport added.")

    elif choice == "2":
        code = input("Enter the ICAO code: ")

        if code in airports:
            print(airports[code])
        else:
            print("Airport not found.")

    elif choice == "3":
        break

    else:
        print("Invalid option.")