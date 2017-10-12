'''
filename: body.py
name: shane berthoud
date: october 21st 2014
purpose: to create the body class for each planet to be made.
'''

from cs1lib import *

class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b
    
    # updates the x and y position of the body using the velocity
    def update_position(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep
    
    # updates the velocity of the x and y with an acceleration given by the system class.
    def update_velocity(self, ax, ay, timestep):
        self.vx += ax * timestep
        self.vy += ay * timestep
    
    # draws the bodies with respect to cx and cy being the center point of the solar system.
    def draw(self, cx, cy, pixels_per_meter):
        disable_stroke()
        set_fill_color(self.r, self.g, self.b)
        draw_circle(cx + self.x * pixels_per_meter, cy + self.y * pixels_per_meter, self.pixel_radius)
    
    # returns the mass of the body
    def get_mass(self):
        return self.mass
    
    # returns the x coordinate of the body
    def get_x(self):
        return self.x
    
    # returns the y coordinate of the body
    def get_y(self):
        return self.y