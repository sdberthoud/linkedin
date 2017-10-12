'''
filename: map_plot.py
name: shane berthoud
date: november 11th 2014
course: cs 001
purpose: plots the map and the shortest path from one point on the map to another.
'''

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

def main():
    start = None     # sets the parameters for bfs
    goal = None

    vertex_dict = load_graph("dartmouth_graph.txt")   # makes the dictionary for vertices
    image = load_image("dartmouth_map.png")           # loads the map for plotting
    
    enable_smoothing()
    
    while not window_closed():
        draw_image(image, 0, 0)
        for key in vertex_dict:                        # draws the points on the map and draws the edges between them in blue
            vertex_dict[key].draw_neighbor_edges(0, 0, 1)
            vertex_dict[key].draw(0, 0, 1)
            
        # makes the point that will later be the goal point, the point near the mouse
        found = None
        for key in vertex_dict:
            if vertex_dict[key].near_point(mouse_x(), mouse_y()):
                found = vertex_dict[key]
                break
        
        # makes the start vertex the clicked vertex    
        if mouse_down():
            start = found
        
        # makes the goal vertex the vertex that is closest to the mouse, and draws the start vertex in red.
        if start != None:
            start.draw(1, 0, 0)
            goal = found
        
        if start != None and goal != None:   # only runs this if there is a start and goal vertex.
            path = bfs(start, goal)
            previous = goal
            
            # draws the path in red and the vertices in the path in red
            for vertex in path:
                vertex.draw(1, 0, 0)
                vertex.draw_edge(previous, 1, 0, 0)
                previous = vertex
                
        request_redraw()
        sleep(.02)
start_graphics(main, "Map of Dartmouth", WINDOW_WIDTH, WINDOW_HEIGHT)    
    