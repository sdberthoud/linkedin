from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

TIME_SCALE = 1000000
PIXELS_PER_METER = 3 / 3e9

FRAME_RATE = 30
TIMESTEP = 1.0 / FRAME_RATE

def main():
    sun = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0)
    mercury = Body(3.295e23, 5.791e7 * 1000, 0, 0, 47890, 2, .596, .596, .596)
    venus = Body(4.867e24, 1.082e8 * 1000, 0, 0, 35040, 4, 1, .5, 0)
    earth = Body(5.972e24, 1.496e8 * 1000, 0, 0, 29790, 5, 0, 0, 1)
    mars = Body(6.39e23, 2.279e8 * 1000, 0, 0, 24140, 3, 1, 0, 0)
    
    solar_system = System([sun, mercury, venus, earth, mars])
    
    set_clear_color(0, 0, 0)
    enable_smoothing()
    
    while not window_closed():
        clear()
        solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
        solar_system.update(TIMESTEP * TIME_SCALE)
        request_redraw()
        sleep(TIMESTEP)
        
start_graphics(main, "solar system", WINDOW_WIDTH, WINDOW_HEIGHT)