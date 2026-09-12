# function that gets a list of integers as a parameter
# function returns the sum of all the numbers in the list

def list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [10, 20, 30, 40, 50]
result = list(numbers)
print("the sum is: ", result)