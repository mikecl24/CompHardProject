from random import randint
from Node import Node
from Edge import Edge
from functions import spanningTreeCheck
from itertools import combinations

f = open("test03.uwg", "r")
NVertices = int(f.readline())
NEdges = int(f.readline())

Edges = []
for i in range(NEdges):
    edge = f.readline().split(" ")
    Edges.append(Edge(int(edge[0]), int(edge[1]), int(edge[2])))
'''
NVertices = 3
NEdges = 3
Edges = []

Edges.append(Edge(1, 2, 1))
Edges.append(Edge(2, 3, 2))
Edges.append(Edge(1, 3, 3))
'''

#Verify integrity of list of Edges
#print(*Edges, sep=' ')

#Highest B
B=0
for e in Edges:
    B += e.weight
#print("Maximum B: " + str(B) )

#generate combinations
comb = combinations(Edges, NVertices-1)

min = B
for c in comb:

    # calculate sum Edges
    sum = 0
    for e in c:
        sum += e.weight
        # print(sum)
    if sum>B:
        continue

    # check sum in Edges'
    sump = 0
    for e in c:
        sump += Edges[NEdges - 1 - Edges.index(e)].weight
        # print(sump)
    if sump>B:
        continue

    #Check if its a spanning tree
    if not spanningTreeCheck(c, NVertices):
        #print("Not a spanning Tree")
        continue

    copy = c
    if sum < sump:
        B = sump
    else:
        B = sum

print(*copy, sep=' ')
print("Smallest B: " + str(B))


'''
#random implementation

#pick NVertices-1
NumPicked = []
while len(NumPicked) != (NVertices-1):
    e = randint(0, NEdges-1)
    if e not in NumPicked:
        NumPicked.append(e)
NumPicked = sorted(NumPicked)
print(NumPicked)

#check if B in Edges
sum = 0
for i in NumPicked:
    sum += Edges[i].weight
    if sum<B:
        
#check if B in Edges'


#check if Spanning Tree
#   Has all vertices connected
for i in NumPicked:
    print(Edges[i])
#   Is connected (all reachable from 1)
'''
