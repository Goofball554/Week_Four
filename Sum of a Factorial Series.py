aBound = int(input("Please enter a number: "))

def factorialTo(aBounds):
    theFactorial = 1
    
    for aFactorial in range(1, aBounds + 1):
        theFactorial = theFactorial*aFactorial

    return theFactorial

def sumTo(aBound):
    theSum = 0
    
    for aNumber in range(1, aBound + 1):
        theSum = theSum + 1/(factorialTo(aNumber))

    return theSum


print(sumTo(aBound))
