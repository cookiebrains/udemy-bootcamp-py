from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def run():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
    is_race_on = False
    all_turtles = []
    user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
    for i in range(7):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-200, (150 - (i + 1) * 35))
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True
 
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    screen.exitonclick()
