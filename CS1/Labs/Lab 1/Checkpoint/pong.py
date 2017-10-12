from cs1lib import *

#set changeable window height
WINDOW_HEIGHT = 400

def main():
    ''' draws the pong game
    parameters: none
    returns: nothing, without startgraphics(), with startgraphics draws pong and makes it function.
    '''
    # set the background color
    set_clear_color(0, 0, 0)
    clear()
    
    #make things look beter
    enable_smoothing()
    disable_stroke()
    
    #set dimensions of paddles and how much they move
    PADDLE_WIDTH = 20
    PADDLE_HEIGHT = 80
    PADDLE_MOVE = 10
        
    #set variables for the position of the paddles
    LX = 0
    LY = 0
        
    #make second paddle variable to window height
    RX = WINDOW_HEIGHT
    RY = WINDOW_HEIGHT
        
    #make variable that will be changed
    left_x = LX
    left_y = LY
    right_x = RX
    right_y = RY
        
    #set directions for paddles
    LEFT_UP = "a"
    LEFT_DOWN = "z"
    RIGHT_UP = "k"
    RIGHT_DOWN = "m"
        
    #draw the paddles and set them to variables
    set_fill_color(1, 1, 1)
    draw_rectangle(left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(right_x, right_y, -PADDLE_WIDTH, -PADDLE_HEIGHT)
    
    # while loop that runs while window is open.
    while not window_closed():
       
        
        # move the paddles, all comments in first if applies to all elif
        if is_key_pressed(LEFT_DOWN) and left_y < WINDOW_HEIGHT - 80:
            # clear the paddles
            clear()
            
            #move the paddle by 10
            left_y += PADDLE_MOVE
            
            #redraw the rectangles with new y coordinate
            draw_rectangle(left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT)
            draw_rectangle(right_x, right_y, -PADDLE_WIDTH, -PADDLE_HEIGHT)
            
            #redraw and then sleep
            request_redraw()
            sleep(.02)
        elif is_key_pressed(LEFT_UP) and left_y > 0:
            clear()
            left_y -= PADDLE_MOVE
            draw_rectangle(left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT)
            draw_rectangle(right_x, right_y, -PADDLE_WIDTH, -PADDLE_HEIGHT)
            request_redraw()
            sleep(.02)
        elif is_key_pressed(RIGHT_DOWN) and right_y < WINDOW_HEIGHT:
            clear()
            right_y += PADDLE_MOVE
            draw_rectangle(left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT)
            draw_rectangle(right_x, right_y, -PADDLE_WIDTH, -PADDLE_HEIGHT)
            request_redraw()
            sleep(.02)
        elif is_key_pressed(RIGHT_UP) and right_y > 80:
            clear()
            right_y -= PADDLE_MOVE
            draw_rectangle(left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT)
            draw_rectangle(right_x, right_y, -PADDLE_WIDTH, -PADDLE_HEIGHT)
            request_redraw()
            sleep(.02)

start_graphics(main, "pong", WINDOW_HEIGHT, WINDOW_HEIGHT)