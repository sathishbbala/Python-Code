from turtle import Turtle, Screen
import random
colors = ["DarkOrchid", "DeepSkyBlue", "Gold", "LimeGreen", "Tomato", "OrangeRed", "MediumVioletRed", "Turquoise"]
tim = Turtle()
tim.pensize(2)
tim.speed('fastest')
timmy = Turtle()
tommy = Turtle()
def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)  

def random_walk(steps):
    directions = [0, 90, 180, 270]
    tim.pensize(10)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
    tim.forward(steps)  

# this did not work need to check why it is not working 
# using the colors list to choose a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(num_circles, size_of_gap):
    for _ in range(int(num_circles)):
        tim.color(random.choice(colors))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

def move_forward():
    tim.forward(10) 

def move_backward():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home() 
    tim.pendown()
# Example usages: the example below to draw a spirograph
#draw_spirograph(100,10)

timmy.color("blue")
timmy.shape("turtle")

tommy.color("red")
tommy.shape("turtle")   


screen = Screen()
#screen.listen()
#screen.onkey(key = "W", fun = move_forward)
#screen.onkey(key = "S", fun = move_backward)
#screen.onkey(key = "A", fun = turn_left)
#screen.onkey(key = "D", fun = turn_right)
#screen.onkey(key = "C", fun = clear)
screen.title("Turtle Graphics")
screen.setup(width=1000, height=600)
screen.exitonclick()




