# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Lab 7
#function that prints a square and takes in length and width as parameters
def printRectangle(length, width):
    #Prints number of dashes times width
    print(" " + width * "-")
    #For loop that prints vertical bars and creates spaces times the length
    for x in range(length):
        print("|" + str(" " * width) + "|")
    # Prints number of dashes times width
    print(" " + width * "-")

#function that takes in a size parameter and prints a square
def printSquare(size):
    #prints the top of the square
    print(" " + str(size * "-"))
    #For loop that prints the sides of the square
    for y in range(size):
        print("|" + str(" " * size) + "|")
    # Prints the bottom of the square
    print(" " + size * "-")

def main():
    #Asks user to choose a shape
    print("What shape would you like to print?")
    print("r) rectangle")
    print("s) square")
    #Takes in user input
    shape = input("> ")
    #If user choses r, take in the length and width and call the rectangle function
    if shape.lower() == "r":
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        printRectangle(length, width)
    #If the user chosses s, take in the user size and call the square function
    elif shape.lower() == "s":
        size = int(input("Enter the side: "))
        printSquare(size)
    #If user doesn't choose r or s, output this message
    else:
        print("That shape is not supported.")

main()