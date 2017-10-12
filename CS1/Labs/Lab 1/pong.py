'''
filename: pong.py
name: shane berthoud
date: september 23rd? 2014
course: CS1
file purpose: lab 1 and to play a fully functional pong game
'''

from cs1lib import *

#set changeable window height
WINDOW_HEIGHT = 400
 
#set dimensions of paddles and how much they move
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
PADDLE_MOVE = 10

#set dimensions for the pong circle and how much it will move
CIRCLE_MOVE = 5
CX = WINDOW_HEIGHT/2
CY = WINDOW_HEIGHT/2
R = 10
        
#set variables for the position of the left paddle
LX = 0
LY = 0
        
#make second paddle variable to window height
RX = WINDOW_HEIGHT
RY = WINDOW_HEIGHT
        
#set all keys for play of game
LEFT_UP = "a"
LEFT_DOWN = "z"
RIGHT_UP = "k"
RIGHT_DOWN = "m"
QUIT = "q"
BEGIN_PLAY = " "
        

def main():
    ''' 
    this function specifies the drawing of the entire pong game, 
    with movements of the paddles, movements of the ball, winning and losing.
    '''
            
    #make variable that will be changed
    left_x = LX
    left_y = LY
    right_x = RX
    right_y = RY
    circle_x = CX
    circle_y = CY
    move_cx = CIRCLE_MOVE
    move_cy = CIRCLE_MOVE
    
    # set the background color
    set_clear_color(0, 0, 0)
    clear()
    
    #make things look better
    enable_smoothing()
    disable_stroke()
   
    #draw the paddles and the circle and set the fill color
    set_fill_color(1, 1, 1)
    draw_rectangle(left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(right_x, right_y, -PADDLE_WIDTH, -PADDLE_HEIGHT)
    draw_circle(circle_x, circle_y, R)
    
    #set variables to be changed within game in order to know the state of the game
    game_over = True
    right_player_wins = False
    left_player_wins = False
    
    #function remembered from lecture
    def point_in_rectangle(x, y, rx, ry, rw, rh):
        '''
        this function takes as parameter, an x and a y of a point and the dimensions (including x [rx], y [ry] 
        width [rw] and height [rh]) of a rectangle and checks to see if the point is in the rectangle.
        '''
        if x >= rx and x < rx + rw and y >= ry and y < ry + rh:
            return True
        else:
            return False
        
    # while loop that runs while window is open.
    while not window_closed():
        
        #clears the graphics window and prepares for the movement of paddles and ball, during play of game.
        clear()
        
        #quits the game if the key assigned to QUIT is pressed
        if is_key_pressed(QUIT):
            cs1_quit()
            
        #changes the state of game_over to False to begin a new game
        if is_key_pressed(BEGIN_PLAY):
            game_over = False
        
        #defines the variables moving_x and moving_y as the next place the circle is going to be
        moving_y = circle_y + move_cy
        moving_x = circle_x + move_cx
        
        #checks to see if moving_y is within the window, if it is outside of the boundaries, it changes the direction of the ball
        if moving_y - R < 0 or moving_y + R > WINDOW_HEIGHT:
            move_cy = -move_cy
            
        #checks if moving_x is within the boundaries, and if it is not, it changes to game over
        if moving_x - R < 0 or moving_x + R > WINDOW_HEIGHT:
            move_cx = 0
            game_over = True
            #changes either right or left player_wins to write on the screen whether left or right player has won.
            if moving_x - R < 0:
                right_player_wins = True
                left_player_wins = False
            if moving_x + R> WINDOW_HEIGHT:
                left_player_wins = True
                right_player_wins = False
        
        '''checks to see if the point on the radius of the rectangle is touching the paddle, if the point is within
        the rectangle, it changes the direction of the ball depending on where the ball hits the paddle. if the ball
        hits the paddle on its vertical side, it will change the x direction, moving it in the opposite direction
        if it hits the horizontal side, it changes the y direction, eliminating the phenomenon where the ball will
        enter the paddle for a second before ending the game.
        '''
        if point_in_rectangle(moving_x - R, moving_y, left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT):
            move_cx = -move_cx
        if point_in_rectangle(moving_x + R, moving_y, right_x-PADDLE_WIDTH, right_y-PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT):
            move_cx = -move_cx
        if point_in_rectangle(moving_x , moving_y + R, right_x-PADDLE_WIDTH, right_y-PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT):
            move_cy = -move_cy
        if point_in_rectangle(moving_x , moving_y - R, right_x-PADDLE_WIDTH, right_y-PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT):
            move_cy = -move_cy
        if point_in_rectangle(moving_x, moving_y - R, left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT):
            move_cx = -move_cx
        if point_in_rectangle(moving_x, moving_y + R, left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT):
            move_cx = -move_cx
        
        #defines what is seen when the game is not over, the paddles move, the ball moves and the game is in play.
        if not game_over:
            
            #gets rid of the borders on all shapes
            disable_stroke()
            
            #moves the paddles in a direction specified by the variable if that key is pressed
            if is_key_pressed(LEFT_DOWN) and left_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
                left_y += PADDLE_MOVE
            elif is_key_pressed(LEFT_UP) and left_y > 0:
                left_y -= PADDLE_MOVE
            if is_key_pressed(RIGHT_DOWN) and right_y < WINDOW_HEIGHT:
                right_y += PADDLE_MOVE
            elif is_key_pressed(RIGHT_UP) and right_y > PADDLE_HEIGHT:
                right_y -= PADDLE_MOVE
            
            #moves the circle down and to the right to begin the game, before any changes are made
            circle_y += move_cy
            circle_x += move_cx
            
            #redraws the shapes in a new position after the variables have been updated and sleeps for .02 seconds between
            draw_circle(circle_x, circle_y, R)
            draw_rectangle(left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT)
            draw_rectangle(right_x, right_y, -PADDLE_WIDTH, -PADDLE_HEIGHT)
            request_redraw()
            sleep(.02)
        
        '''sets the shapes during game over to their original places, resets variables, displays text of which 
        player won, and shows how to start a new game
        '''
        if game_over:
            if right_player_wins:
                enable_stroke()
                set_stroke_color(1, 1, 1)
                draw_text("GAME OVER, RIGHT PLAYER WINS", 205, 100, True)
            if left_player_wins:
                enable_stroke()
                set_stroke_color(1, 1, 1)
                draw_text("GAME OVER, LEFT PLAYER WINS", 205, 100, True)
            enable_stroke()
            set_stroke_color(1, 1, 1)
            draw_text("PRESS THE SPACE BAR TO START GAME", 210, 300, True)
            disable_stroke()
            draw_circle(CX, CY, R)
            draw_rectangle(LX, LY, PADDLE_WIDTH, PADDLE_HEIGHT)
            draw_rectangle(RX, RY, -PADDLE_WIDTH, -PADDLE_HEIGHT)
            request_redraw()
            sleep(.02)
            right_y = RY
            left_y = LY
            circle_x = WINDOW_HEIGHT/2
            circle_y = WINDOW_HEIGHT/2
            move_cx = CIRCLE_MOVE
            move_cy = CIRCLE_MOVE
            

start_graphics(main, "pong", WINDOW_HEIGHT, WINDOW_HEIGHT)