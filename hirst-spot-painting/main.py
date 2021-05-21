import turtle as t
import random as r
t.colormode(255)
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
tim.hideturtle()


for i in range(84):
    random_color = r.choice(color_list)
    tim.dot(10, random_color)
    tim.penup()
    tim.forward(15)
    if tim.xcor() == 180:
        tim.goto(0, tim.ycor() + 15)

screen = t.Screen()
screen.exitonclick()