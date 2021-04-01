from branch import Branch
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import generators as gen

LEAFVERTS = 7

class coordinator():
    def __init__(self):
        self.tracker = {}
        self.fig, self.ax = plt.subplots()

    def newBranch(self,callerName,childNumber,length=1,type = 'default', start = (0,0,0), form = 'branch'):
        name = str(callerName) + '.' + str(childNumber)
        self.tracker[name] = Branch(callerName,childNumber,length,type,start, form = form)

        children = 0



        #special modes for the branch type
        if type == 'children1':
            numChildren = gen.gaussianInts(0,2,min = 0)
            if numChildren == 0:
                return
            for idx in range(numChildren): #need to add functionality to start the branches somewhere other than the origin
                maxLength = self.tracker[name].length
                if maxLength > 1:
                    startPosIdx = gen.randomIntRange(1,maxLength)
                    startPos = (self.tracker[name].vertices[startPosIdx, 0], self.tracker[name].vertices[startPosIdx, 1], self.tracker[name].vertices[startPosIdx, 2])
                    self.newBranch(name, idx, length = gen.gaussianInts(length/2,2), type = 'children1', start = startPos)
                    children += 1
        
        #draw leaf at the end of branch
        #TODO: write function to get the tuple position of a certain element along the branch
        if type != 'leaf':
            self.newBranch(name, children, length = 0, form = 'leaf', start = (self.tracker[name].vertices[length, 0], self.tracker[name].vertices[length, 1], self.tracker[name].vertices[length, 2]))


    def draw(self):
        paths = []
        for b in self.tracker:
            if self.tracker[b].form == 'branch':
                verts = self.tracker[b].vertices[:,0:2]
                path = Path(verts)
                patch = patches.PathPatch(path, fill = False, edgecolor = 'black')
                self.ax.add_patch(patch)
            #leaves' shape isn't really important, so it is only calculated when the leaf is drawn
            elif self.tracker[b].form == 'leaf':
                verts = []
                codes = []
                for vert, code in gen.leafConstruct(LEAFVERTS, self.tracker[b].start):
                    verts.append(vert)
                    codes.append(code)
                path = Path(verts, codes)
                patch = patches.PathPatch(path, fill = True, facecolor= 'orange')
                self.ax.add_patch(patch)



        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(0,20)
        plt.show()