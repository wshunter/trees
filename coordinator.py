from branch import Branch
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

class coordinator():
    def __init__(self):
        self.tracker = {}
        self.fig, self.ax = plt.subplots()

    def newBranch(self,callerName,childNumber,length=1,t = 'default'):
        self.tracker[callerName + '.' + childNumber] = Branch(callerName,childNumber,length,t)

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