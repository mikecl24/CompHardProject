from Edge import Edge
from Greedy.functionsG import check_Set, Union

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
    #print(e.weight_p)

#Make-Set(v) for all vertices
Sets = []
for i in range(1, NVertices+1):
    Sets.append([i])
if debug:
    print('Vertices:')
    print(*Sets, sep=' ')

#Order edges by weight
if debug:
    print('Unsorted Edges: ')
    print(*Edges, sep=' ')

Edges_O = sorted(Edges, key=lambda x: (x.weight, x.weight_p))
Edges_OP = sorted(Edges, key=lambda x: (x.weight_p, x.weight))

if debug:
    print('Ordered Edges by weight:')
    print(*Edges_O, sep=' ')
    print('Ordered Edges by weight of the prime:')
    print(*Edges_OP, sep=' ')

A = []
B=0
B_prime = 0
while len(A)<NVertices-1:
    if debug:
        print('Current Edge: ')
        print(e)

    #smallest increase
    #if B + Edges_O[0].weight > B_prime + Edges_OP[0].weight_p:
    if B>B_prime:
        e=Edges_O[0]
    else:
        e=Edges_OP[0]

    #verify if the vertices are already part of the same set
    status, t1, t2 = check_Set(e.vertex1, e.vertex2, Sets, debug)
    if status:
        if debug:
            print('Edges where not in same set')
        A.append(e)  # A = A U {(u,v)}
        B += e.weight
        B_prime += e.weight_p

        Sets = Union(t1, t2, Sets)
        #remove edge from worklists
        del Edges_O[Edges_O.index(e)]
        del Edges_OP[Edges_OP.index(e)]
    else:
        if debug:
            print('Edges are in the same tree')

        # remove edge from worklists
        del Edges_O[Edges_O.index(e)]
        del Edges_OP[Edges_OP.index(e)]

if B>B_prime:
    print(B)
    print(B_prime)
else:
    print(B_prime)
    print(B)

A = sorted(A, key=lambda x: (x.vertex1, x.vertex2))
print(*A, sep=' ')