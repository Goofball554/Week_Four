import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()
z = 0

for i in range(3):  # repeat four times
    for aColor in ["yellow", "red", "purple", "blue", "green", "pink", "orange", "grey"]:
        alex.color(aColor)
        alex.forward(50 + z)
        alex.left(90)
        z = z + 10
    

wn.exitonclick()
