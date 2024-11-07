# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Lab 10
#this function reads the file and creates a dictionary of keys and the frequency of each letter
def readFile(fileName):
    #empty dictionary to store information
    dictionary = {}
    #reads the file
    fileIn = open(fileName,"r")
    #for each character in the file
    for char in fileIn:
        #strip the word of extra space and change it to lower case
        char = char.strip()
        char = char.lower()
        #for each letter in the word, check if its a letter and increase the frequency in the dictionary
        for letter in char:
            if letter.isalpha() == True:
                if letter in dictionary.keys():
                    dictionary[letter] += 1
                else:
                    dictionary[letter] = 1
    #close the file and return the dictionary
    fileIn.close()
    return dictionary
#this function sorts the dictionary alphabetically
def sortKeys(dictionary):
    #turns the dictionary into a list
    sorteddict = list(dictionary.keys())
    #sorts the list
    sorteddict.sort()
    return sorteddict
def main():
    #calls the function and stores it in variables
    dictionary = readFile("speech.txt")
    sortedList = sortKeys(dictionary)
    print("This frequency of letters are: ")
    #loops through each key and prints it out
    for key in sortedList:
        print(key," : ",dictionary[key])


main()