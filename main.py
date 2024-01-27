import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
repeat = True

while repeat:
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password = []

    for x in range(1, nr_letters + 1):
        randChar = random.choice(letters)
        password += randChar

    for x in range(1, nr_symbols + 1):
        randChar = random.choice(symbols)
        password += randChar

    for x in range(1, nr_numbers + 1):
        randChar = random.choice(numbers)
        password += randChar

    random.shuffle(password)
    newPassword = ""
    for x in password:
        newPassword += x

    print(f"Your password is \n {newPassword} \n has {nr_numbers} numbers, {nr_symbols} symbols, {nr_letters} letters.")
    regenerate = int (input("Do you want to repeat the process?\n press 1-yes \n press 2-no "))
    if regenerate == 2:
        repeat = False
        break