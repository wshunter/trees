import generators as gen

class options():
    def __init__(self, type = 'default', form = 'branch', reach = (5,2), color = '#ff0000', size = 0):
        self.type = type #a string that instructs the tree how to do various things, like generate  
                         #the object's vertices or draw it
        self.form = form # 'branch' or 'leaf', determines whether or not the object has a pre-defined list of vertices 
                         #or if its vertices are decided at draw time. stops leaves from growing eachother recursively

        self.reach = reach #a tuple containing two numbers with information on how to generate the object's vertices.
                            #for example for a default branch, contains the mean length and standard deviation, respectively

        self.color = color #hex color
        self.size = size #determines how many children a branch may have. A branch with size 0 may only have leaves
                        # as children branches with size >0 may only have branches with lower size and possibly leaves.

    def getLength(self): #function that returns a random length depending on the reach.
                        #this is lets branches can share the same options object but have different lengths
            return gen.gaussianInts(self.reach[0], self.reach[1], min = 1)

leafstandard = options(form = 'leaf', size = 0)
normal = options(reach = (10,3))
kids = options(reach = (15,6), form = 'branch', type = 'children1')