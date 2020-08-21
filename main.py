from turtle import *

# Create a player with their paddle and listen for inputs
class Player:
  # How much to move the paddle when user presses the corresponding key
  move_offset = 15 

  def __init__(self, speed, shape, color, initial_pos_x, initial_pos_y, up_key, down_key):
    # Create the turtle and set its characteristics
    self.player = Turtle()
    self.player.shape('rectangle')
    self.player.color(color)
    self.player.penup()
    self.player.goto(initial_pos_x, initial_pos_y)
    
    # Set up the screen and movement
    self.screen = Screen()
    self.screen.onkey(self.move_up, up_key)
    self.screen.onkey(self.move_down, down_key)
    self.screen.listen()
    
  # Movement
  def move_up(self):
    print("Moving up")
    self.player.sety(self.player.ycor() + self.move_offset)

  def move_down(self):
    print("Moving down")
    self.player.sety(self.player.ycor() - self.move_offset)

  def main(self):
    self.screen.mainloop()

# Encode information about the ball
class Ball:
  def __init__(self, speed, shape, color, initial_pos_x, initial_pos_y):
    ball = Turtle()
    ball.shape(shape)
    ball.color('white')
    ball.penup()
    ball.goto(initial_pos_x, initial_pos_y)

# Paddle information
paddle_width = 40
paddle_height = 10

# Screen
screen_width = 500
screen_height = 500
screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")

# Information about a custom shape
screen.register_shape("rectangle",[
  (paddle_width, paddle_height),
  (-paddle_width, paddle_height),
  (-paddle_width, -paddle_height),
  (paddle_width, -paddle_height)
])

# Create players
Player_A = Player(0, 'square', 'red', -250, 0, 'Up', 'Down')
Player_B = Player(0, 'square', 'blue', 250, 0, 'W', 'S')
Ball = Ball(0, 'circle', 'white', 0, 0)

Player_A.main()
Player_B.main()

