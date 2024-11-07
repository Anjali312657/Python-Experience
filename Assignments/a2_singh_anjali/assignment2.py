# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 2
# Description:
#This program creates a Mad Libs Story.
#It gets input from the user and prints output


def main():
    #These are the varaibles that hold all of the users inputs after they input different things
    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    num1 = int(input("Enter a number: "))
    noun2 = input("Enter a noun: ")
    num2 = float(input("Enter a number with a decimal point: "))
    adj2 = input("Enter an adjective: ")
    verb1 = input("Enter a verb ending in -ing: ")
    num3 = int(input("Enter a number: "))
    adj3 = input("Enter an adjective: ")
    num4 = int(input("Enter a number: "))
    verb2 = input("Enter a verb ending in -ing: ")

    #These lines print the story and place the users inputs within the story
    print("\nToday, I woke up feeling " + "\"" + adj1 + ".\"", end = " ")
    print("I couldn't wait to go to Hawaii with " + "\"" + noun1 + ".\"", end = " ")
    print("After landing, I waited in a line with about", "\"" + str(num1) + "\"", "people just to get on the shuttle to my hotel.")
    print("After arriving at the hotel, I ran into " + "\"" + noun2 + "\"" + " and we decided to go on a walk together", end = ". ")
    print("We stopped by a shaved ice shack and paid a whopping $" + "\"" + str(num2) + "\"", end = " dollars.\n ")
    print("\nAfter the long walk I was feeling " + "\"" + adj2 + ".\"",end = " ")
    print("I decided to go " + "\"" + verb1 + "\"" + " at the beach and watch the sunset",end = ". ")
    print("I met", "\"" + str(num3) + "\"" + " people just at the beach, it was so fun.")
    print("The sunset was " + "\"" + adj3 + ".\"" , end = " ")
    print("I met", "\"" + str(num4) + "\"", "people playing volleyball and decided to join",end = ". ")
    print("Just at the beach today, I met", "\"" + str(num3 + num4) + "\"" + " people alone!")
    print("My team won and to celebrate we went " + "\"" + verb2 + ".\"")

main()