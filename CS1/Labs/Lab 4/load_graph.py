'''
filename: load_graph.py
name: shane berthoud
date: november 8th 2014
course: cs1
purpose: to define the function load_graph which puts all of the vertices in perspective and makes the connections between them'''

from vertex import Vertex

def load_graph(filename):
    # a function that takes a filename as parameter, opens the file, parses through the file and makes every line a vertex that
    # has adjacent vertices that are also vertex objects
    info = []
    openf = open(filename, "r")
    for line in openf:
        info.append(line)
    openf.close()
    
    vertex_dict = {}
    
    for line in info:
        param = line.split(";")
        name = param[0].strip()
        x_y = param[2].split(",")
        vertex_dict[name] = Vertex(name, int(x_y[0].strip()), int(x_y[1].strip()))
    for line in info:
        param = line.split(";")
        name = param[0].strip()
        adjacent = param[1].split(",")
        for item in adjacent:
            vertex_dict[name].adjacent.append(vertex_dict[item.strip()])
    return vertex_dict
    

        
        
        