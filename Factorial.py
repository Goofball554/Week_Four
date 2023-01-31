aBound = int(input("Please enter a number you would like to get the factorial of: "))

def sumTo(aBound):
    theSum = 1
    
    for aNumber in range(1, aBound + 1):
        theSum = theSum*aNumber

    return theSum

print(sumTo(aBound))
