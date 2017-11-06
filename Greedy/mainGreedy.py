from functionsG import check_Set, Union
from Edge import Edge

nr = input("Which test? (1-4): ")
try:
    int(nr)
except ValueError:
    print("Wrong dataset number (NaN)")
    exit()

if int(nr) not in range(1,5):
    print("Wrong dataset number (not 1-4)")
    exit()

# import from file selected
if int(nr) == 1:
    f = open("test01.uwg", "r")
elif int(nr) == 2:
    f = open("test02.uwg", "r")
elif int(nr) == 3:
    f = open("test03.uwg", "r")
else:
    f = open("test04.uwg", "r")
NVertices = int(f.readline())
NEdges = int(f.readline())

Edges = []
for i in range(NEdges):
    edge = f.readline().split(" ")
    Edges.append(Edge(int(edge[0]), int(edge[1]), int(edge[2])))

# Add the prime weights
for e in Edges:
    e.weight_p = Edges[NEdges - 1 - Edges.index(e)].weight

# Make-Set(v) for all vertices
Sets = []
Sets_h = []
for i in range(1, NVertices+1):
    Sets.append([i])
    Sets_h.append([i])

# Order edges by weight
# by first weight, then mirror weight
Edges_W = sorted(Edges, key=lambda x: (x.weight, x.weight_p))
# by first mirror weight, then weight
Edges_WM = sorted(Edges, key=lambda x: (x.weight_p, x.weight))
# by sum of weight and mirror weight
Edges_S = sorted(Edges, key=lambda x: (x.weight_p + x.weight))

#Do it for smallest increase of biggest sum
A = []
B = 0
B_prime = 0
while len(A) < NVertices-1:

    #smallest increase
    if B>B_prime:
        e = Edges_W[0]
    else:
        e = Edges_WM[0]

    #verify if the vertices are already part of the same set
    status, t1, t2 = check_Set(e.vertex1, e.vertex2, Sets)
    if status:
        A.append(e)  # A = A U {(u,v)}
        B += e.weight
        B_prime += e.weight_p

        Sets = Union(t1, t2, Sets)
        #remove edge from worklists
        del Edges_W[Edges_W.index(e)]
        del Edges_WM[Edges_WM.index(e)]

    #should be removed because already in same tree
    else:
        # remove edge from worklists
        del Edges_W[Edges_W.index(e)]
        del Edges_WM[Edges_WM.index(e)]

# Do it for the least increase in both
A_h = []
B_h = 0
B_prime_h = 0
while len(A_h) < NVertices-1:
    #smallest total increase (heuristic):
    e2 = Edges_S[0]

    # verify if the vertices are already in the same set for the heuristic case
    status_h, t1_h, t2_h = check_Set(e2.vertex1, e2.vertex2, Sets_h)
    if status_h:
        A_h.append(e2)
        B_h += e2.weight
        B_prime_h += e2.weight_p
        Sets_h = Union(t1_h, t2_h, Sets_h)
        del Edges_S[Edges_S.index(e2)]
    else:

        del Edges_S[Edges_S.index(e2)]


Res = 0
Res_h = 0
#max(...)
if B > B_prime:
    Res = B
else:
    Res = B_prime
#max(...)
if B_h > B_prime_h:
    Res_h = B_h
else:
    Res_h = B_prime_h
#return minimum solution
if Res < Res_h:
    print("Smallest B: " + str(Res))
    A = sorted(A, key=lambda x: (x.vertex1, x.vertex2))
    print(*A, sep=' ')
else:

    print("Smallest B: " + str(Res_h))
    A_h = sorted(A_h, key=lambda x: (x.vertex1, x.vertex2))
    print(*A_h, sep=' ')