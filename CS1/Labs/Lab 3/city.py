class City:
    def __init__(self, c_code, name, region, population, latitude, longitude):
        self.c_code = c_code
        self.name = name
        self.region = region
        self.pop = population
        self.lat = latitude
        self.long = longitude
    
    def __str__(self):
        return str(self.name) + "," + str(self.pop) + "," + str(self.lat) + "," + str(self.long)