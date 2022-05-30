# reference: https://www.youtube.com/watch?v=BP7KMlbvtOo&list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ&index=1&t=0s TokyoEdtech

import turtle as t
import time
import random as r

delay = 0.2

# screen


tile_s = 30
width, height = 40*tile_s, 30*tile_s
high_score = 0

class Object():
    def __init__(self, pos_x, pos_y, dir):
        self.s = t.Turtle()
        self.s.speed(0)
        self.s.penup()
        self.s.goto(pos_x, pos_y)
        self.s.direction = dir
    def move(self):
        if self.s.direction == "up":
            y = self.s.ycor()
            self.s.sety(y + tile_s)
        elif self.s.direction == "down":
            y = self.s.ycor()
            self.s.sety(y - tile_s)
        elif self.s.direction == "left":
            x = self.s.xcor()
            self.s.setx(x - tile_s)
        elif self.s.direction == "right":
            x = self.s.xcor()
            self.s.setx(x + tile_s)
        else:
            pass

# snake

class Snake_Head(Object):
    def __init__(self, pos_x, pos_y, dir = "right"):
        super().__init__(pos_x, pos_y, dir)
        self.s.color("darkgreen")
        self.s.shape("square")
        self.s.shapesize(stretch_wid = tile_s/20, stretch_len = tile_s/20)
    def go_up(self):
        if self.s.direction != "down":
            self.s.direction = "up"
    def go_down(self):
        if self.s.direction != "up":
            self.s.direction = "down"
    def go_left(self):
        if self.s.direction != "right":
            self.s.direction = "left"
    def go_right(self):
        if self.s.direction != "left":
            self.s.direction = "right"
 

class Snake_Body(Object):
    def __init__(self, pos_x, pos_y, dir = "right"):
        super().__init__(pos_x, pos_y, dir)
        self.s.color("green")
        self.s.shape("square")
        self.s.shapesize(stretch_wid = tile_s/20, stretch_len = tile_s/20)

class Snake():
    def __init__(self, pos_x, pos_y):
        self.body = []
        self.body.append(Snake_Head(pos_x, pos_y))
        for i in range(1, 3):
            self.body.append(Snake_Body(pos_x - i*tile_s, pos_y))
    def incollision_check(self):
        for i in range(1, len(self.body)):
            if self.body[0].s.distance(self.body[i].s) < tile_s:
                return True
        return False
    def advance(self):
        self.body[0].move()
        for i in range(1, len(self.body)):
            self.body[i].move()
        for i in range(len(self.body)-1, 0, -1):
            if self.body[i].s.direction != self.body[i-1].s.direction:
                self.body[i].s.direction = self.body[i-1].s.direction
    def grow(self):
        x = self.body[-1].s.xcor()
        y = self.body[-1].s.ycor()
        self.body.append(Snake_Body(x, y, "stop"))

# walls

class Wall(Object):
    def __init__(self, pos_x, pos_y, size_X, size_Y, dir = "stop"):
        super().__init__(pos_x, pos_y, dir)
        self.s.color("black")
        self.s.shape("square")
        self.size_X = size_X
        self.size_Y = size_Y
        self.s.shapesize(stretch_wid = size_Y*tile_s/20, stretch_len = size_X*tile_s/20)
# food

class Food(Object):
    def __init__(self, pos_x, pos_y, dir = "stop"):
        super().__init__(pos_x, pos_y, dir)
        self.s.color("red")
        self.s.shape("circle")
        self.s.shapesize(stretch_wid = tile_s/20, stretch_len = tile_s/20)

# setup

def setup():
    global wn, s, f, walls, flag, score, pen

    wn = t.Screen()
    wn.title = ("SNAKE")
    wn.bgcolor ("white")
    wn.setup(width + 100*tile_s/20, height + 100*tile_s/20)
    wn.tracer(0)

    s = Snake(0, 0)

    f = Food(0, 5*tile_s)

    score = 0

    walls = []
    walls.append(Wall(0, height/2, width/tile_s, 1))
    walls.append(Wall(0, -height/2, width/tile_s, 1))
    walls.append(Wall(width/2, 0, 1, height/tile_s))
    walls.append(Wall(-width/2, 0, 1, height/tile_s))
    walls.append(Wall(0, height/2-7*tile_s, width/tile_s-16, 1))
    walls.append(Wall(0, -height/2+7*tile_s, width/tile_s-16, 1))
    walls.append(Wall(-width/2+8*tile_s, height/2-9*tile_s, 1, 5))
    walls.append(Wall(width/2-8*tile_s, height/2-9*tile_s, 1, 5))
    walls.append(Wall(-width/2+8*tile_s, -height/2+9*tile_s, 1, 5))
    walls.append(Wall(width/2-8*tile_s, -height/2+9*tile_s, 1, 5))

    flag = False

    wn.listen()
    wn.onkeypress(s.body[0].go_up, "w")
    wn.onkeypress(s.body[0].go_down, "s")
    wn.onkeypress(s.body[0].go_left, "a")
    wn.onkeypress(s.body[0].go_right, "d")

    pen = t.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("blue")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 310*tile_s/20)
    
setup()

def collision_check(item):
    x = item.s.xcor()
    y = item.s.ycor()
    for wall in walls:
        if (abs(x-wall.s.xcor()) < tile_s*(wall.size_X+1)/2) and (abs(y-wall.s.ycor()) < tile_s*(wall.size_Y+1)/2):
            return True
            break

    return False
while True:
    pen.clear()
    pen.write("Score: {} High score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))
    wn.update()
    s.advance()
    if s.incollision_check():
        print("Body")
        flag = True

    if collision_check(s.body[0]):
        print("Border")
        flag = True

    if flag:
        if score > high_score:
            high_score = score
        del s
        del f
        walls.clear()
        del walls
        del flag
        wn.clearscreen()
        setup()
 
    if s.body[0].s.distance(f.s) < tile_s:
        score += 10
        while True:
            x = r.randint(-width/2+tile_s, width/2-tile_s)
            y = r.randint(-height/2+tile_s, height/2-tile_s)
            f.s.goto(x, y)
            if not collision_check(f):
                break
        s.grow()

    time.sleep(delay)

wn.mainloop()