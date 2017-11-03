class Node:
    def __init__(self, TnotE, EnotT, parent):
        self.TnotE = TnotE[:]
        self.EnotT = EnotT[:]
        self.parent = parent
        self.child = []

    def addChild(self,node):
        assert isinstance(node, Node)
        self.child.append(node)
