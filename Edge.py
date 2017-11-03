class Edge:
    def __init__(self, v1, v2, w):
        self.weight = w
        self.vertex1 = v1
        self.vertex2 = v2
    def __str__(self):
        return '<'+str(self.vertex1)+' '+str(self.vertex2)+' '+str(self.weight)+'>'

    def __gt__(self, edge2):
        return self.weight > edge2.weight
