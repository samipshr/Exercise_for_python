#function that gets a list of integers as a parameter
#function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed

def remove_odd(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


# Main program
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = remove_odd(numbers)

print("Original list:", numbers)
print("Even no list:", even)