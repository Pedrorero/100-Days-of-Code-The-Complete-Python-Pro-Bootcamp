import turtle as t
import random

tim = t.Turtle()

colours = ["blue", "lawn green", "dark red", "orchid", "dark goldenrod", "tomato", "turquoise", "dark slate blue",
           "yellow"]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


