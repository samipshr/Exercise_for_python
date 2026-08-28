#program that asks for the biological gender and hemoglobin value (g/l),
#program the notifies the user if the hemoglobin value is low, normal or high

print("This is only accurate for adults, consult an ACTUAL doctor for children and teenagers.")
gender = input("Enter your gender (M/F): ")
hvalue = float(input("Enter your hemoglobin value (g/l): "))

if gender == "M" or gender == "m":
    if hvalue < 134 or hvalue > 167:
        print("Your hemoglobin value is not at a normal level, consult a Doctor,")
    elif hvalue >= 134 and hvalue <= 167:
        print("Your hemoglobin value is at a normal level, you are healthy ")
if gender == "F" or gender == "f":
    if hvalue < 117 or hvalue > 155:
        print("Your hemoglobin value is not at a normal level, consult a Doctor,")
    elif hvalue >= 117 and hvalue <= 155:
        print("Your hemoglobin value is at a normal level, you are healthy ")
    else:
      print("Invalid gender input, enter M for Male or F for female")