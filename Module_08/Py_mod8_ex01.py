#program that asks the user for a number of a month and then prints out the corresponding season 

season = ("spring" , "summer", "autumn", "winter")
month = int(input("Enter the number of a month: "))


if month in (3, 4, 5):
    print(season[0])
elif month in (6, 7, 8):
    print(season[1])
elif month in (9, 10, 11):
    print(season[2])
elif month in (12, 1, 2):
    print(season[3])
else:
    print("There is no new month after 12 or before 1")