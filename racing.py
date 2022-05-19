from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("TURTLE RACING")

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race (red, blue, orange, yellow, green or purple)? Enter a color: ")

colors = ["red", "blue", "orange", "yellow", "green", "purple"]
turtles =[]


# REFEREE TURTLE
ref = Turtle(shape="turtle")
ref.fillcolor("grey")
ref.penup()
ref.setheading(90)
ref.goto(x=225,y=-100)
ref.pendown()
ref.goto(x=225,y=100)
ref.penup()
ref.goto(x=225, y=150)
ref.setheading(270)



for ii in range(6):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[ii])
    turtle.penup()
    turtle.goto(x=-225, y=(-75+(ii*30)))
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 205:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color is: {winning_color}.")
            else:
                print(f"You've lost! The winning color is: {winning_color}.")


        random_distance = random.randint(1,3)
        turtle.forward(random_distance)

screen.exitonclick()
