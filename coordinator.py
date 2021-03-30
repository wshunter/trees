from branch import Branch
import matplotlib.pyplot as plt

class coordinator():
    def __init__(self):
        self.tracker = {}
        fig, ax = plt.subplots()

    def newBranch(self,callerName,childNumber,length=1,t = 'default'):
        self.tracker[callerName + '.' + childNumber] = Branch(callerName,childNumber,length,t)

    def draw(self):
        for b in self.tracker:
            print(b.name)