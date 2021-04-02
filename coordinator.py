from branch import Branch
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import generators as gen
import branchconfig as cfg
import math

LEAFVERTS = 7

class coordinator():
    def __init__(self):
        self.tracker = {}
        self.fig, self.ax = plt.subplots()

    def newBranch(self,callerName,childNumber,options,start = (0,0,math.pi / 2)):
        if options.form == 'none':
            return
        name = str(callerName) + '.' + str(childNumber)
        length = options.getLength() #length needs to be pre-calculated so that the tree and the branch agree on the length
        #so it is passed separately to the branch constructor
        self.tracker[name] = Branch(callerName, childNumber, options, length, start)

        children = 0


        #special modes for the branch type
        '''
        if options.type == 'children1':
            numChildren = gen.gaussianInts(0,2,min = 0)
            if numChildren == 0:
                #if it is decided this branch should have no sub children, create a leaf and exit the function
                self.newBranch(name, children, cfg.leafstandard, start = self.tracker[name].getPos(length-1))
                return
            for idx in range(numChildren): #need to add functionality to start the branches somewhere other than the origin
                maxLength = self.tracker[name].length
                if maxLength > 1:
                    startPosIdx = gen.randomIntRange(1,maxLength)
                    startPos = self.tracker[name].getPos(startPosIdx)
                    self.newBranch(name, idx, options = cfg.normal, start = startPos)
                    children += 1
        '''
        #generate sub branches according to the getchildsettings function
        if options.form == 'branch':
            if options.proclivity[2] == cfg.PER_NODE:
                for node in range(length-1): #don't generate kids at node 0
                    numchildren = gen.gaussianInts(options.proclivity[0], options.proclivity[1])
                    childrenOptions = options.getChildSettings(options)
                    for num in range(numchildren):
                        newname = str(name) + '.' + str(children)
                        self.newBranch(name, children, childrenOptions, self.tracker[name].getPos(node+1))
                        children += 1
            if options.proclivity[2] == cfg.TOTAL:
                numchildren = gen.gaussianInts(options.proclivity[0], options.proclivity[1])
                for child in range(numchildren):
                    idx = gen.randomIntRange(1, length - 1)
                    childrenOptions = options.getChildSettings(options)
                    self.newBranch(name, children, childrenOptions, self.tracker[name].getPos(idx))
                    children += 1

        
        #draw leaf at the end of branch
        #TODO: write function to get the tuple position of a certain element along the branch
        '''if options.form != 'leaf':
            lastPos = length - 1
            newCoords = self.tracker[name].getPos(lastPos)
            self.newBranch(name, children, options = cfg.leafstandard, start = newCoords)
        '''
        

    def draw(self):
        paths = []
        for b in self.tracker:
            if self.tracker[b].options.form == 'branch':
                verts = self.tracker[b].vertices[:,0:2]
                path = Path(verts)
                patch = patches.PathPatch(path, fill = False, edgecolor = 'black')
                self.ax.add_patch(patch)
            #leaves' shape isn't really important, so it is only calculated when the leaf is drawn
            elif self.tracker[b].options.form == 'leaf':
                verts = []
                codes = []
                for vert, code in gen.leafConstruct(LEAFVERTS, self.tracker[b].start):
                    verts.append(vert)
                    codes.append(code)
                path = Path(verts, codes)
                patch = patches.PathPatch(path, fill = True, facecolor= self.tracker[b].options.color)
                self.ax.add_patch(patch)

        
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-2, 18)
        plt.show()
    
    