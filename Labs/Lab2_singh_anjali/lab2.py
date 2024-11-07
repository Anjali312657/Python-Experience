# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
#Lab 2

def main():
    #Takes in year the user enters and casts it to an int
    year = int(input("Enter the year: "))
    #Determines what animal you are depending on the modulous divison calculation
    if (year-2000) % 12 == 0:
        sign = "Dragon"
    elif (year - 2000) % 12 == 1:
        sign = "Snake"
    elif (year - 2000) % 12 == 2:
        sign = "Horse"
    elif (year - 2000) % 12 == 3:
        sign = "Goat"
    elif (year - 2000) % 12 == 4:
        sign = "Monkey"
    elif (year - 2000) % 12 == 5:
        sign = "Rooster"
    elif (year - 2000) % 12 == 6:
        sign = "Dog"
    elif (year - 2000) % 12 == 7:
        sign = "Pig"
    elif (year - 2000) % 12 == 8:
        sign = "Rat"
    elif (year - 2000) % 12 == 9:
        sign = "Ox"
    elif (year - 2000) % 12 == 10:
        sign = "Tiger"
    else:
        sign = "Rabbit"
    #Prints the message that tells the user what sign they are
    print(year,"is the Year of the " + sign + ".")

main()
