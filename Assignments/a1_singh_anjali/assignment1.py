# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 1
# Description: This program displays two truths and a lie
def main():
    #Sets the first and last variable to a string of my first name and my last name
    first = "Anjali"
    last = "Singh"

    #Sets each statement variable to a string of either a truth or a lie
    statement1 = "I have never been stung by a bee."
    statement2 = "I have never been outside of the country."
    statement3 = "I have never broken a bone."

    #Sets each truth variable to a boolean of true or false
    truth1 = True
    truth2 = False
    truth3 = True

    #Sets each pet and sibling to an integer representing how many pets and siblings I have
    pets = 0
    siblings = 1

    #Prints my full name by concatenating the first and last string variables
    print("Full Name: " + first + " " + last)

    #Adds a new line and prints the number of pets by concatenating a string and casting the integer of 0 to a string
    print("\nNumber of pets: " + str(pets))

    # Prints the number of siblings by concatenating a string and casting the integer of 1 to a string
    print("Number of siblings: " + str(siblings))

    #Adds a new line. The print statement prints each statement that is stores in each varaible. It concatenates a string with another string
    print("\nStatement 1: " + statement1)
    print("Statement 2: " + statement2)
    print("Statement 3: " + statement3)

    #Adds a new line. The print statement prints whether each statement is true or false. It concatenates a string with a boolean that is casted into a string
    print("\nStatement 1 is " + str(truth1))
    print("Statement 2 is " + str(truth2))
    print("Statement 3 is " + str(truth3))


main()