# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 9
# Description:
#Write a language translator program that translates English words to another language using data from a CSV file

#Parameters:fileName is a string that has the default value of the name of the file
#Return Values:a list of the languages in the header row that are available to the user
#Description:this function geta a list of the languages in the header row of the file
def getAllLanguages(fileName = "languages.csv"):
    fIn = open(fileName, "r")
    header = fIn.readline()
    languageList = header.split(",")
    fIn.close()
    return languageList
#Parameters: a list of languages available to the user
#Return Values:a string of the language to translate words into
#Description:Displays the langauges to the user and allows the user to choose a language, checks if the language is valid
def getTranslationLanguage(languagesList):
    languagesList = languagesList[1:]
    print("Translate English words to one of the following languages: ",languagesList)
    keepRunning = True
    while keepRunning:
        choice = input("Enter a language: ").capitalize()
        if choice in languagesList:
            keepRunning = False
        else:
            print("This program does not support", choice.capitalize())
            choice = choice.capitalize()
    return choice
#Parameters: 1. list of the languages, 2. the string containing the name of the language which has a default value of english
#3. the name of the file which has a default value of languages.csv
#Return Values:a list of words in the language identified by the languagestr
#Description:this function reads through each line in the file, splits the data, and gets the correct word and appends it to the list
def readDataFile(languagesList,languageStr="English",fileName="languages.csv"):
    words = []
    fIn = open(fileName, "r")
    header = fIn.readline()
    index = languagesList.index(languageStr)
    for line in fIn:
        line = line.strip()
        dataList = line.split(",")
        words.append(dataList[index])
    fIn.close()
    return words
#Parameters:language is a string containing the name of the language
#Return Values:None
#Description:The variable writes a message to the text file
def createTextFile(language):
    language = language
    fileOut = open(language + ".txt", "w")
    print("Words translated from English to " + language, file=fileOut)
    fileOut.close()
#Parameters:1. a list of the words in english, 2. a list of the translated words, 3. a string containing the language of the translation
#Return Values:None
#Description:Checks if the word is able to be translates and translates the word, also writes to the text file
def translateWords(englishList,translationList,language):
    fileAppend = open(language + ".txt","a")
    keepRunning = True
    while keepRunning:
        word = input("\nEnter a word to translate: ")
        #if the word is not in the list, output this message
        if word not in englishList:
            print(word, "is not in the list")
        #if the word is in the list, get the index of the english word and match it to the index of the translated word
        else:
            index = englishList.index(word)
            translatedWord = translationList[index]
            #if word does not have a translation output a message
            if translatedWord == "-":
                print(word, "did not have a translation")
            #if the word has a translation, translate it and append a message to the text file
            else:
                print(word, "is translated to", translatedWord)
                print(word, "=", translatedWord, file=fileAppend)
        playAgain = input("Another word (y or n)? ")
        if playAgain.lower() != "y":
            keepRunning = False
            print("\nTranslated words have been saved to "+ language.capitalize() + ".txt")

    fileAppend.close()
#Parameters:none
#Return Values:none
#Description:Calls all of the functions and conducts the program
def main():
    print('Language Translator')
    #stores the list of possible languages
    languageList = getAllLanguages()
    #stores the lanuage the user selects
    choice = getTranslationLanguage(languageList)
    #stores a list of the english words
    englishWords = readDataFile(languageList)
    #stores a list of the translated words
    translatedWords = readDataFile(languageList,choice,"languages.csv")
    #writes text to the file
    createTextFile(choice)
    #translates the word and outputs messages to the user 
    translateWords(englishWords,translatedWords,choice)


main()