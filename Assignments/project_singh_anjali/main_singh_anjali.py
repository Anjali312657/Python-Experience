# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Final Project
#main_singh_anjali.py
# Description:
#This file imports two other python files and uses branching to call each function depending on user input
import tasks
import interface

def main():
    print("National Parks")
    #reads the file and sets it equal to a variable to use as a parameter in arious functions
    parkList = tasks.readParksFile()
    #gets the menu for the user
    menu = interface.getMenuDict()
    choice = ""
    #while loop runs until the user enters q
    #branching is used to call certain functions depending on the users input
    while choice != "Q":
        interface.displayMenu(menu)
        choice = interface.getUserChoice(menu)
        if choice == "A":
            interface.printAllParks(parkList)
        elif choice == "B":
            interface.printParksInState(parkList)
        elif choice == "C":
            interface.printLargestPark(parkList)
        elif choice == "D":
            interface.printParksforSearch(parkList)
        elif choice == "E":
            interface.printOldestPark(parkList)

main()