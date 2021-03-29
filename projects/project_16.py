from turtle import Turtle, Screen
from prettytable import PrettyTable


def run():
    # timmy = Turtle()
    # timmy.shape("turtle")
    # timmy.color("red")
    # timmy.forward(100)
    #
    # my_screen = Screen()
    # my_screen.exitonclick()
    table = PrettyTable()

    table.add_column("Pokemon Name", ['Balbasaur', 'Pikachu', 'Charmander'])
    table.add_column("Type", ['Electric', 'Water', 'Fire'])
    table.align = "l"
    print(table)
