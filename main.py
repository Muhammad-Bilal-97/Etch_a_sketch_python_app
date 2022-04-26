from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # we can also use right function as well, both performs the same way


def turn_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    # we can also use left function as well, both performs the same way


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
