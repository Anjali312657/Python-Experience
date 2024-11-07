# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Lab 3

def main():
    #prints the menu to the user initially and takes in user input
    print("What would you like to know?")
    print("a) Favorite Animal")
    print("f) Favorite Food")
    print("p) Favorite Place")
    print("q) Quit")
    answer = input("> ")
    #If statements print the statement depending on what the user enters & converts it to lower case so its not case sensitive
    if answer.lower() == "a":
        print("My favorite animal is a panda.")
    elif answer.lower() == "f":
        print("My favorite food is neopolitan pizza.")
    elif answer.lower() == "p":
        print("My favorite place is Honolulu, Hawaii.")
    elif answer.lower() == "q":
        print("Goodbye")
    else:
        print("This option is not available.")
    #While the user input is not q this loop will continuously print out the menu,check for input, and go thru if statements
    while answer.lower() != "q":
        print("\nWhat would you like to know?")
        print("a) Favorite Animal")
        print("f) Favorite Food")
        print("p) Favorite Place")
        print("q) Quit")
        answer = input("> ")
        # If statements print the statement depending on what the user enters & converts it to lower case so its not case sensitive
        if answer.lower() == "a":
            print("My favorite animal is a panda.")
        elif answer.lower() == "f":
            print("My favorite food is neopolitan pizza.")
        elif answer.lower() == "p":
            print("My favorite place is Honolulu, Hawaii.")
        elif answer.lower() == "q":
            print("Goodbye")
        else:
            print("This option is not available.")

main()