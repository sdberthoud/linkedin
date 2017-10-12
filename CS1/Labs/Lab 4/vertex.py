'''
filename: vertex.py
name: shane berthoud
date: november 8th 2014
course: cs1
purpose: to create the vertex class that shows the adjacent vertices with the vertexes name and location
'''
from cs1lib import *

RADIUS = 8
WIDTH = 3

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adjacent = []
    
    def draw(self, r, g, b):
        set_fill_color(r, g, b)
        disable_stroke()
        draw_circle(self.x, self.y, RADIUS)
    
    def draw_edge(self, vertex, r, g, b):
        enable_stroke()
        set_stroke_width(WIDTH)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex.x, vertex.y)
    
    def draw_neighbor_edges(self, r, g, b):
        for vertex in self.adjacent:
            self.draw_edge(vertex, r, g, b)
    
    def near_point(self, x, y):
        return abs(self.x - x) <= RADIUS and abs(self.y - y) <= RADIUS
        
        