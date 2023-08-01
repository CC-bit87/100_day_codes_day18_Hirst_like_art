import colorgram
import random
from turtle import Turtle, Screen

spot_bot = Turtle()
screen = Screen()
screen.colormode(255)
def color_extractor():
    # hent farvepalette fra et billede
    color_extract = colorgram.extract("spots.jpg", 100)
    # colorgram.extract returns Color objects, which let you access
    # RGB, HSL, and what proportion of the image was that color_extract.
    color_list_rgb = []

    for colors in color_extract:
        r = colors.rgb.r
        g = colors.rgb.g
        b = colors.rgb.b
        new_colors = (r, g, b)
        color_list_rgb.append(new_colors)

    print(color_list_rgb)


color_palette = [(240, 236, 229), (0, 0, 0), (208, 157, 107), (226, 236, 228), (124, 172, 194), (241, 227, 231),
    (30, 115, 154), (131, 180, 152), (144, 82, 55), (218, 227, 234), (230, 202, 114), (205, 135, 151), (157, 59, 79),
    (209, 75, 96), (40, 130, 87), (222, 80, 59), (178, 154, 53), (66, 162, 115), (236, 161, 173), (163, 28, 45), (34,
    162, 190), (164, 207, 185), (234, 170, 160), (14, 48, 75), (16, 96, 64), (148, 34, 26), (19, 65, 46), (71, 32, 47),
    (8, 92, 109), (159, 205, 214), (80, 73, 34), (28, 62, 117), (179, 189, 211), (108, 125, 161), (236, 200, 10)]

spot_bot.speed("fastest")
spot_bot.hideturtle()
spot_bot.penup()
y = -400
x = -500
spot_bot.setx(x)
spot_bot.sety(y)
no = True

while no:

    for spot in range(33):
        spot_bot.color(random.choice(color_palette))

        spot_bot.dot(15)
        spot_bot.penup()
        spot_bot.forward(30)
        spot_bot.pendown()
        spot_bot.dot(15)

    if y < 400:
        y += 30
        spot_bot.penup()
        spot_bot.sety(y)
        spot_bot.setx(x)
        print(round(spot_bot.ycor(), 5))
    else:
        no = False




screen.exitonclick()