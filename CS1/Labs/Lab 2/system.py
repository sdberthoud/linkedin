'''
filename: system.py
name: shane berthoud
date: october 21st, 2014
purpose: to create the system class in order to have the bodies work together and be easier to draw and change velocities/positions.
'''

from cs1lib import *
from math import sqrt
from body import Body

class System:
    def __init__(self, body_list):
        self.body_list = body_list
    
    def draw(self, cx, cy, pixels_per_meter):
        # iterates through the items in body_list and draws each item in the list.
        for n in range(len(self.body_list)):
            self.body_list[n].draw(cx, cy, pixels_per_meter)
    
    # method that computes accelerations for each planet.
    def compute_acceleration(self, n):
            a_x = 0
            a_y = 0
            # iterates through the planets in order to compute the effect of the acceleration by the other planets.
            for i in range(len(self.body_list)):
                G = 6.67394e-11
                M = self.body_list[i].get_mass()
                r = self.distance( self.body_list[i].get_x(), self.body_list[n].get_x(), self.body_list[i].get_y(), self.body_list[n].get_y() )
                dx = self.body_list[i].get_x() - self.body_list[n].get_x()
                dy = self.body_list[i].get_y() - self.body_list[n].get_y()
                # makes sure the acceleration isn't computed if the planets are the same.
                if i < n or i > n:
                    a = (G * M) / (r * r)
                    a_x += (a * dx) / r
                    a_y += (a * dy) / r
            return (a_x, a_y)
    
    # method made in order to make computing the accelerations easier
    def distance(self, x1, x2, y1, y2):
        disx = x1 - x2
        disy = y1 - y2
        return sqrt(disx ** 2 + disy ** 2)
    
    # updates the accelerations, velocities, and positions of all planets.
    def update(self, timestep):
        # computes the accelerations and updates the velocity of all planets first.
        for p in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(p)
            self.body_list[p].update_velocity(ax, ay, timestep)
        # then updates position of all planets.
        for p in range(len(self.body_list)):
            self.body_list[p].update_position(timestep)