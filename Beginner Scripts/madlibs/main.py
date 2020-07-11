import re
import random

'''
Each Madlib is able to be on multiple lines.
The user-input variables should use the following format:
Example: '___ (word type)'
Word Type = Verb, Adverb, Adjective, etc.
Word type can have multiple words in it like 'verb, past tense'
'''


def madlibGenerator():
    # Initiates madlibs.txt file variables
    madlibs = []  # Used To Hold All the Madlibs Possible
    madlibsEntry = []  # Temp To Hold Lines For Each Madlib

    # creates the list of possible madlibs from the madlibs.txt file
    with open('madlibs.txt', 'r+') as madlibFile:
        for line in madlibFile:
            # Appends Each Line to Temp Madlib List
            madlibsEntry.append(line)

            # Checks If Line Is Empty (Dictates End of Madlib Entry)
            if not line.strip():
                # Appends Entire Madlib Entry List to Madlibs Possibilities
                madlibs.append(madlibsEntry)
                # Reinitiates Temp Madlib Entry
                madlibsEntry = []
        # Appends Final Madlib Entry (When At End of File)
        madlibs.append(madlibsEntry)

    # Randomly Selects Which Madlib To Use
    madlib = random.choice(madlibs)

    # Madlib Entry With User Inputted Variables
    newMadLib = []

    # Goes Through Each Line To Ask User To Input Variable
    for line in madlib:
        # Ensures Every User-Input Variable is Answered
        while re.search(r"___ \(([^\)]+)\)", line) != None:
            # Find The Next User-Input Variable Word Type
            wordType = re.search(r"___ \(([^\)]+)\)", line)
            # Strips The Extra String Characters
            wordType = wordType.group(0).strip('_').strip(
                ' ').strip('(').strip(')').title()
            # Requests User's Input For The Current Variable
            newWord = input("Give a(n) '"+wordType+"': ")
            # Replaces Line with New Line WITH User's Variable
            line = re.sub(r'___ \(([^\)]+)\)', newWord, line, 1)
        # Appends the New Line to the New Madlib
        newMadLib.append(line)

    # Prints The New Madlib Line by Line
    print()
    for line in newMadLib:
        print(line, end='')

    return newMadLib


# Default Constructor Method
if __name__ == "__main__":
    madlibGenerator()
