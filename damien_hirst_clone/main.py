import colorgram
import turtle as turtle_module
import random

def extract_colors(image):
    colors = colorgram.extract(image, 20)
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if (r < 245 and g < 245 and b < 245):
            color_list.append((r,g,b))
    return color_list

# TODO extract colors
# TODO Draw Dots
# TODO 10 by 10, 20px wide circles spaced aport by 50px


color_list = extract_colors('dame_time2.jpg')
directions = {'east': 0, 'northeast': 45, 'north': 90, 'northwest': 135,
              'west': 180, 'southwest': 225, 'south': 270, 'southeast': 315}

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")


# tim.setheading(directions['southwest'])
# tim.forward(500)
# tim.setheading(directions['east'])
x = -300
y = -300
tim.penup()
def paint_row():
    for i in range (10):
        tim.dot(20, random.choice(color_list))

        tim.forward(50)


for i in range (10):
    tim.setx(x)
    tim.sety(y)
    paint_row()
    y += 50






canvas = turtle_module.Screen()
canvas.exitonclick()