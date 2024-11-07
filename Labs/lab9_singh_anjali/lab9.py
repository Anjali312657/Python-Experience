# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Lab 9

def readFile(userGenre, fileName):
    #reads the file in
    fileIn = open(fileName,"r")
    #empty list that will eventually hold the shows
    showList = []
    for line in fileIn:
        # for each line in the file, it strips and splits the file and seperates them into two columns
        line = line.strip()
        data_list = line.split(",")
        showName = data_list[0]
        showGenre = data_list[1]
        #if the user-specificed genre is the genre of the show then append the name
        if userGenre in showGenre:
            showList.append(showName)
    #close file and return the list of shows
    fileIn.close()
    return showList
def writeFile(genre,showList):
    #name the file based on the genre and open the file
    fileName = genre + ".txt"
    fileOut = open(fileName, "w")
    #writes list to a file
    for show in showList:
        print(show, file=fileOut)

def main():
    #prints out possible genres
    print("TV Shows")
    genre = "action & adventure, animation,comedy, documentary, drama, mystery & suspense, science fiction & fantasy"
    print("Possible genres are", genre)
    keepRunning = True
    #while loop keeps asking until user enters a valid genre
    while keepRunning:
        userChoice = input("Enter a genre: ")
        if userChoice in genre:
            keepRunning = False
    #reads the file based on user input and writes TV shows to a file
    listOfShows = readFile(userChoice,"shows.csv")
    writeFile(userChoice,listOfShows)
    print("The file",userChoice,".txt","has the following shows:")
    print(listOfShows)
    
main()

