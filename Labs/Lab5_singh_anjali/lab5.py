# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Lab 5

def main():
    #creates the three lists with three elements for verbs,adverbs, and nouns
    noun = ["Panda", "Betty Crocker","Hawaii"]
    verbs = ["danced","laughed","walked"]
    adverbs = ["happily", "cheerfully","bravely"]
    #Loop that continually runs the game until the user quits
    keepRunning = True
    while keepRunning:
        #Prints out menu options
        print("Welcome to the Sentence Generator")
        print("1) View Words")
        print("2) Add Noun")
        print("3) Remove verb")
        print("4) Generate Sentence")
        print("5) Exit")
        #gets users choice
        choice = input("> ")
        #If the user chosses 1, outputs the lists
        if choice == "1":
            print("nouns:",noun, "\nverbs:", verbs, "\nadverbs:",adverbs,"\n")
        #If the user enters 2, take in the input of the user and append it to the list
        elif choice == "2":
            newNoun = input("Enter the word: ")
            noun.append(newNoun)
       #If the user enters 3, take in there input and remove that from the list
        elif choice == "3":
            newVerb = input("Enter the word: ")
            verbs.remove(newVerb)
        #If the user enters 4, import the random module and use random.choice() to choose a rand item from each list
        #Print the items in order to create a sentence
        elif choice == "4":
            import random
            randomNoun = random.choice(noun)
            randomVerb = random.choice(verbs)
            randomAdverb = random.choice(adverbs)
            print(randomNoun,randomVerb,randomAdverb + ".\n")
        #If the user enters 5, print a message and exit the while loop
        elif choice == "5":
            print("Thank you for using Sentence Generator!")
            keepRunning = False
        #If the user doesn't enter a valid choice output invalid choice
        else:
            print("\nInvalid choice")















main()
