#Simple pong in python
import turtle

# win stands for window
win = turtle.Screen()
win.title("Pong by Tejas")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)
# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  #Turtle() is class name
paddle_a.speed(0)           #speed(0) is for animation speed and setting it on 0 is for max. possible speed
paddle_a.shape("square")
paddle_a.color("cyan")
paddle_a.shapesize(stretch_wid = 5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()  #Turtle() is class name
paddle_b.speed(0)           #speed(0) is for animation speed and setting it on 0 is for max. possible speed
paddle_b.shape("square")
paddle_b.color("cyan")
paddle_b.shapesize(stretch_wid = 5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()  #Turtle() is class name
ball.speed(0)           #speed(0) is for animation speed and setting it on 0 is for max. possible speed
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
 #Now I want to seperate the ball movement into x and y coordinate movement
ball.dx = 0.5             #dx means change in x
ball.dy = 0.5             #dy means change in y

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# Function
def paddle_a_up():      #To move this paddle using keyboard
    y = paddle_a.ycor() #ycor() returns the y coordinate cuz to move the paddle up, y coordinate is required
    y +=20              #allows the paddle to move 20 pixels upwards
    paddle_a.sety(y)    #sety() function sets the new value to y i.e in sety(y)

def paddle_a_down():      #To move this paddle using keyboard
    y = paddle_a.ycor() #ycor() returns the y coordinate cuz to move the paddle down, y coordinate is required
    y -=20              #allows the paddle to move 20 pixels downwards
    paddle_a.sety(y)    #sety() function sets the new value to y i.e in sety(y)

def paddle_b_up():      #To move this paddle using keyboard
    y = paddle_b.ycor() #ycor() returns the y coordinate cuz to move the paddle up, y coordinate is required
    y +=20              #allows the paddle to move 20 pixels upwards
    paddle_b.sety(y)    #sety() function sets the new value to y i.e in sety(y)

def paddle_b_down():      #To move this paddle using keyboard
    y = paddle_b.ycor() #ycor() returns the y coordinate cuz to move the paddle down, y coordinate is required
    y -=20              #allows the paddle to move 20 pixels downwards
    paddle_b.sety(y)    #sety() function sets the new value to y i.e in sety(y)

# Keyboard Binding
win.listen()            #takes keyboard input
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()            #Everytime the loop runs update() function updates the screen
    

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:   # This helps to prevent ball from escaping 
        ball.sety(290)      # in upward direction
        ball.dy *= -1       # This reverses the ball direction
    
    if ball.ycor() < -290:  # This helps to prevent ball from escaping 
        ball.sety(-290)     # in downward direction
        ball.dy *= -1       # This reverses the ball direction

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1