from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.hideturtle()
        self.go_to_start()
        self.showturtle()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
    def back(self):
        self.backward(MOVE_DISTANCE)

    def player_score(self):
        self.setpos(STARTING_POSITION)

    def go_to_start(self):
        self.setpos(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
