# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
# Table Information
WIDTH = 600
HEIGHT = 400
# Ball Information
BALL_RADIUS = 20
INITIAL_BALL_POSITION = [WIDTH / 2, HEIGHT / 2]
ball_pos = list(INITIAL_BALL_POSITION)
ball_vel = [0, 0]
ball_acc = 0
# Pad Information
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
# pad vertical position 
paddle1_pos = [HEIGHT / 2 - PAD_HEIGHT /2, 
               HEIGHT / 2 + PAD_HEIGHT /2]
paddle2_pos = [HEIGHT / 2 - PAD_HEIGHT /2, 
               HEIGHT / 2 + PAD_HEIGHT /2]
paddle1_vel = 0
paddle2_vel = 0

LEFT = False
RIGHT = True
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, ball_acc# these are vectors stored as lists
    ball_pos = list(INITIAL_BALL_POSITION)
    ball_acc = 0
    if direction:
        ball_vel = [1, 2*random.random()-1]
    else:
        ball_vel = [-1, 2*random.random()-1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(random.randrange(0, 2))

def draw(canvas):
    global score1, score2, paddle1_vel, paddle2_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] = ball_pos[0] + math.sqrt(ball_acc) * ball_vel[0]
    ball_pos[1] = ball_pos[1] + math.sqrt(ball_acc) * ball_vel[1]
    
    #print ball_pos
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")       
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0] = paddle1_pos[0] + paddle1_vel
    paddle1_pos[1] = paddle1_pos[1] + paddle1_vel
    paddle2_pos[0] = paddle2_pos[0] + paddle2_vel
    paddle2_pos[1] = paddle2_pos[1] + paddle2_vel
    # draw paddles
    # paddle1
    canvas.draw_polygon([(0, paddle1_pos[0]), 
                         (PAD_WIDTH, paddle1_pos[0]), 
                         (PAD_WIDTH, paddle1_pos[1]), 
                         (0, paddle1_pos[1])], 1, 'Green', 'White')
    # paddle2
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos[0]), 
                         (WIDTH, paddle2_pos[0]), 
                         (WIDTH, paddle2_pos[1]), 
                         (WIDTH - PAD_WIDTH, paddle2_pos[1])], 1, 'Green', 'White')

    # determine whether paddle and ball collide    
    # ball collide
    if ball_pos[0] < BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] > paddle1_pos[0] and ball_pos[1] < paddle1_pos[1] :
            ball_vel[0] = - ball_vel[0]
            print ball_pos[1]
            print paddle1_pos
        else:
            score2 += 1
            spawn_ball(LEFT)
    if ball_pos[0] > WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] > paddle2_pos[0] and ball_pos[1] < paddle2_pos[1] :
            ball_vel[0] = - ball_vel[0]
        else:
            score1 += 1
            spawn_ball(RIGHT)
    if ball_pos[1] < BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # paddle collide    
    if paddle1_pos[0] < 0:
        paddle1_vel = 0
        paddle1_pos[0] = 0
        paddle1_pos[1] = PAD_HEIGHT
    if paddle1_pos[1] > HEIGHT:
        paddle1_vel = 0
        paddle1_pos[0] = HEIGHT - PAD_HEIGHT
        paddle1_pos[1] = HEIGHT
    if paddle2_pos[0] < 0:
        paddle2_vel = 0
        paddle2_pos[0] = 0
        paddle2_pos[1] = PAD_HEIGHT
    if paddle2_pos[1] > HEIGHT:
        paddle2_vel = 0
        paddle2_pos[0] = HEIGHT - PAD_HEIGHT
        paddle2_pos[1] = HEIGHT
        
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 2 - 50 - int(frame.get_canvas_textwidth(str(score1), 48) / 2), 50], 48, 'white')
    canvas.draw_text(str(score2), [WIDTH / 2 + 50 - int(frame.get_canvas_textwidth(str(score2), 48) / 2), 50], 48, 'white')

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

def timer_ball_handler():
    global ball_acc
    ball_acc += 1;
    
def button_start_handler():
    
    if not timer_ball.is_running():
        timer_ball.start()
        new_game()
    
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer_ball = simplegui.create_timer(1000, timer_ball_handler)
button_start = frame.add_button("Strat/Restart", button_start_handler, 100)


# start frame
new_game()
frame.start()
