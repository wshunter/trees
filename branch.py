import numpy as np
import generators as gen


'''
representation of one of the branches of the tree
for the program's internal logic. it should know its 
length,know its starting position, and have a list of
its children along with its parent branch.


'''

class Branch:
    #name of the parent branch is required.
    def __init__(self,creatorName,childNumber,length, t = 'default'):
        self.len = int(length)
        self.children = []
        self.vertices = np.ndarray((self.len,2))
        self.parentName = creatorName

        #ensure the creator and child numbers are ints
        try:
            self.name = str(creatorName) + '.' + str(childNumber)
        except: print("warning: name passed as an int instead of a string")
        self.type = t
        self.numChildren = 0
        


        self.populateDefault()

    def populateDefault(self):
        for x, y, idx in gen.verticalWeightedMotion(self.vertices.shape[0]):
            self.vertices[idx][0] = x
            self.vertices[idx][1] = y

    def testgetlength(self):
        return self.len


    #tells the tree to create a new branch with the parent's name and a new digit. Both the branch and the tree can create new branches.
    # def growChild(self):
    #     self.numChildren += 1
    #     tree.newBranch(self.name,self.numChildren)

    





