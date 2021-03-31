import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math
import matplotlib.path as path
import matplotlib.patches as patches

from wind import windclass
from branch import *
from coordinator import *

def main():
    rd.seed()
    tree = coordinator()
    tree.newBranch("1","1",length=8)
    tree.newBranch("1","2",length=6)
    for idx in range(200):
        tree.newBranch("1", str(idx), length = gen.gaussianBranchLengths(10, 3))
    tree.draw()

if __name__ == "__main__":
    main()
    


