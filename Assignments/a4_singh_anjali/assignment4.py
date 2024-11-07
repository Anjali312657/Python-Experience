# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 4
# Description:
#This program allows the user to enter an unknown amount of numbers
#This program determines the smallest number entered and largest number entered by using variables
#and branching

def main():
    #Outer "do" while loop that resets the variables to zero and keeps the program running
    keepRunning = True
    while keepRunning:
        smallestNum = 0
        largestNum = 0
        count = 0
        sum = 0
        userNum = 0
        #Asks the user to input an integer
        print("Input an integer greater than or equal to 0 or -1 to quit")
        #Loop that runs while the user does not enter -1
        while userNum != -1:
            #Gets input from the user
            userNum = int(input("> "))
            #If statements that find the largest number and smallest number
            if userNum > largestNum:
                largestNum = userNum
            #if the smallest number is equal to 0, it sets the smallest number equal to the number that the user enters
            #Compares values and finds the smallest number
            if smallestNum == 0:
                smallestNum = userNum
            elif userNum < smallestNum and userNum != -1:
                smallestNum = userNum
            #Increases the count each time a number is entered and adds the number the user entered to the sum
            count += 1
            sum += userNum
            #Calculates average
            #If count is greater than 2, add one to the sum and subtract one from the count
            #You need to substract one from the account to not count "-1" as one of the numbers entered
            #You need to add one to not let the "-1" be added to the sum 

            if count > 2:
                avg = (sum + 1) / (count - 1)
            else:
                avg = sum/count
        #Prints the largest,smallest, and average
        print("The largest number is", largestNum )
        print("The smallest number is", smallestNum)
        print("The average number is", avg)
        #Asks the user if they want to enter more numbers
        #If the user doesn't enter yes then stop running the program and print goodbye
        startOver = input("\n Would you like to enter another set of numbers (y/n)?" )
        if startOver.lower() != "y":
            keepRunning = False
            print("\nGoodbye!")

main()