from turtle import Turtle, Screen
import random

tutty = Turtle()
tutty.shape("turtle")
tutty.color("blue")

tutta = Turtle()
tutta.shape("turtle")
tutta.color("orange")

while True:
    tutty.forward(10)
    tutty.right(random.randint(-45,45))
    tutta.forward(10)
    tutta.right(random.randint(-45,45))

my_screen = Screen()
my_screen.exitonclick()
