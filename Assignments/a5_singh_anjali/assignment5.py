# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 5
# Description:
#Allows the user to enter a sentence and then uses looping to print an
#Asterick symbol to show character distrubution

def main():

    keepRunning = True
    runNumber = int(input("Enter the number of times to run: "))
    #range based loop that runs as many times as user wants it to
    while runNumber >= 1:
        # All of the letters in the alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        # Gets a sentence from the user
        sentence = input("Enter a sentence: ")
        runNumber = runNumber-1
        # Counts the number of special characters
        specialCount = 0
        # For each letter in a sentence, if the letter is not in the alphabet variable, add 1 to special count variable
        for letter in sentence:
            if letter.lower() not in alphabet and letter != ' ':
                specialCount = specialCount + 1
        # Prints the number of astericks per the number of special count
        if specialCount >= 1:
            print("Special Character" + ": " + "*" * specialCount)
        elif specialCount == 0:
            print("Sepcial Character" + ": NONE")

        for eachLetter in alphabet:
            counter = 0
            # If the letter in the word is in the alphabet, add one to the counter
            for char in sentence:
                if eachLetter in char.lower():
                    counter = counter + 1
                # Elif the letter is ot in the alphabet, counter remainds same
                elif eachLetter not in char.lower():
                    counter = counter
            # If the counter is greater than or equal to 1, multiply it be the astericks
            if counter >= 1:
                print(eachLetter + ": " + "*" * counter)
            else:
                print(eachLetter + ": " + "NONE")
    #Exits code
    keepRunning = False


main()