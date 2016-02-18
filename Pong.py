# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
# Table Information
WIDTH = 600
HEIGHT = 400
# Ball Information
BALL_RADIUS = 20
INITIAL_BALL_POSITION = [WIDTH / 2, HEIGHT / 2]
ball_pos = INITIAL_BALL_POSITION
ball_vel = [0, 0]
# Pad Information
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = [HEIGHT / 2 - PAD_HEIGHT /2, HEIGHT / 2 + PAD_HEIGHT /2]
paddle2_pos = [HEIGHT / 2 - PAD_HEIGHT /2, HEIGHT / 2 + PAD_HEIGHT /2]
paddle1_vel = 0
paddle2_vel = 0
LEFT = False
RIGHT = True
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = INITIAL_BALL_POSITION
    if RIGHT:
        ball_vel = [1, 1]
    if LEFT:
        ball_vel = [-1, 1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = INITIAL_BALL_POSITION[0] + ball_vel[0]
    ball_pos[1] = INITIAL_BALL_POSITION[1] + ball_vel[1]
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")       
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
