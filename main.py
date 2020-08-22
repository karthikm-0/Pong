from turtle import *
from random import randint, choice

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

  # Start the main loop which runs infinitely
  def main(self):
    self.screen.mainloop()

# Encode information about the ball
class Ball:
  # Constants that represent how fast the ball will move around the screen

  def __init__(self, speed, shape, color, initial_pos_x, initial_pos_y, width, height, Pl_A, Pl_B):
    self.ball = Turtle()
    self.ball.shape(shape)
    self.ball.color('white')
    self.ball.penup()
    self.ball.goto(initial_pos_x, initial_pos_y)
    self.ball.speed = speed
    self.ball.setheading(choice([0, 180]) + randint(-60, 60))

    # Displacement of ball in x and y
    #self.ball.dx = -self.BALL_DX
    #self.ball.dy = -self.BALL_DY

    # Screen
    self.screen = Screen()

  def move(self, Pl_A, Pl_B):
    self.ball.forward(self.ball.speed)
    #x_new = self.ball.xcor() + self.ball.dx
    #y_new = self.ball.ycor() + self.ball.dy
    #self.ball.setposition(x_new, y_new)
    #self.screen.mainloop()

    # Look for whether we have hit the boundaries and reset the ball and flip the direction the ball will move

    # Left-Paddle

    # Right-Paddle

  def distance(self, Pl_X):
    
    '''if self.ball.xcor() < - screen_width / 2:
      self.ball.setx(-screen_width / 2)
      #self.ball.dx = self.BALL_DX
      self.ball.setheading(-self.ball.heading())

    # X-right
    if self.ball.xcor() > screen_width / 2:
      self.ball.setx(-screen_width / 2)
      #self.ball.dx = -self.BALL_DX
      self.ball.setheading(-self.ball.heading())'''

    # Y-top
    if self.ball.ycor() > screen_height / 2:
      self.ball.sety(screen_height / 2)
      self.ball.setheading(-self.ball.heading())

      #self.ball.dy = -self.BALL_DY

    # Y-bottom
    if self.ball.ycor() < - screen_height / 2:
      self.ball.sety(-screen_height / 2)
      self.ball.setheading(-self.ball.heading())

      #self.ball.dy = self.BALL_DY
    
    # Check collision with either paddle
    # Paddle A
    #if self.ball.xcor() == Player_A.player.xcor():
      #print("Colliding with player A")
      #self.ball.dx = self.BALL_DX
    
    #elif self.ball.xcor() == Player_B.player.xcor():
      #print("Colliding with player B")
      #self.ball.dx = -self.BALL_DX

# Paddle information
paddle_height = 40
paddle_width = 10

# Screen
screen_width = 500
screen_height = 500
screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")

# Information about a custom shape
screen.register_shape("rectangle",[
  (paddle_height, paddle_width),
  (-paddle_height, paddle_width),
  (-paddle_height, -paddle_width),
  (paddle_height, -paddle_width)
])

# Create players
Player_A = Player(0, 'square', 'red', -250, 0, 'Up', 'Down')
Player_B = Player(0, 'square', 'blue', 250, 0, 'W', 'S')
Ball = Ball(5, 'circle', 'white', 0, 0, screen_width, screen_height, Player_A, Player_B)

Player_A.main()
Player_B.main()

#screen.listen()
#Ball.move(Player_A, Player_B)
#screen.mainloop()

#screen.ontimer(Ball.move(Player_A, Player_B), 50)
#Ball.main(Player_A, Player_B)

#screen.listen()
#screen.mainloop()

while(True):
  #print(Player_A.player.position())
  # Figure out how the ball should move next passing in the paddle's positions
  Ball.move(Player_A, Player_B)