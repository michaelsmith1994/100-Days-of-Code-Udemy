import random

def generateAPassword(w, x, y, z):
    startPassword = []
    if(w != "False"):
        startPassword += [chr(random.randint(65, 90)) for _ in range(1)]
    startPassword += [chr(random.randint(97, 122)) for _ in range(x)]
    startPassword += [chr(random.randint(48, 57)) for _ in range(y)]
    symbol_ranges = (
        list(range(33, 48)) +   # ! to /
        list(range(58, 65)) +   # : to @
        list(range(91, 97)) +   # [ to `
        list(range(123, 127))   # { to ~
    )
    startPassword += [chr(random.choice(symbol_ranges)) for _ in range(z)]
    
    random.shuffle(startPassword)
    return ''.join(startPassword)
    
print("\nWelcome to the password generator.")

upper_char = str(input("\nNeed a capital letter? True or False "))
lower_char = int(input("How many lower case letters in this password? "))
number_char = int(input("How many numbers in this password? "))
symbol_char = int(input("How many symbols in this password? "))

createdPassword = generateAPassword(upper_char, lower_char, number_char, symbol_char)
print("\nYour password is: " + createdPassword)