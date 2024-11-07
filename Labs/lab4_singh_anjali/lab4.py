# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Lab 4
def main():
    #number of rows in the triangle
    rows = 10
    #creates a loop that runs through all of the rows
    #Prints spaces between each symbol and an odd number of symbols on each line
    for i in range(rows):
        print("  " * (rows - i - 1) + " #" * (2 * i + 1))



main()