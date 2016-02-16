# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

intial_ball_pos = [WIDTH / 2, HEIGHT / 2]

time = 0

vel = [0, 0]

# define event handlers
def draw(canvas):
    ball_pos = intial_ball_pos
    multi = 5
    ball_pos[0] = intial_ball_pos[0] + multi*vel[0]
    ball_pos[1] = intial_ball_pos[1] + multi*vel[1]
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    timer.start()
    global vel
    if key == simplegui.KEY_MAP["left"]:
        vel[0] = -1
    elif key == simplegui.KEY_MAP["right"]:
        vel[0] = 1
    elif key == simplegui.KEY_MAP["down"]:
        vel[1] = 1
    elif key == simplegui.KEY_MAP["up"]:
        vel[1] = -1
def keyup(key):
    global vel, time
    timer.stop
    vel = [0, 0]
    time = 0
    
def timer_handler():
    global time
    time += 0.001
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(1, timer_handler)
# start frame
frame.start()
