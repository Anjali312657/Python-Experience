# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 8
# Description:
#Program that simulates a two-player game of Tic-Tac Toe
import TicTacToeHelper

#Parameters: a list representing the board, an integer that corresponds to the index position that the user wants their choice to land on
#Return values: a boolean value, true or false that checks if the board position is in the range and available
#Purpose:This function checks if the position entered is a valid number in the range and checks to see if the position is available
#It returns true false if its taken and true its available
def isValidNumber(boardList,position):
    if 0 <= position <= 8:
        if boardList[position] == "x" or boardList[position] == "o":
            return False
        else:
            return True
#Parameters: a list representing the board, an integer that represents the index position the user chooses their 'x' or 'o' for, and a string that represents the users 'x' or 'o'
#Return value: none
#Purpose: This function places the player's 'x' or 'o' in the space that they chose on the board
def updateBoard(boardList,position,playerLetter):
    boardList[position] = playerLetter
#Parameters: None
#Reurn Value:None
#Purpose: This function through each player taking a turn until the game is over. It outputs who wins
def playGame():
    board = ["0","1","2","3","4","5","6","7","8"]
    moveCount = 0
    player = "x"
    #While the game is not over...
    while TicTacToeHelper.checkForWinner(board, moveCount) == "n":
        #prints board
        TicTacToeHelper.printPrettyBoard(board)
        keepRunning = True
        #This loop takes in user input about what position they want, if its a valid number the loop will stop running
        #Inside this loop the updateBoard function is called so that the users input will be updated in the board
        while keepRunning:
            pos = int(input("Player " + player + ", enter a number: "))
            if isValidNumber(board,pos):
                updateBoard(board,pos,player)
                keepRunning = False
        #changes the players to go back and forth
        if player == "x":
            player = "o"
        elif player == "o":
            player = "x"
        #increases move count after each move
        moveCount = moveCount + 1
    #reprints board
    TicTacToeHelper.printPrettyBoard(board)
    #sets the winner equal to a variable
    result = TicTacToeHelper.checkForWinner(board,moveCount)
    print("\nGame Over!")
    #Prints out the winner depending on the checkforWinner function
    if result == "x":
        print("Player x is the winner!")
    elif result == "o":
        print("Player o is the winner!")
    else:
        print("Stalemate reached.")
#Parameter:none
#Return value:none
#Purpose: Calls the play game function and checks how many rounds the user wants to play
def main():
    print("Let's play Tic Tac Toe!")
    keepPlaying = True
    while keepPlaying:
        playGame()
        goAgain = True
        while goAgain:
            playAgain = input("Would you like to play another round(y/n): ").lower()
            if playAgain == "y":
                goAgain = False
            else:
                keepPlaying = False
                goAgain = False
    print("Goodbye!")

main()



