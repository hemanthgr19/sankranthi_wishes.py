import turtle

d=turtle.Turtle()
s=turtle.Screen()
s.setup(width= 1280 , height=900)


turtle.bgcolor("black")
turtle.screensize(1080,450)
d.speed(5)
d.pensize(5)
d.pencolor("white")
col = "white"
col1 = "brown"
col2 = "orange"

d.fillcolor(col1)
d.begin_fill()
d.right(90)
d.circle(120,180)
d.left(90)
d.forward(242)
d.end_fill()

d.fillcolor(col2)
d.begin_fill()
d.right(89)
#d.circle(-120,45)
#d.left(90)
#d.forward(50)
#d.right(135)
#d.forward(180)

d.circle(-120,30)
d.right(130)
d.forward(60)
d.left(130)
d.forward(63)

d.right(130)
d.forward(60)
d.left(130)
d.forward(63)

d.right(130)
d.forward(58)
d.left(130)
d.forward(60)

d.right(130)
d.forward(58)
d.left(130)
d.forward(60)

d.right(130)
d.forward(58)

d.left(140)
d.circle(90,38)

d.left(70)
d.forward(225)
d.end_fill()

#upper part of pot
d.fillcolor(col1)
d.begin_fill()
d.right(100)
d.circle(-110,30)

d.left(90)
d.forward(60)

d.right(138)
d.forward(225)
d.fillcolor(col)
d.begin_fill()
d.left(90)
d.circle(80,45)
d.left(-90)
d.circle(70,45)
d.right(10)
d.left(30)
d.circle(80,45)
d.left(-30)
d.circle(70,45)
d.right(10)

d.left(30)
d.circle(80,45)
d.left(-90)
d.circle(70,45)
d.right(10)
d.left(30)
d.circle(80,45)
d.left(-30)
d.circle(70,45)
d.right(10)


d.left(30)
d.circle(80,45)
d.left(-90)
d.forward(15)

d.right(-112)
d.forward(100)
d.right(-5)
d.forward(123)
d.end_fill()


d.right(130)
d.forward(60)
d.left(95)
d.circle(-150,30)
d.pendown()

d.pencolor("black")
d.left(120)
d.circle(360,230)
d.right(30)
d.forward(360)
d.pencolor("white")
style = ('Courier', 60, 'italic')
d.write("Happy Sankranthi", font=style, align = 'left' , move=True)


turtle.mainloop()





