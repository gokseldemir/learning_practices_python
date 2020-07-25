import turtle
t = turtle.Turtle()
win=turtle.Screen()
win.bgcolor("purple")
while True:
    for c in ["darkorange", "green", "yellow", "blue"]:             
        t.shape("turtle")
        t.width(15)
        t.color(c)
        t.forward(75)
        t.left(60)
        
