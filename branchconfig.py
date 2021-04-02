import generators as gen
import copy
TOTAL = 0
PER_NODE = 1

def default_child_fn(option): #a default child generator function that returns a new options class one size smaller
    new_option = copy.copy(option)
    if new_option.size > 0:
        new_option.size -= 1
        new_option.reach = (new_option.reach[0]-1, new_option.reach[1])
        new_option.popFunction = gen.perpendicularRandomMotion
        return new_option

    else:
        result = copy.copy(leafstandard)
        result.color = '#8db54e'
        return result


class options():
    def __init__(self, type = 'default', form = 'branch', reach = (7,3), color = '#ff0000', size = 2, segLength = (0.1, 0.125),
    proclivity = (3, 2, TOTAL), leafRate = (2, 0), childfunction = default_child_fn, endWithLeaf = False, popFunction = gen.verticalRandomMotion):
        self.type = type #a string that instructs the tree how to do various things, like generate  
                         #the object's vertices or draw it

        self.form = form # 'branch' or 'leaf', determines whether or not the object has a pre-defined list of vertices 
                         #or if its vertices are decided at draw time. stops leaves from growing eachother recursively

        self.reach = reach #a tuple containing two numbers with information on how to generate the object's vertices.
                            #for example for a default branch, contains the mean length and standard deviation, respectively

        self.color = color #hex color

        self.size = size #determines how many children a branch may have. A branch with size 0 may only have leaves
                        # as children branches with size >0 may only have branches with lower size and possibly leaves.

        self.segLength = segLength #tuple containing information for the branch generator

        self.proclivity = proclivity #tuple containg mean and std. dev number of children. TOTAL flag for if this denotes the
                        #total number of children a branch can have, PER_NODE if this refers to the number of children per node

        self.leafRate = leafRate #contains info about how often leaves are to be generated
        
        self.getChildSettings = childfunction #function that takes in an option object and returns a new one.
                #this object's children will have the new options. Should result in an object with no children
                #under some conditions which will always be obtained eventually to prevent infinite recursive child growing.

        self.popFunction = popFunction
                #generator function used to populate a branch's vertices. Should
                #take branch length, start struct, segLength struct
                # and yield (in order: x, y, theta, index of vertex)



    def getLength(self): #function that returns a random length depending on the reach.
                        #this is lets branches can share the same options object but have different lengths
            return gen.gaussianInts(self.reach[0], self.reach[1], min = 1)


leafstandard = options(form = 'leaf', size = 0, color = '#31782f')
normal = options(reach = (10,3))
justone = options(reach = (2,0),
        size=0,
        segLength = (1,0))
fall = options(reach = (5,1), 
        form = 'branch', 
        type = 'default', 
        segLength = (0.1, 0.03), 
        proclivity = (1, 2, PER_NODE), 
        size = 3,
        color = '#8db54e')
