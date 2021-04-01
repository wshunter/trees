import numpy as np
import generators as gen
import branchconfig as cfg

'''
representation of one of the branches of the tree
for the program's internal logic. it should know its 
length,know its starting position, and have a list of
its children along with its parent branch.


'''

class Branch:
    #name of the parent branch is required.
    def __init__(self, creatorName, childNumber, options, length, start):
        self.form = options.form
        self.type = options.type
        self.length = length #do NOT call options.getlength() directly, it was pre-decided on by the tree.
        self.vertices = np.ndarray((self.length,3))
        self.parentName = creatorName
        self.start = start
        #ensure the creator and child numbers are ints
        try:
            self.name = str(creatorName) + '.' + str(childNumber)
        except: print("warning: name passed as an int instead of a string")
        
        if self.form == 'branch':
            self.populateDefault(self.type)

    def populateDefault(self, type):
        for x, y, t, idx in gen.angularWeightedMotion(self.vertices.shape[0], self.start):
            self.vertices[idx][0] = x
            self.vertices[idx][1] = y
            self.vertices[idx][2] = t

    def testgetlength(self):
        return self.length

    def getPos(self, index):
        try: #returns the position of a vertex on the branch by its index
            return (self.vertices[index, 0], self.vertices[index, 1], self.vertices[index, 2])
        except Exception:
            print("warning! tried to get an indexed position of a branch with no vertices!")
            return self.start


    #tells the tree to create a new branch with the parent's name and a new digit. Both the branch and the tree can create new branches.
    # def growChild(self):
    #     self.numChildren += 1
    #     tree.newBranch(self.name,self.numChildren)

    





