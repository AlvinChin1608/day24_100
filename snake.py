from turtle import Turtle

# Constants for starting positions, move distance, and direction angles
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        """Initialize the snake with segments and set the head."""
        self.segments = []  # List to hold all segments of the snake
        self.create_snake()  # Create the initial snake body
        self.head = self.segments[0]  # The head is the first segment

    def create_snake(self):
        """Create the snake's initial body segments at predefined positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")  # Create a new segment
        new_segment.color("white")  # Set segment color to white
        new_segment.penup()  # Lift pen to prevent drawing lines
        new_segment.goto(position)  # Move segment to the starting position
        self.segments.append(new_segment)  # Add segment to the list

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # The head is the first segment

    def extend(self):
        """Add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by moving each segment to the position of the segment ahead."""
        # Move each segment to the position of the segment in front of it, starting from the tail
        for seg_num in range(len(self.segments) - 1, 0, -1):  # (start=2, stop=0, step=-1)
            new_x = self.segments[seg_num - 1].xcor()  # Get x-coordinate of the segment ahead
            new_y = self.segments[seg_num - 1].ycor()  # Get y-coordinate of the segment ahead
            self.segments[seg_num].goto(new_x, new_y)  # Move current segment to the new position
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        """Change the snake's direction to up if it's not currently moving down."""
        if self.head.heading() != DOWN:  # Prevent the snake from reversing
            self.head.setheading(UP)  # Set the heading to up

    def down(self):
        """Change the snake's direction to down if it's not currently moving up."""
        if self.head.heading() != UP:  # Prevent the snake from reversing
            self.head.setheading(DOWN)  # Set the heading to down

    def left(self):
        """Change the snake's direction to left if it's not currently moving right."""
        if self.head.heading() != RIGHT:  # Prevent the snake from reversing
            self.head.setheading(LEFT)  # Set the heading to left

    def right(self):
        """Change the snake's direction to right if it's not currently moving left."""
        if self.head.heading() != LEFT:  # Prevent the snake from reversing
            self.head.setheading(RIGHT)  # Set the heading to right
