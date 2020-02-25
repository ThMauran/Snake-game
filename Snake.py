import turtle, random, time

#Screen

wn = turtle.Screen()
wn.bgcolor("green")
wn.setup(width = 700, height = 700)
wn.title("Snake Game, by ThM")

#Variables
vitesse = 10
vie = 1
tailleDuTerrain = 350
cursorSize = 14
score = 0
ancienScore = score / 2 
segments = []
wn.tracer(0)


#Head
class turtleHead(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.speed(0)
        self.shape("square")
        self.direction = "stop"
        self.pu()
    
    def move(self):
        global vie
        if self.xcor() > tailleDuTerrain - cursorSize-8 or self.xcor() < - tailleDuTerrain + cursorSize or self.ycor() > tailleDuTerrain - cursorSize or self.ycor() < -tailleDuTerrain + cursorSize+8:
            vie = 0
        if self.direction == "up" and self.direction != "down":
            y = self.ycor() 
            self.sety(y + vitesse)

        if self.direction == "down":
            y = self.ycor()
            self.sety(y - vitesse) 

        if self.direction == "left":
             x = self.xcor()
             self.setx(x - vitesse)
        if self .direction == "right":
            x = self.xcor()
            self.setx(x + vitesse)
    def go_up(self):
        self.direction = "up"
    def go_down(self):
        self.direction = "down"
    def go_left(self):
        self.direction = "left"
    def go_right(self):
        self.direction = "right"
    
class Food(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.shape("circle")
        self.pu()
        self.speed(0)

    def respawn(self):
        newX = random.randint(-tailleDuTerrain + cursorSize, tailleDuTerrain - cursorSize)
        newY = random.randint(-tailleDuTerrain + cursorSize, tailleDuTerrain - cursorSize)
        self.goto(newX, newY)

class Segment(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("grey")
        self.pu()
        self.shape("square")
        self.speed(0)


#Assiniation des objets à des variables
head = turtleHead()
food = Food()
food.respawn()

def distance(t1, t2):
    global score
    if t1.distance(t2) < cursorSize:
        score += 100
        food.respawn()
        newSegement = Segment()
        segments.append(newSegement)





wn.listen()
wn.onkey(head.go_up, "Up")
wn.onkey(head.go_down, "Down")
wn.onkey(head.go_left, "Left")
wn.onkey(head.go_right, "Right")





while vie > 0:
    time.sleep(0.02)
    wn.update()
    head.move()


    distance(food, head)

    if score > ancienScore*2:
        ancienScore = score
        vitesse += 0.5

    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)




wn.mainloop()
