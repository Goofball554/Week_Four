x = int(input("How many rows would you like?"))
y = int(input("How many columns would you like?"))


def printnums(x,y):
    for y in range(y):
        print("")
        for x in range(x):
            print(x+1, end="")

printnums(y, x)