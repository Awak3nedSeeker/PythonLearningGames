# Simple Pong in Python 3 for Beginners
# Part 1: Getting started

import turtle

Win = turtle.Screen()
Win.title("HI")
Win.bgcolor("blue")
Win.setup(width=800, height=600)
Win.tracer(0)

def Quit():
    global Running
    Running = False

Win.listen()
Win.onkeypress(Quit, "q")

Running = True

# Main Game Loop
while Running:
    Win.update();

Win.bye()