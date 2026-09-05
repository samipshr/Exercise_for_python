# program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
print("all numbers divisible by 3 in the range of 1-1000")

num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num = num + 1

print("All numbers divisible by 3 from 1-1000")