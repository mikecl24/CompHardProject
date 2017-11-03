class Edge:
    def __init__(self, v1, v2, w):
        self.weight = w
        self.weight_p = 0
        self.vertex1 = v1
        self.vertex2 = v2
    def __str__(self):
        return '<'+str(self.vertex1)+' '+str(self.vertex2)+' '+str(self.weight)+' '+str(self.weight_p)+'>'

    def __eq__(self, edge2):
        return self.weight == edge2.weight and self.vertex1 == edge2.vertex1 and self.vertex2 == edge2.vertex2

    def __gt__(self, edge2):
        w_edge1 = 0
        w_edge2 = 0
        if self.weight>self.weight_p:
            w_edge1 = self.weight
        else:
            w_edge1 = self.weight_p
        if edge2.weight>edge2.weight_p:
            w_edge2 = edge2.weight
        else:
            w_edge2 = edge2.weight_p
        return w_edge1 > w_edge2
