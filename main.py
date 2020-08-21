from turtle import *

# Create a player with their paddle
class Player:
  # # of pixels to move the paddle each time the user presses something
  move_offset = 15 

  # Provide initial information:
  # speed - of the turtle object
  # shape
  # color
  # initial positions of the object (x, y)
  # size of the object (x, y)
  def __init__(self, speed, shape, color, initial_pos_x, initial_pos_y):
    player = Turtle()
    player.shape('rectangle')
    player.color(color)
    player.penup()
    player.goto(initial_pos_x, initial_pos_y)

  #def move_paddle(direction):
  def move_up():
    new_y = player.ycor() + move_offset
    player.sety(new_y)

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

# Key inputs
screen.onkey(Player.move_up, 'Up')
#screen.onkey(Player.move_down, "Down")

# Information about a custom shape
screen.register_shape("rectangle",[
  (paddle_width, paddle_height),
  (-paddle_width, paddle_height),
  (-paddle_width, -paddle_height),
  (paddle_width, -paddle_height)
])

# Create players
Player_A = Player(0, 'square', 'red', -250, 0)
Player_B = Player(0, 'square', 'blue', 250, 0)
Ball = Ball(0, 'circle', 'white', 0, 0)

screen.listen()
screen.mainloop()
