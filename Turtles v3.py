import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()
z = 0

for i in range(3):  # repeat four times
    for aColor in ["yellow", "red", "purple", "blue", "green", "pink", "orange", "grey", "black"]:
        alex.color(aColor)
        alex.forward(z)
        alex.left(z)
        z = z + 1
    

wn.exitonclick()