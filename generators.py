import random as rd
import numpy as np
import math

def randomTheta(): #returns an angle between -pi and pi
    return (rd.random()-0.5)*2*math.pi
def randomVel(): #returns a velocity between -1 and 1
    return (rd.random() - 0.5)*2

def verticalWeightedMotion(length):
    velR = 1
    velT = math.pi/2
    posX = 0
    posY = 0
    yield 0, 0, 0
    for i in range(length-1):
        velR += randomVel() / 10
        velT += randomTheta()/8

        posX += velR*math.cos(velT)
        posY += velR*math.sin(velT)

        yield posX, posY, i + 1
        

def gaussianInts(mean, standardDeviation, min = 1):
    val = np.random.normal(mean, standardDeviation) + 0.5
    val = int(val)
    if min == False:
        return val
    if min == True:
        min = 1
    if val < min:
        val = min
    return val


def test():
    for i in range(20):
        print(gaussianInts(0,2, min = False))
if __name__ == "__main__":
    test()

