'''
filename: visualize_cities.py
name: shane berthoud
date: november 6th 2014
course: cs1
purpose: draws the 50 most populated cities in order.'''

from cs1lib import *

WINDOW_WIDTH = 720      # sets variables for variables that will not change
WINDOW_HEIGHT = 360     
DOT_SIZE = 7                 
def main():
    img = load_image("world.png")               # loads the map for the background
    f = open('cities_population.txt', 'r')      # opens the cities_population.txt file to plot the points on the map

    put_on_map = []                             # list to check if the points are already on the map
    for line in f:                              
        if len(put_on_map) > 50:                # makes sure there are only 50 points.
            break           
        param = line.strip().split(',')
        
        
        clear()
        draw_image(img, 0, 0)                    # draws the map
        for city in put_on_map:                  # draws the cities in the list put_on_map 
            disable_stroke()
            set_fill_color(1, 0.5, 0)   
            draw_rectangle(city[0] - (DOT_SIZE / 2), city[1] - (DOT_SIZE / 2), DOT_SIZE, DOT_SIZE)
        
        center_x = int(round((WINDOW_WIDTH / 2) + (WINDOW_WIDTH / 2) * (float(param[3]) / 180)))      # converts the latitude and longitude of the cities to pixels
        center_y = int(round((WINDOW_HEIGHT / 2) + (WINDOW_HEIGHT / 2) * (float(param[2]) / 90)))
        
        request_redraw()
        sleep(0.25)

        put_on_map.append([center_x, center_y])  # puts the cities on the map.

    f.close()   # closes the file
    request_redraw()
    
start_graphics(main, "The World", WINDOW_WIDTH, WINDOW_HEIGHT, True)