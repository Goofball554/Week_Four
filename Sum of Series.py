def sumTo(aBound):
    theSum = 0
    for aNumber in range(1, aBound + 1):
        theSum = theSum + 1/aNumber

    return theSum

print(sumTo(4))

print(sumTo(1000))