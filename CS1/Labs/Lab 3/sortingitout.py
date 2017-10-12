from city import City
from quicksort import *

in_file = open("world_cities.txt", "r") # opens the file world_cities.txt for reading.

cities = []

for line in in_file:                    # makes every line in the file a City object by taking out the commas and putting the parts of the line in the city constructor.
    param = line.splice().split(",")
    cities.append(City(param[0], param[1], param[2], int(param[3]), float(param[4]), float(param[5])))
in_file.close()                         # closes the file

def write(cities, filename):
    '''because when I tried to do these separately, it would take too long to process, this is a function that writes the every line of each file.'''
    outfile = open(filename, "w")
    i = 0
    while i < len(cities):
        outfile.write(str(cities[i]) + "\n")
        i += 1
    outfile.close()

# sorts each city and writes them back to the new files.
sort(cities, compare_name)
write(cities, "cities_alpha.txt")
sort(cities, compare_population)
write(cities, "cities_population.txt")
sort(cities, compare_latitude)
write(cities, "cities_latitude.txt")