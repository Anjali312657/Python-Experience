# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Final Project
#Tasks.py
# Description:This is essentially a helper file that is used in interface.py
# This file includes the readParksFile, which creates a list of dictionary objects from the CSV file, a date converter
#which formats the date and a function that finds the largest park


#Parameters:fileName is set to the national parks csv file
#Returns: A list of dictionary objects where the keys are the strings from the header rows and the values are the information from the file
#Description: This function reads in the file and creates a list of dictionary objects with all of the information from the CSV file
def readParksFile(fileName = "national_parks.csv"):
    #creates an empty list
    parkList = []
    #opens the file and reads in the header line, strips header line of white space and splits it using commas
    fIn = open(fileName, "r")
    header = fIn.readline()
    header = header.strip()
    keysList = header.split(",")
    #for each line in the file, strip each line and split it with a comma
    for line in fIn:
        dict = {}
        line = line.strip()
        tempList = line.split(",")
        #for each key in the list of keys, find its index and append it to the appropriate dictionary
        for key in keysList:
            #for description, join and start at the indicies 7 till the end
            if key == "Description":
                dict[key] = ",".join(tempList[7:])
            #append dictionaries to the list
            else:
                 index = keysList.index(key)
                 dict[key] = tempList[index]
        parkList.append(dict)
    fIn.close()
    return parkList
#Parameters:dataStr is a string containing the date with dashes
#Returns:a string with the date in the correct format
#Description:This function turns the date format from (YYYY-MM-DD) to (Month day, year)
def convertData(dataStr):
    #split the string at the dashes
    dataStr = dataStr.split("-")
    #create variables for the month,year, and day by accessing correspoinding indicies
    year = dataStr[0]
    month = dataStr[1]
    day = dataStr[2]
    #using branching, numbers are matched with the correct months
    if dataStr[1] == "01":
        month = "January"
    elif dataStr[1] == "02":
        month = "Febuary"
    elif dataStr[1] == "03":
        month = "March"
    elif dataStr[1] == "04":
        month = "April"
    elif dataStr[1] == "05":
        month = "May"
    elif dataStr[1] == "06":
        month = "June"
    elif dataStr[1] == "07":
        month = "July"
    elif dataStr[1] == "08":
        month = "August"
    elif dataStr[1] == "09":
        month = "September"
    elif dataStr[1] == "10":
        month = "October"
    elif dataStr[1] == "11":
        month = "November"
    elif dataStr[1] == "12":
        month = "December"
    #creates a string with the date in the correct format
    date = month + " " + day + ", " +year
    return date
#Parameters:parkList is a list of dictionary objects that store park information
#Returns: string that is the park code of the larges tpark
#Description:This function determines the largest park in terms of acres and retruns the code of the park
def getLargestPark(parkList):
    code = ""
    #set the max to a really low number so it can be used for comparison
    max = -10
    #for each park in the list of parks, set the value equal to the acres of that park and compare the to eachother
    for parks in parkList:
        value = int(parks["Acres"])
        #if the park has a larger acres than the current max, set the park equal to the max
        if value > max:
            max = value
            code = parks["Code"]
    return code
#Parameters:parkList is a list of dictionary objects that store park information
#Returns: string that is the park code of the oldest park
#Description:This function determines the oldest park in terms of the year
def printOldestPark(parksList):
    code = ""
    #make the value really high for comparison
    min = 10000
    for park in parksList:
        #split the date by dashes and just access the year
        date = park["Date"].split("-")
        year = date[0]
        #if the year is less than the minimum, replace the minimum with year and access it's code
        if int(year) < min:
            min = int(year)
            code = park["Code"]
    return code



