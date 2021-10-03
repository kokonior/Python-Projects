import turtle
import random

colors = ["blue", "red", "green"]

y_cord = [0, -100, 100]

all_turtles = []

speeds = [3, 2, 5]

turtle.setup(width=900, height=400)
user_bet = turtle.textinput("Which colour do you bet on, Green, yellow or red?", "Give your bet here:")

for i in range(3):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.speed(speeds[i])
    t.penup()
    t.goto(-425, y_cord[i])
    all_turtles.append(t)

race = 1

while race == 1:
    for x in all_turtles:
        a = random.randint(5, 20)
        x.forward(a)
        t_pos = x.xcor()
        if t_pos >= 425:
            print("The winning turtle is", x.pencolor())
            if user_bet == x.pencolor():
                print("You are correct!")
            else:
                print("You are incorrect")
            race = 0
