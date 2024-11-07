# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Lab 6

def main():
    #takes in users input
    word1 = input("Enter word #1: ")
    word2 = input("Enter word #2: ")
    #converts users input to lower case
    word1 = word1.lower()
    word2 = word2.lower()
    #strips each word of spaces
    string1 = word1.strip()
    string2 = word2.strip()
    string1 = string1.replace(" ","")
    string2 = string2.replace(" ","")
    #converts the words to lists
    list1 = list(string1)
    list2 = list(string2)
    #sorts both lists
    list1.sort()
    list2.sort()
    #if the lists are equal then they are anagrams, else they are not
    if list1 == list2:
        print("These words are anagrams!")
    else:
        print("These words are NOT anagrams.")
    #gets in a phrase from the user and converts it to lowercase
    phrase = input("\nEnter a phrase: ")
    phrase = phrase.lower()
    #replaces all spaces in the phrase with no space, removes all space
    phrase1 = phrase.replace(" ","")
    #converts phrase to a list and reverse the list
    list3 = list(phrase1)
    list3.reverse()
    #creates a string from the list
    newString = ''.join(list3)
    #compares the original phrase with the new string to determine if its a palindrome
    if newString == phrase1:
        print("This phrase is a palindrome!")
    else:
        print('This phrase is NOT a palindrome.')


















main()