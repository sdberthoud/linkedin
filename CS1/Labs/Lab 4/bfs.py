'''
filename: bfs.py
name: shane berthoud
date: november 10th 2014
course: cs 001
purpose: to have the function that makes the paths for each vertex
'''

from vertex import Vertex
from collections import deque
from mhlib import PATH

def bfs(start, goal):
    '''this is the defining function of the entire map_plot.py file. this function takes every point and puts them into the
    deque, then checks what the next point is, pulls the previous point of the deque, and gets the shortest path.'''
    visited = {}             # the dictionary that stores the points that have been visited
    campus = deque()         # the deque that makes the function possible, it stores the vertices that will be visited
    
    campus.append(start)     # puts the first vertex in the queue
    
    prev_point = {}          # the dictionary that stores the previous points to each vertex
    prev_point[start] = None # there is no previous point for the first point ...
    
    while len(campus) > 0:   # if there are still points to visit, it will keep going
        vertex = campus.popleft()
        visited[vertex] = True    # the vertex has been visited
        if vertex == goal:   # when the path is done, retrace.
            path = []        # stores the path so it can be drawn
            while vertex != None: # adds the point if it is not the starting point
                path.append(vertex)
                vertex = prev_point[vertex]   # makes the next vertex the previous vertex from the current vertex
            return path
        else:                # if the path isn't done, keep it going.
            for point in vertex.adjacent:
                if not point in visited and not point in campus:  # makes sure the vertex hasn't been visited and it's not on campus already
                    prev_point[point] = vertex                    # makes a previous point for each vertex
                    campus.append(point)
    return None