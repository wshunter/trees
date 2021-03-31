from branch import Branch
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import generators as gen

class coordinator():
    def __init__(self):
        self.tracker = {}
        self.fig, self.ax = plt.subplots()

    def newBranch(self,callerName,childNumber,length=1,t = 'default'):
        name = str(callerName) + '.' + str(childNumber)
        self.tracker[name] = Branch(callerName,childNumber,length,t)
        if t == 'children1':
            numChildren = gen.gaussianInts(0,2,min = 0)
            if numChildren == 0:
                return
            for idx in range(numChildren): #need to add functionality to start the branches somewhere other than the origin
                self.newBranch(name, idx, length = gen.gaussianInts(4,2))


    def draw(self):
        paths = []
        for b in self.tracker:
            verts = self.tracker[b].vertices
            path = Path(verts)
            patch = patches.PathPatch(path, fill = False, edgecolor = 'black')
            self.ax.add_patch(patch)

        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(0,20)
        plt.show()