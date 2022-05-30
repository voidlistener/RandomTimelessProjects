# reference: https://www.youtube.com/watch?v=LH8WgrUWG_I&list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2&index=1&t=0s TokyoEdtech

import turtle as t
import winsound
# window
wn = t.Screen()
wn.bgcolor("black")
wn.setup(width = 1280, height = 1024)
wn.tracer(0)

# speed up

class Object:
    def __init__(self, x, y, dx, dy):
        self.pd = t.Turtle()
        self.pd.speed(0)
        self.pd.shape("square")
        self.pd.penup()
        self.pd.goto(x, y)
        self.dx = dx
        self.dy = dy
    def move(self):
        x = self.pd.xcor() + self.dx
        y = self.pd.ycor() + self.dy
        self.pd.goto(x, y)
    def move_inv(self):
        x = self.pd.xcor() - self.dx
        y = self.pd.ycor() - self.dy
        self.pd.goto(x, y)
    def amp(self, value):
        self.dx *= value
        self.dy *= value

# paddle

class Paddle(Object):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
        self.pd.color("#06038D")
        self.pd.shapesize(stretch_wid = 5, stretch_len = 1)


# ball

class Ball(Object):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
        self.pd.color("#00FFFF")
        self.pd.shapesize(stretch_wid = 1, stretch_len = 1)

# setup

pd1 = Paddle(-550, 0, 0, 20)
pd2 = Paddle(550, 0, 0, 20)
b = Ball(0, 0, 1, 1)
wn.listen()
wn.onkeypress(pd1.move, 'w')
wn.onkeypress(pd1.move_inv, 's')
wn.onkeypress(pd2.move, 'Up')
wn.onkeypress(pd2.move_inv, 'Down')

# score 

pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 472)
score_A = 0
score_B = 0
pen.write("Player A: {} Player B: {}".format(score_A, score_B), align = "center", font = ("Courier", 24, "normal"))

# game

while True:
    wn.update()
    b.move()
    b.amp(1.001)
    # controls

    

    # collisions
    p1x = pd1.pd.xcor()
    p1y = pd1.pd.ycor()
    p2x = pd2.pd.xcor()
    p2y = pd2.pd.ycor()
    bx = b.pd.xcor()
    by = b.pd.ycor()
    if by > 502:
        b.dy *= -1
        b.pd.sety(502)
        b.amp(0.8)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if by < -502:
        b.dy *= -1
        b.pd.sety(-502)
        b.amp(0.8)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if bx > 630:
        b.dx /= -b.dx
        b.dy /= -b.dy
        b.pd.goto(0, 0)
        score_A += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_A, score_B), align = "center", font = ("Courier", 24, "normal"))
    if bx < -630:
        b.dx /= -b.dx
        b.dy /= -b.dy
        b.pd.goto(0, 0)
        score_B += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_A, score_B), align = "center", font = ("Courier", 24, "normal"))
    if (abs(bx-p1x) < 20) and (abs(by-p1y) < 60):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        b.dx *= -1
        b.pd.setx(-530)
        b.amp(0.8)
    if (abs(bx-p2x) < 20) and (abs(by-p2y) < 60):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        b.dx *= -1
        b.pd.setx(530)
        b.amp(0.8)


