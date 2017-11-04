from Edge import Edge
from NonGreedy.Grow import Grow
from NonGreedy.Grow2 import Grow2

debug = False
f = open("test03.uwg", "r")
NVertices = int(f.readline())
NEdges = int(f.readline())

Edges = []
for i in range(NEdges):
    edge = f.readline().split(" ")
    Edges.append(Edge(int(edge[0]), int(edge[1]), int(edge[2])))

#Add the prime weights
for e in Edges:
    e.weight_p = Edges[NEdges - 1 - Edges.index(e)].weight


'''
T = {1}
init = []
B, A = Grow(T, Edges, 0, 0)
print(B)
print(*A, sep=' ')
'''
Grow2(Edges, NVertices)