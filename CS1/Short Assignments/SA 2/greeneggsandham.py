from cs1lib import *

# makes shape color white
def set_fill_white():
    set_fill_color(1, 1, 1)

# makes shape color green
def set_fill_green():
    set_fill_color(0, 1, 0)

# makes border color blue
def set_stroke_blue():
    set_stroke_color(0, 0, 1)

# makes border color black
def set_stroke_black():
    set_stroke_color(0, 0, 0)

# ... makes the background red
def make_background_red():
    set_clear_color(1, 0, 0)
    clear()

# draws the entire drawing
def draw_green_eggs_and_ham():
    start_graphics(green_eggs_and_ham)

#this is the function that makes this all possible
def green_eggs_and_ham():
    # set background
    make_background_red()
    
    #prepare the plate and the eggs
    set_fill_white()
    set_stroke_black()
    set_stroke_width(2)
    
    #draw the plate
    draw_triangle(25, 175, 350, 375, 375, 25)
    
    #draw the eggs
    draw_ellipse(160, 210, 45, 25)
    draw_ellipse(275, 275, 45, 25)
    
    #prepare the ham and yolk and take the border off that and the ham bone
    set_fill_green()
    disable_stroke()
    
    #draw the yolk
    draw_circle(160, 210, 10)
    draw_circle(275, 275, 10)
    
    #draw the ham
    draw_ellipse(275, 145, 75, 45)
    
    #color and draw the ham bone
    set_fill_white()
    draw_circle(275, 145, 10)
    
    #set color of the fork
    enable_stroke()
    set_stroke_blue()
    
    #draw the fork
    draw_line(255, 50, 255, 125)
    draw_line(247, 125, 263, 125)
    draw_line(247, 125, 247, 145)
    draw_line(263, 125, 263, 145)
    draw_line(252, 125, 252, 145)
    draw_line(258, 125, 258, 145)
    
    #my signature
    set_stroke_black()
    set_stroke_width(1)
    draw_text("Shane Berthoud", 25, 375)
draw_green_eggs_and_ham()