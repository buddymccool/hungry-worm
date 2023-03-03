from turtle import Turtle

import scoreboard

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Worm:

    def __init__(self):
        self.segments = []
        self.make_a_worm()
        self.head = self.segments[0]
        self.current_seg = len(self.segments)

    def make_a_worm(self):
        for position in STARTING_POS:
            self.grow_worm(position)

    def grow_worm(self, position):
        new_seg = Turtle('square')
        new_seg.color('sienna4')
        new_seg.pensize(14)
        new_seg.fillcolor('LightPink')
        new_seg.shapesize(stretch_len=0.75, stretch_wid=0.75)
        new_seg.pu()
        new_seg.goto(position)
        if (len(self.segments) % 2) == 0:
            new_seg.fillcolor('LightPink2')
        self.segments.append(new_seg)
        new_seg.pd()

    def more_worm(self):
        self.grow_worm(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg_num - 1].xcor()
            newy = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newx, newy)
        self.head.fd(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
