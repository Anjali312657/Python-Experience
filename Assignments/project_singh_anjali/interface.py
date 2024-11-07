# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Final Project
#Interface.py
# Description:This file includes various functions that are called in the main.
#This file contains functions that get the menu, display the menu, read the user choice,prints all parks, prints
#parks by state, prints the largest park, gets the user state choice, and prints park by search

import tasks
#Parameters:None
#Returns: A dictionary in which the keys are letters and the values are the header line of the CSV file
#Description: Creates a menu by creating a dictionary of the menu options
def getMenuDict():
    menu = {'A': 'All national parks', 'B': 'Parks in a particular state','C': 'The largest park','D' : 'Search for a park',
            'E' : 'The oldest park', 'Q' : 'Quit'}
    return menu
#Parameters:menuDict is the dictionary for the menu
#Returns:None
#Description:prints the menu in the correct format with arrows
def displayMenu(menuDict):
    print()
    for key in menuDict:
        print("" + key + " -> " + menuDict[key])
#Parameters:menuDict is the dictionary for the menu
#Returns: choice, which is a valid string  entered by the user
#Description:Uses a loop and asks the user for input until its valid
def getUserChoice(menuDict):
    #asks the user for their choice and capitalizes it
    choice = input("Choice: ").title()
    #turns the keys of the dictionary into a list
    keysList = list(menuDict.keys())
    #loops through and checks if the choice entered is in the list of the keys that were in the dictionary
    while choice not in keysList:
        choice = input("Choice: ").title()
    return choice
#Parameters:parksList is a list of dictionary objects with park information
#Returns:None
#Description: Loops thruogh each park in the list of dictionary objects and prints out information for each park in the file
def printAllParks(parksList):
    #for each park in the list, prints out park information in the correct format
    for park in parksList:
        print((park["Name"]) + "(" + (park["Code"]) + ")")
        print("\tLocation:",park["State"])
        print("\tArea:",park["Acres"],"acres")
        print("\tDate Established:",tasks.convertData(dataStr=park["Date"]))
#Parameters:None
#Returns: a string of the two letter state abbreviation
#Description: Gets input from the user and loops through until the user enters a two state abbreviation
def getStateAbbr():
    state = input("Enter a state: ").upper()
    #While the length of the input is not two, keep asking the user to enter a abbreviation
    while len(state) != 2:
        print("Need the two letter abbreviation")
        state = input("Enter a state: ").upper()
    return state
#Parameters:parksList is a list of dictionary objects with park information
#Returns:None
#Description:Loops through and checks if parks are in the state chosen by the user, prints out park information
def printParksInState(parksList):
    #call this function to get the state and stores it in a variable
    state = getStateAbbr()
    counter = 0
    #loops through each park in the list
    for park in parksList:
        #if the state entered is a value in the state key, prints out park information in the correct format
        if state in park["State"]:
            print((park["Name"]) + "(" + (park["Code"]) + ")")
            print("\tLocation:", park["State"])
            print("\tArea:", park["Acres"], "acres")
            print("\tDate Established:", tasks.convertData(dataStr=park["Date"]))
            #increment counter if parks were identified in the state
            counter = counter + 1
    #if the counter was not incremented, print out this statement
    if counter == 0:
        print("There are no national parks in",state, "or it is not a valid state.")
#Parameters: parkList is a list of dictionary objects with park information
#Returns:None
#Description: Prints information about the largest park
def printLargestPark(parksList):
    #calls the LargestPark function and sets the return value to a variable to get the largest park
    largestPark = tasks.getLargestPark(parksList)
    for park in parksList:
        # if the park code matches up with the code from the largest park, prints out park information in the correct format
        if park["Code"] == largestPark:
            print((park["Name"]) + "(" + (park["Code"]) + ")")
            print("\tLocation:",park["State"])
            print("\tArea:",park["Acres"],"acres")
            print("\tDate Established:",tasks.convertData(dataStr=park["Date"]))
            print("\tDescription:",park["Description"].strip('"'))
#Parameters: parkList is a list of dictionary objects with park information
#Returns: None
#Description: Gets input from the user and allows them to search for key words in parks
def printParksforSearch(parksList):
    search = input("Enter text for searching: ")
    counter = 0
    #loops through each park in the list of parks
    for park in parksList:
        #if the users input appears in the values of the code,name, or description keys, then print out park information in the correct format
        if search in park["Code"].lower() or search in park["Name"].lower() or search in park["Description"].lower():
            print((park["Name"]) + "(" + (park["Code"]) + ")")
            print("\tLocation:",park["State"])
            print("\tArea:",park["Acres"],"acres")
            print("\tDate Established:",tasks.convertData(dataStr=park["Date"]))
            print("\tDescription:",park["Description"].strip('"'))
            # increment counter if searches were found
            counter = counter + 1
            print()
    # if the counter was not incremented, print out this statement
    if counter == 0:
        print("There are no national parks for the search term of '"+search +"'.")
#Parameters: parkList is a list of dictionary objects with park information
#Returns: None
#Description: Prints the oldest park in the directory
def printOldestPark(parksList):
    for park in parksList:
        code = tasks.printOldestPark(parksList)
        if code in park["Code"]:
            print((park["Name"]) + "(" + (park["Code"]) + ")")
            print("\tLocation:",park["State"])
            print("\tArea:",park["Acres"],"acres")
            print("\tDate Established:",tasks.convertData(dataStr=park["Date"]))
            print("\tDescription:",park["Description"].strip('"'))
