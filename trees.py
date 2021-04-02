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
    for idx in range(1):
        startPos = (10*idx, 0, 0)
        tree.newBranch("1", str(idx), cfg.kids, start = startPos)

    for b in tree.tracker:
        print(tree.tracker[b].name, " ", tree.tracker[b].options.form)

    tree.draw()

if __name__ == "__main__":
    main()
    



# %%
