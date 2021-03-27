import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math
from matplotlib.path import Path
import matplotlib.patches as patches

from wind import windclass

rd.seed(a=None, version =2)
#create an array of points we can use
len = 32
codes = []
tpath = np.zeros((len,2))
for r in range(0,len):
    tpath[r][0] = r*math.cos(r)
    tpath[r][1] = r*math.sin(r)
    codes.append(Path.LINETO)
codes[0] = Path.MOVETO

mypath = Path(tpath, codes)
patch = patches.PathPatch(mypath)
fig, ax = plt.subplots()
ax.add_patch(patch)
ax.set_xlim(-40,40)
ax.set_ylim(-40,40)
plt.show()
