from turtle import Turtle
class Snake(Turtle):
    speed = 2
    turtle_list = []
    direction = ""
    body_number = 3

    def __init__(self, body_number):
        super().__init__()
        x = 0
        y = 0
        self.body_number = body_number
        for i in range(0, body_number):
            turtle = Turtle(shape="square")
            turtle.penup()
            turtle.goto(x, y)
            turtle.shapesize(1, 1, 1)  # 2 * 20 = 40 pixels width
            self.turtle_list.append(turtle)
            x -= 20
            turtle.color("red")

    def reset(self):
        for snake in self.turtle_list:
            snake.goto(1000,1000)
        self.turtle_list = []
        self.clear()
        x = 0
        y = 0
        for i in range(0, self.body_number):
            turtle = Turtle(shape="square")
            turtle.penup()
            turtle.goto(x, y)
            turtle.shapesize(1, 1, 1)  # 2 * 20 = 40 pixels width
            self.turtle_list.append(turtle)
            x -= 20
            turtle.color("red")


    def setSpeed(self, speed):
        speed = speed

    def move(self):
        positions = []
        self.turtle_list[0].forward(20)
        for i in range(0, len(self.turtle_list)):
            positions.append((self.turtle_list[i].position(), self.turtle_list[i].heading()))
        for i in range(1, len(self.turtle_list)):
            self.turtle_list[i].setposition(positions[i - 1][0])
            self.turtle_list[i].setheading(positions[i - 1][1])

    def up(self):
        if not self.turtle_list[0].heading() == -90:
            self.turtle_list[0].setheading(90)
        self.direction = "up"

    def down(self):
        if not self.turtle_list[0].heading() == 90:
            self.turtle_list[0].setheading(-90)
        self.direction = "down"

    def left(self):
        if not self.turtle_list[0].heading() == 0:
            self.turtle_list[0].setheading(180)
        self.direction = "left"

    def right(self):
        if not self.turtle_list[0].heading() == 180:
            self.turtle_list[0].setheading(0)
        self.direction = "right"

    def extend(self):
        turtle = Turtle(shape="square")
        turtle.penup()
        tlen = len(self.turtle_list)
        x = 0
        y = 0
        if(self.turtle_list[len(self.turtle_list)-1].xcor() > self.turtle_list[len(self.turtle_list)-2].xcor()): # to the right
            x = self.turtle_list[len(self.turtle_list)-1].xcor() + 40
            y = self.turtle_list[len(self.turtle_list)-1].ycor()
        elif self.turtle_list[len(self.turtle_list)-1].xcor() < self.turtle_list[len(self.turtle_list)-2].xcor():
            x = self.turtle_list[len(self.turtle_list) - 1].xcor() - 40
            y = self.turtle_list[len(self.turtle_list) - 1].ycor()
        elif self.turtle_list[len(self.turtle_list)-1].ycor() > self.turtle_list[len(self.turtle_list)-2].ycor():
            x = self.turtle_list[len(self.turtle_list) - 1].xcor()
            y = self.turtle_list[len(self.turtle_list) - 1].ycor() + 40
        else:
            x = self.turtle_list[len(self.turtle_list) - 1].xcor()
            y = self.turtle_list[len(self.turtle_list) - 1].ycor() - 40
        turtle.goto(x, y)
        turtle.shapesize(1, 1, 1)  # 2 * 20 = 40 pixels width
        self.turtle_list.append(turtle)
        turtle.color("red")

    def check_coil(self):
        condition = False
        for i in range (2, len(self.turtle_list)):
            print(self.turtle_list[0].distance(self.turtle_list[i]))
            if self.turtle_list[0].distance(self.turtle_list[i]) < 4:
                condition = True
        return condition
