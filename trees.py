import matplotlib.pyplot as plt
import numpy as np
import random as rd
from matplotlib.path import Path
import matplotlib.patches as patches

from wind import windclass

rd.seed(a=None, version =2)
#create an array of points we can use
WINDRANGE = 0.1
len = 32
num = 8
x = np.zeros((num,2,len),dtype=float)
gust = windclass(0)
for j in range(0,num):
    for i in range(0,len):
        x[j][0][i] = i
        x[j][1][i] += gust.step(i)
    gust.setVel(0)

heights = x[0,0,:]
lengths = x[0,1,:]
print(heights)
print(lengths)
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(0,num):
    ax.plot(x[i][1][:],x[i][0][:], 'go--')
plt.show()
