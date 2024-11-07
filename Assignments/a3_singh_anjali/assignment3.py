# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 3
# Description:
#This program creates a Harry Potter vending machine
#It determines the change and gives a discount

def main():
    #prints out the menu that the user can select from and takes in their choice
    print("Please select an item from the vending machine:")
    print("\ta) Assortment of Candy for 11 sickles and 7 knuts")
    print("\tb) Butterbeer for 2 sickles")
    print("\tc) Quill for 6 sickles")
    print("\td) Daily Prophet for 5 knuts")
    choice = input("Choice: ")
    #if else statements that allows lower or upper case entry and assigns an item and cost variable
    if choice.lower() == "a":
        item = "Assortment of Candy"
        cost = 326
    elif choice.lower() == "b":
        item = "Butterbeer"
        cost = 58
    elif choice.lower() == "c":
        item = "Quill"
        cost = 174
    elif choice.lower() == "d":
        item = "Daily Prophet"
        cost = 5
    #Else statement incase the user enters an option not given and assigns an option that I chose
    else:
        print("You entered an invalid choice, this the item selected is the Quill")
        item = "Quill"
        cost = 174
    #asks the uesr to enter the amount and type of payment they're using
    print("\nPlease pay by entering the number of each coin")
    galleons = int(input("Number of galleons: "))
    sickles = int(input("Number of sickles: "))
    knuts = int(input("Number of knuts: "))
    #converts sickles and galleons to knuts
    sicklesConversion = sickles * 29
    galleonsConversion = galleons * 493
    #Adds the conversions and converts them to knuts
    payment = galleonsConversion + sicklesConversion + knuts
    #Outputs the cost in knuts of the item chosen and the payment after conversion to knuts
    print("\nCost in Knuts: " + str(cost))
    print("Payment in knuts: " + str(payment))

    #If the payment is greater than or equal to the cost, this calculates the change
    if int(payment) >= cost:
        # Prints what item what purchased
        print("\nYou purchased the", item)
        change = payment - cost
        #Prints change in knuts
        print("Your change is " + str(change) + " knuts")
        #Converts galleons, sickles, and knuts back into their categories using modulo and regular divison
        galleonChange = change // 493
        sickleChange = change // 29
        knutChange = change % 29
        #prints the change given for each type of coin
        print("You will be given")
        print("\tGalleons: " + str(galleonChange))
        print("\tSickles: " + str(sickleChange))
        print("\tKnuts: " + str(knutChange))
        #if the payment is less than the cost tell the user they won't recieve the item
    elif int(payment) < cost:
        print("You did not enter enough money and will not receive the Quill")

main()
