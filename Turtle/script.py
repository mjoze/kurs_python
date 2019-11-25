import turtle
import random
import field

turtle.setup(1000, 600)
screen = turtle.Screen()

goalie = turtle.Turtle()
ball = turtle.Turtle()

ball.penup()
ball.shape("circle")
ball.shapesize(2)
ball.fillcolor("white")
ball.speed(1)
ball.setheading(180)

goalie.penup()
goalie.shape("turtle")
goalie.shapesize(2)
goalie.fillcolor("red")
goalie.speed(6)
goalie.setheading(90)
goalie.goto(-300, 0)



def kick():
    ball.setheading(180)
    angle = random.randint(0, 27)
    direction = random.randint(0, 1)

    if direction == 0:
        ball.left(angle)
    else:
        ball.right(angle)

    ball.forward(320)

    if goalie.distance(ball) < 35:
        ball.write("SAVE")
    else:
        ball.write("GOAL")

    ball.hideturtle()
    ball.speed(0)
    ball.home()
    ball.speed(1)
    ball.showturtle()


def goalieup():
    goalie.setheading(90)
    goalie.forward(5)


def goaliedown():
    goalie.setheading(270)
    goalie.forward(10)


screen.onkeypress(goalieup, "Up")
screen.onkeypress(goaliedown, "Down")
screen.onkey(kick, "k")

screen.listen()
screen.mainloop()
# screen.exitonclick()
