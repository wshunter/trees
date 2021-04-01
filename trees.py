#%%
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math
import matplotlib.path as path
import matplotlib.patches as patches

from wind import windclass
from branch import *
from coordinator import *
# %%
def main():
    rd.seed()
    tree = coordinator()
    for idx in range(1):
        tree.newBranch("1", str(idx), length = gen.gaussianInts(10, 3), type = 'children1')
    tree.draw()
    print(tree.tracker)

if __name__ == "__main__":
    main()
    



# %%
