"""
Name: Kristina Rydbom
bumper.py

Problem: HW 8  ---------

Certification of Authenticity:
I certify that this assignment is entirely my own work.
# """
from graphics import *
# from random import randint


def main():
    # window
    w = 700
    h = 500

    win = GraphWin("Bumper!", w, h)

    x1 = 300
    y1 = 200
    x2 = 500
    y2 = 400

    point_a = Point(x1, y1)
    point_b = Point(x2, y2)

    ball = Circle(point_a, 40)
    ball.setFill("purple")
    ball.setOutline("purple")

    ball2 = Circle(point_b, 40)
    ball2.setFill("green")
    ball2.setOutline("green")

    # draw!
    ball.draw(win)
    ball2.draw(win)

    for i in range(500):
        ball.move(-10, 0)
        ball2.move(10, 0)
        time.sleep(0.1)
        # if y1 == 500 or y1 == 0:
        #     ball.move(10, 0)
        if (x1 == 700) or (x1 == 0):
            ball.move(10, 0)


    win.getMouse()
#
    win.getMouse()

    win.close()

# import turtle
# # Set key parameters
# gravity = -0.005  # pixels/(time of iteration)^2
# y_velocity = 1  # pixels/(time of iteration)
# x_velocity = 0.25  # pixels/(time of iteration)
# energy_loss = 0.95
# width = 600
# height = 800
# # Set window and ball
# window = turtle.Screen()
# window.setup(width, height)
# window.tracer(0)
# ball = turtle.Turtle()
# ball.penup()
# ball.color("green")
# ball.shape("circle")
# # Main loop
# while True:
#     # Move ball
#     ball.sety(ball.ycor() + y_velocity)
#     ball.setx(ball.xcor() + x_velocity)
#     # Acceleration due to gravity
#     y_velocity += gravity
#     # Bounce off the ground
#     if ball.ycor() < -height / 2:
#         y_velocity = -y_velocity * energy_loss
#         # Set ball to ground level to avoid it getting "stuck"
#         ball.sety(-height / 2)
#     # Bounce off the walls (left and right)
#     if ball.xcor() > width / 2 or ball.xcor() < -width / 2:
#         x_velocity = -x_velocity
#     window.update()


if __name__ == '__main__':

    main()
