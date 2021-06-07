import turtle

bob = turtle.Turtle()
bob.pensize(10)
bob.speed(10)

#makes 'H'
bob.color("red")

bob.right(90)
bob.forward(200)
bob.left(180)
bob.forward(100)
bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(100)
bob.right(180)
bob.forward(200)
bob.penup()
bob.left(90)
bob.forward(25)

#makes 'e'
bob.color("orange")

bob.pendown()
bob.left(90)
bob.forward(100)
bob.right(90)
bob.forward(50)
bob.right(90)
bob.forward(50)
bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.penup()
bob.forward(25)

#makes 'l'
bob.color("yellow")

bob.pendown()
bob.left(90)
bob.forward(200)
bob.right(180)
bob.forward(200)
bob.left(90)
bob.penup()
bob.forward(25)

#makes 'l'
bob.color("green")

bob.pendown()
bob.left(90)
bob.forward(200)
bob.right(180)
bob.forward(200)
bob.left(90)
bob.penup()
bob.forward(25)

#makes 'o'
bob.color("blue")

bob.pendown()
for i in range(2):
    bob.forward(50)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
