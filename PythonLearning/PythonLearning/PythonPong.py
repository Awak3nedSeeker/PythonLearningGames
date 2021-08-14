# Simple Pong in Python 3 for Beginners

import turtle

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
Ball.dx = 2;
Ball.dy = 2;

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

Win.bye();