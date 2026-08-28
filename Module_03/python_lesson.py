#
letter = input("enter a letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u": 
    print("this letter is a vowel")
elif letter == "y":
    print("this letter is sometimes a vowel and sometimes a consonant")
elif letter.isalpha():
    print("this letter is a consonant")
else:
    print("that is not a letter from the alphabet")