from cs1lib import *

# function to run the chalkboard
def chalkboard():
    set_clear_color(0, 0, 0)
    enable_smoothing()
    clear()
    set_stroke_color(1, 1, 1)
    
    while not window_closed():
        set_stroke_width(2)
        while mouse_down():
            old_x = mouse_x()
            old_y = mouse_y()
            sleep(.02)
            draw_line(mouse_x(), mouse_y(), old_x, old_y)
            request_redraw()
        if is_key_pressed("r"):
            set_stroke_color(1, 0, 0)
        elif is_key_pressed("g"):
            set_stroke_color(0, 1, 0)
        elif is_key_pressed("b"):
            set_stroke_color(0, 0, 1)
        elif is_key_pressed("y"):
            set_stroke_color(1, 1, 0)
        elif is_key_pressed("e"):
            set_stroke_color(0, 0, 0)
        elif is_key_pressed("E"):
            clear()
            set_stroke_color(1, 1, 1)
        elif is_key_pressed("w"):
            set_stroke_color(1, 1, 1)

start_graphics(chalkboard, "My Chalkboard", 700, 700)
