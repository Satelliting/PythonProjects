import random


def passwordGenerator():
    # Initiates all possible characters for password combinations
    lowLetters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    highLetters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    specials = [
        ' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', ' ^ ', '_', '`', '{', ' | ', '}', '~'
    ]

    # User Inputted Choices
    choices = [None, None, None, None, '-1']

    # User Input for Possible Characters to be Used
    while choices[0] not in ['0', '1']:
        choices[0] = input("Do you want lowercase letters? 0 = No, 1 = Yes: ")
    while choices[1] not in ['0', '1']:
        choices[1] = input("Do you want uppercase letters? 0 = No, 1 = Yes: ")
    while choices[2] not in ['0', '1']:
        choices[2] = input("Do you want numbers? 0 = No, 1 = Yes: ")
    while choices[3] not in ['0', '1']:
        choices[3] = input("Do you want special chars? 0 = No, 1 = Yes: ")

    # Check if NO Possible Characters are Useable
    if choices[0] == '0' and choices[1] == '0' and choices[2] == '0' and choices[3] == '0':
        print("No possible password.")
        exit()

    # Compiles a List of ALL Potential Characters for the Created Password
    potentialLists = []
    if choices[0] == '1':
        potentialLists.append(lowLetters)
    if choices[1] == '1':
        potentialLists.append(highLetters)
    if choices[2] == '1':
        potentialLists.append(numbers)
    if choices[3] == '1':
        potentialLists.append(specials)

    # User Input For Password Length
    while choices[4].isdigit() == False or choices[4] == '0':
        choices[4] = input("How many characters? ")

    # Creates The Password
    password = ''
    length = int(choices[4])
    while length > 0:
        # Randomly Selects Which Potential Character Lists Is Selected
        choiceList = random.choice(potentialLists)
        potentialLists.remove(choiceList)
        # Randomly Selects # of Characters Used From choiceList
        choiceLength = random.randint(1, (length - (len(potentialLists))))
        # Lowers Total Length Left Available For Other Potential Lists
        length = length - choiceLength

        # Randomly Selects Character From choiceList
        for potentialChar in range(choiceLength):
            password = password + random.choice(choiceList)

    # Shuffles Entire Password To Avoid All Same List Characters Being Next To One Another Every Time
    password = ''.join(random.sample(password, len(password)))

    print()
    print(password)
    return password


# Default Constructor Method
if __name__ == "__main__":
    passwordGenerator()
