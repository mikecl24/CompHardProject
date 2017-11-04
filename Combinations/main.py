from itertools import combinations
from Edge import Edge

from Combinations.functions import spanningTreeCheck

f = open("test02.uwg", "r")
NVertices = int(f.readline())
NEdges = int(f.readline())

Edges = []
for i in range(NEdges):
    edge = f.readline().split(" ")
    Edges.append(Edge(int(edge[0]), int(edge[1]), int(edge[2])))

#Add the prime weights
for e in Edges:
    e.weight_p = Edges[NEdges - 1 - Edges.index(e)].weight

B=0
for e in Edges:
    B += e.weight
#print("Maximum B: " + str(B) )

#generate combinations
comb = combinations(Edges, NVertices-1)

for c in comb:
    #print(*c, sep=' ')
    # calculate sum Edges
    sum = 0
    for e in c:
        sum += e.weight
        # print(sum)
    if sum > B:
        continue

    # check sum in Edges'
    sump = 0
    for e in c:
        sump += Edges[NEdges - 1 - Edges.index(e)].weight
        # print(sump)
    if sump > B:
        continue

    #Check if its a spanning tree
    if not spanningTreeCheck(c, NVertices):
        #print("Not a spanning Tree")
        continue

    copy = c
    if sum < sump:
        B = sump
        continue
    else:
        B = sum
        continue

print(*copy, sep=' ')
print("Smallest B: " + str(B))

