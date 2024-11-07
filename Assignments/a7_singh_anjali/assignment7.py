# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 7
# Description:
#define and call functions to stimulate a game of rock-paper scissors
def main():
    keepRunning = True
    #createes variables for the counts of who wins
    winCount = 0
    loseCount = 0
    tieCount = 0
    #while true...
    while keepRunning:
        #call the menu function and store the computernum and playerum function output into variables
        displayRules()
        computerNum = getComputerNum()
        playerNum = getPlayerNum()
        #calls the playround function to play the game
        outcome = playRound(computerNum, playerNum)
        #if the outcome variable equals 0,1,-1 then returns appropriate message
        if outcome == 0:
            print("You and the computer tied.")
            tieCount = tieCount + 1
        elif outcome == 1:
            print("You win!")
            winCount = winCount + 1
        else:
            print("Computer wins.")
            loseCount = loseCount + 1
        #calls the continue game function, if the user doesn't enter y it outputs the final message
        keepRunning = continueGame()
        if keepRunning == False:
            print("\nYou won " + str(winCount) + " game(s)")
            print("The computer won " + str(loseCount) + " game(s).")
            print("You tied with the computer " + str(tieCount) + " time(s).")


#This function displays the menu
def displayRules():
    print("Let's play Rock Paper Scissors.")
    print("The rules of the game are:")
    print("\tRock smashes Scissors")
    print("\tScissors cut Paper")
    print("\tPaper covers Rock")
    print("\tIf both the choices are the same, it's a tie")
#This function gets a random integer and stores it in a variable
def getComputerNum():
    import random
    randomNum = random.randrange(1,3)
    return randomNum
#This function creates a loop and gets the user input until its in the valid range
def getPlayerNum():
    keepGoing = True
    print("Enter 0 for Rock, 1 for Paper, or 2 for scissors ")
    while keepGoing:
        choice = int(input("> "))
        if choice == 0 or choice == 1 or choice == 2:
            keepGoing = False

    return choice
#This function compares the computer number to the player number and returns an integer based on who wins
def playRound(computerNum, playerNum):
    if computerNum == playerNum:
        return 0
    elif playerNum == 1:
        if computerNum == 0:
            return 1
        elif computerNum == 2:
            return -1
    elif playerNum == 0:
        if computerNum == 1:
            return -1
        elif computerNum == 2:
            return 1
    elif playerNum == 2:
        if computerNum == 0:
            return -1
        elif computerNum == 1:
            return 1

#This function asks the user whether or not to continue the game and returns true or false
def continueGame():
    keepPlaying = input("Do you want to continue playing (y or n)? ")
    if keepPlaying.lower() == "y":
        return True
    else:
        return False

main()