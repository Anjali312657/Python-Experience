# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Lab 8

#imports random module
import random
def coin():
    #assigns a variable to a random int of either 0 or 1
    flip = random.randrange(0,2)
    #if the random int is 0 assign the value heads, else if the random int is 1 assign the value tails
    if flip == 0:
        coin = "heads"
    elif flip == 1:
        coin = "tails"
    #returns heads or tails
    return coin
def experiment():
    #sets the number of flips and number of heads equal to 0
    numFlips = 0
    numHeads = 0
    #while there aren't three heads in a row, keep flipping and adjusting the counts
    while numHeads < 3:
        flips = coin()
        #if the flip equals heads, add 1 to the headcount and flipcount
        if flips == "heads":
            numHeads = numHeads + 1
            numFlips = numFlips + 1
        #if the flip equals tails, reset the heads count and add 1 to the flip count
        else:
            numHeads = 0
            numFlips = numFlips + 1
    #return the total number of flips
    return numFlips


def main():
    total = 0
    #calls the experiment function 10 times and adds the return value of the experiment funciton to create a total
    for i in range(10):
        flips = experiment()
        total = flips + total
    #calculates average number of flips it takes to get to 3 heads
    average = total / 10.0
    #outputs the number
    print("The average for 3 heads in a row is: " + str(average))

main()