import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Merhaba Turtle!")
tess = turtle.Turtle()
#tess.shape("turtle")       #tess.shape("circle")
tess.color("red")

tess.pen()                # This is new - penup(), pendown()
size = 20
tess.shapesize(1, 1, 2)
for i in range(30):
   tess.stamp()            # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(24)           #  ...  and turn her
   

wn.mainloop()
