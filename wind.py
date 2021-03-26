import random as rd

class windclass:
    vel = 0.0
    upper = 0.0
    lower = 0.0
    def __init__(self, init=0.0, *bounds):
        self.vel = init
        if(len(bounds) == 0):
            self.upper = 0.1
            self.lower = -0.1
        if(len(bounds) == 1):
            self.upper = bounds[0]
            self.lower = -1*bounds[0]
        if(len(bounds) == 2):
            self.lower = bounds[0]
            self.upper = bounds[1]
        assert(len(bounds) <= 2)


    def setVel(self, v):
        self.vel = v
    #Called every step up the tree to change the wind velocity a little.
    #returns new velocity so we can move the tree
    def step(self, height):
        u = self.upper*height
        l = self.lower*height
        self.vel += (rd.random()*(u-l))+l
        return self.vel

    