import random as rd


def verticalWeightedMotion(length):
    velX = 0
    velY = 1
    velX += (rd.random() - 0.5)/3
    velY += (rd.random() - 0.5)/3
    yield velX, velY
    for i in range(length-1):
        velX += (rd.random() - 0.5)/3
        velY += (rd.random() - 0.5)/3
        yield velX, velY


