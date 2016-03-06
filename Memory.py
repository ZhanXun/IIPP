# implementation of card game - Memory

import simplegui
import random

numList = []
numList.extend(range(8))
numList.extend(range(8))
cardState = 16*[0]
state = 0
pos_1 = 0
pos_2 = 0
turn = 0
# helper function to initialize globals
def new_game():
    global cardState, state
    random.shuffle(numList)
    cardState = 16*[0]
    state = 0
    print numList
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, pos_1, pos_2, turn
    if state == 0:
        if cardState[pos[0]/50] == 0:
            pos_1 = pos[0]/50
            cardState[pos_1] = 1
            state = 1
    elif state == 1:
        if cardState[pos[0]/50] == 0:
            pos_2 = pos[0]/50
            cardState[pos_2] = 1
            state = 2
    else:
        if cardState[pos[0]/50] == 0:
            if numList[pos_1] == numList[pos_2]:
                cardState[pos_1] = 2
                cardState[pos_2] = 2
            else:
                cardState[pos_1] = 0
                cardState[pos_2] = 0
            pos_1 = pos[0]/50
            cardState[pos_1] = 1
            state = 1
            turn += 1
            label.set_text('Turns = ' + str(turn))
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 0
    for num in numList:
        canvas.draw_text(str(num), (10+50*i,65), 50, 'white')
        i += 1
    i = 0
    for state in cardState:
        if state == 0:
            canvas.draw_polygon([(50 * i, 0), (50 * i + 50, 0), 
                                 (50 * i + 50, 100), (50 * i,100)],
                                0.5, 'black', 'green')
        i += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
