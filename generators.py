import random as rd
import numpy as np

def verticalWeightedMotion(length):
    velX = 0
    velY = 1
    posX = 0
    posY = 0
    velX += (rd.random() - 0.5)/3
    velY += (rd.random() - 0.5)/3
    yield 0, 0, 0
    for i in range(length-1):
        velX += (rd.random() - 0.5)/3
        velY += (rd.random() - 0.5)/3
        posX += velX
        posY += velY
        yield posX, posY, i + 1

def gaussianBranchLengths(mean, standardDeviation):
    val = np.random.normal(mean, standardDeviation)
    val = int(val)
    if val < 1:
        val = 1
    return val


