from turtle import Turtle

# Changes to this file, reset the score board
# Tracking the previous high score record and keeping in a file

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize score to 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)  # Position the scoreboard at the top center
        self.hideturtle()  # Hide the turtle object
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.clear()  # Clear previous score text
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.score += 1

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        """ Update the high score by replacing the current scoreboard"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0 # reset to 0
        self.update_score()
