# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Lab 1

def main():

    #Prints the quote and adds new lines to align the quote
    print("\"Do your little bit of good where you are; its those little bits of \n good put together that overwhelm the world.\" \n-Desmond Tutu")

    #Stores inputs in varaibles that pose questions to the user
    day = input("\nEnter the day of the week: ")
    month = input("Enter the month: ")
    date = int(input("Enter the date: "))

    #Prints sentences stating what day,month, and day of the week by concatenating variables
    #The integer was casted to the date
    print("\nToday is " + day + ", " + month + " " + str(date) + ".")

    #Prints a setenence that states tells the user what the day is tomorrow by concatenating variables and adding one to the date variable
    #The integer was casted to a string
    print("Tomorrow will be " + month + " " + str(date + 1) + ".")

main()