import random as rd
import numpy as np
import math
from matplotlib.path import Path


def randomTheta(): #returns an angle between -pi and pi
    return (rd.random()-0.5)*2*math.pi
def randomVel(): #returns a velocity between -1 and 1
    return (rd.random() - 0.5)*2
def randomIntRange(lowerBound, upperBound):
    val = rd.random()*(upperBound-lowerBound)
    val = int(val)
    val += lowerBound
    return val
def gaussianRightAngle(angle):
    ofs = np.random.normal(0, math.pi/8)
    if rd.random() > 0.5:
        return angle + math.pi / 2 + ofs
    else: 
        return angle - math.pi / 2 + ofs


#generates a list of coordinates. each coordinate moves forward by some distance, which varies by -segLength[0] to segLength[0]
#in a direction varying by -segLength[1] radians to segLength[1] radians
def angularWeightedMotion(length, start, segLength):
    velR = 1
    velT = math.pi/2
    posX = start[0]
    posY = start[1]
    theta = start[2] 
    yield posX, posY, theta, 0
    for i in range(length-1):
        velR += randomVel() * segLength[0]
        velT += randomTheta() * segLength[1]

        posX += velR*math.cos(velT)
        posY += velR*math.sin(velT)
        theta += velT

        yield posX, posY, theta, i + 1

def leafConstruct(num, start):
    vel = 0.3
    yield start[0:2], Path.MOVETO
    theta = start[2]
    pX = start[0]
    pY = start[1]
    for idx in range(num - 2):
        theta += math.pi / 9
        pX += vel*math.cos(theta)
        pY += vel*math.sin(theta)
        yield (pX, pY), Path.LINETO
    theta += 3*math.pi/6
    for idx in range(num-3):
        theta += math.pi / 9
        pX += vel*math.cos(theta)
        pY += vel*math.sin(theta)
        yield (pX, pY), Path.LINETO
    yield (0,0), Path.CLOSEPOLY



        

def gaussianInts(mean, standardDeviation, min = 1):
    val = np.random.normal(mean, standardDeviation) + 0.5
    val = int(val)
    if val < min:
        val = min
    return val


def test():
    testarray = np.ndarray((10))
    for i in range(200):
        print(randomIntRange(1,0))
    print(testarray)

if __name__ == "__main__":
    test()

