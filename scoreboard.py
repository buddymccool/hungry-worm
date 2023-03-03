from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.points = 0
        self.pu()
        self.ht()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.points}", align=ALIGN, font=FONT)

    def plus_point(self):
        self.clear()
        self.points += 1
        self.write(f"Score: {self.points}", align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color('white')
        self.write(f"Game Over! Final Score: {self.points}", align=ALIGN, font=FONT)
