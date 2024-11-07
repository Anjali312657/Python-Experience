# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 6
# Description:
#a game that displays jumbled words to the user and the user has to guess
#the word and continue guessing until it's correct

def main():
    #imports random module
    import random
    #creates a list with words and hints corresponding to the wrods
    words = ["panda","carnation","sentence","hawaii"]
    hints = ["They love bamboo!","Ohio's state flower.","This in itself is an example.","Islands in the pacific ocean!"]
    #Assingns a random word from the list to the variable and stores the index of the random word in a varaible
    randomWord = random.choice(words)
    indexOfWord = words.index(randomWord)
    #Turns random word into a list
    wordList = list(randomWord)
    #Gets the index of the random word from the hints list and stores it in a variable
    hint = hints[indexOfWord]
    #Empty string to hold jumbled word
    jumbledWord = ""
    #While the list still has elements
    while len(wordList) > 0:
        #Chooses a random letter from the list and removes that letter
        letter = random.choice(wordList)
        wordList.remove(letter)
        #Adds the random letter to the string
        jumbledWord = jumbledWord + letter
    #Prints the word jumbled up
    print("The jumbled word is " + "\"" +jumbledWord + "\"")
    #Asks user to guess and starts count off as 1 due to acount for users first guess
    userInput = input("Enter your guess: ")
    count = 1
    #While the input is not equal to the word
    while userInput != randomWord:
        #Output that its not correct and increase the counter
        print("That is not correct")
        count = count + 1
        #Ask the user if they want a hint, if they do print a hint
        hintInput = input("Do you want a hint (y or n)? ")
        if hintInput.lower() == 'y':
            print(hint)
        #Prints the jumbled word again and asks the user to get
        print("The jumbled word is " + "\"" +jumbledWord + "\"")
        userInput = input("Enter your guess: ")
    #Output that the user got it the message and ouputs the counter if the user input was equal to the random word
    print("You got it!")
    print("It took you", count, "guesses.")

main()
