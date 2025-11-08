from turtle import Turtle, Screen
import random
colors = ["DarkOrchid", "DeepSkyBlue", "Gold", "LimeGreen", "Tomato", "OrangeRed", "MediumVioletRed", "Turquoise"]
tim = Turtle()

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)  

def random_walk(steps):
    directions = [0, 90, 180, 270]
    tim.pensize(10)
    tim.speed('fastest')
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
    tim.forward(steps)  

for i in range(200):
    random_walk(30)   



