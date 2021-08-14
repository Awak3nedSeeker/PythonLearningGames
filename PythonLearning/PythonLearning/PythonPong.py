# Simple Pong in Python 3 for Beginners
# Sound should be .wav

import turtle
import winsound

Win = turtle.Screen();
Win.title("HI");
Win.bgcolor("black");
Win.setup(width=800, height=600);
Win.tracer(0);

Canvas = Win.getcanvas();
Root = Canvas.winfo_toplevel();

def Quit():
    global Running;
    Running = False;

Root.protocol("WM_DELETE_WINDOW", Quit);


Running = True;

# Score
Score_A = 0;
Score_B = 0;

# Paddle A
Paddle_A = turtle.Turtle();
Paddle_A.speed(0);
Paddle_A.shape("square");  
Paddle_A.color("white");
Paddle_A.shapesize(stretch_wid=5, stretch_len=1);
Paddle_A.penup();
Paddle_A.goto(-350, 0);

# Paddle B
Paddle_B = turtle.Turtle();
Paddle_B.speed(0);
Paddle_B.shape("square");  
Paddle_B.color("white");
Paddle_B.shapesize(stretch_wid=5, stretch_len=1);
Paddle_B.penup();
Paddle_B.goto(350, 0);

# Ball
Ball = turtle.Turtle();
Ball.speed(0);
Ball.shape("square");  
Ball.color("white");
Ball.penup();
Ball.goto(0, 0);
Ball.dx = 0.25;
Ball.dy = 0.25;

# Pen
Pen = turtle.Turtle();
Pen.speed(0);
Pen.color("white");
Pen.penup();
Pen.hideturtle();
Pen.goto(0, 260);
Pen.write("Player A: 0 | Player B: 0", align="center", font=("Comics Sans", 24, "normal"))

# Function
def Paddle_A_Up():
    y = Paddle_A.ycor();
    y += 20;
    Paddle_A.sety(y);

def Paddle_A_Down():
    y = Paddle_A.ycor();
    y -= 20;
    Paddle_A.sety(y);

def Paddle_B_Up():
    y = Paddle_B.ycor();
    y += 20;
    Paddle_B.sety(y);

def Paddle_B_Down():
    y = Paddle_B.ycor();
    y -= 20;
    Paddle_B.sety(y);

# Keyboard Binding
Win.listen();
Win.onkeypress(Quit, "Escape");
Win.onkeypress(Paddle_A_Up, "w");
Win.onkeypress(Paddle_A_Down, "s");
Win.onkeypress(Paddle_B_Up, "Up");
Win.onkeypress(Paddle_B_Down, "Down");

# Main Game Loop
while Running:
    Win.update();

    # Move the Ball
    Ball.setx(Ball.xcor() + Ball.dx);
    Ball.sety(Ball.ycor() + Ball.dy);

    # Border Checking
    if Ball.ycor() > 290:
        Ball.sety(290);
        Ball.dy *= -1;
        # winsound.PlaySound("Bounce.wav", winsound.SND_ASYNCH)

    if Ball.ycor() < -290:
        Ball.sety(-290);
        Ball.dy *= -1;

    if Ball.xcor() > 390:
        Ball.goto(0, 0);
        Ball.dx *= -1;
        Score_A += 1;
        Pen.clear();
        Pen.write("Player A: {} | Player B: {}".format(Score_A, Score_B), align="center", font=("Comics Sans", 24, "normal"))


    if Ball.xcor() < -390:
        Ball.goto(0, 0);
        Ball.dx *= -1;
        Score_B += 1;
        Pen.clear();
        Pen.write("Player A: {} | Player B: {}".format(Score_A, Score_B), align="center", font=("Comics Sans", 24, "normal"))

    # Padle and Ball Collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < Paddle_B.ycor() +50 and Ball.ycor() > Paddle_B.ycor() - 50):
        Ball.setx(340);
        Ball.dx *= -1;

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < Paddle_A.ycor() +50 and Ball.ycor() > Paddle_A.ycor() - 50):
        Ball.setx(-340);
        Ball.dx *= -1;

Win.bye();
