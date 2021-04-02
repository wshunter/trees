#%%
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math
import matplotlib.path as path
import matplotlib.patches as patches

import branchconfig as cfg
from branch import *
from coordinator import *

# %%
def main():
    rd.seed()
    tree = coordinator()
    startPos = (0, 0, math.pi/2)
    tree.newBranch('1', '0', cfg.options(), start = startPos)

    #for b in tree.tracker:
    #    print(tree.tracker[b].name, " ", tree.tracker[b].options.form)

    tree.draw()

if __name__ == "__main__":
    main()
    



# %%
print(math.sin(math.pi/2))


# %%
