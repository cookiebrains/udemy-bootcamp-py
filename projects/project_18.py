from turtle import Turtle, Screen, colormode
import random
import colorgram

hirst_colors = colorgram.extract('hirst.JPG', 20)
hirst_rgb_colors = [(26, 108, 163), (193, 39, 81), (235, 161, 54), (234, 215, 87), (222, 138, 175), (142, 109, 58),
                    (104, 194, 217), (21, 57, 132), (204, 165, 30), (212, 75, 92), (237, 89, 51), (142, 208, 226),
                    (119, 191, 141), (106, 108, 197), (6, 185, 177), (7, 158, 89)]


def get_colors_from_image(colors):
    """
    Gets tuples of rgb from extracted variable
    :param colors:
    :return: list of rgb tuples
    """
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors


timmy = Turtle()

timmy.shape("turtle")


def dashed_line():
    for _ in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def draw_square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)


def same_length_side_shapes():
    counter = 3
    while counter < 11:
        timmy.color(random_color_from_list())
        angle = 360 / counter
        for _ in range(counter):
            timmy.forward(100)
            timmy.right(angle)
        counter += 1


def draw_a_random_walk(steps):
    colormode(255)
    timmy.pensize(10)
    angles = [0, 90, 180, 270]
    counter = 0
    while counter < steps + 1:
        timmy.speed('fast')
        timmy.color(random.choice(hirst_rgb_colors))
        timmy.forward(20)
        timmy.setheading(random.choice(angles))
        counter += 1


def generate_random_color():
    # generates random rgb for pencolor, but must set colormode to (255)
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    random_color = (r, g, b)
    return random_color


def random_color_from_list():
    colors = ['purple', 'aquamarine', 'firebrick', 'dodger blue', 'gold',
              'deep sky blue', 'dark turquoise']
    random_num = random.randint(0, 6)
    return colors[random_num]


def spirograph(size_of_gap):
    timmy.pensize(2)
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color_from_list())
        timmy.circle(90)
        timmy.right(size_of_gap)


def draw_one_circle():
    circle_color = random.choice(hirst_rgb_colors)
    timmy.color(circle_color, circle_color)
    timmy.begin_fill()
    timmy.circle(20)
    timmy.end_fill()


def hirst_copy():
    colormode(255)
    timmy.speed('fastest')
    timmy.penup()
    timmy.hideturtle()
    timmy.goto(-350, -350)
    for i in range(10):
        for j in range(10):
            draw_one_circle()
            timmy.penup()
            timmy.forward(70)
        timmy.goto(-350, (-350 + ((i + 1) * 70)))




def run():
    hirst_copy()
    my_screen = Screen()
    my_screen.exitonclick()
