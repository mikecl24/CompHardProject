from Edge import Edge

def check_Set(v1, v2, sets, debug):
    #Find vertex 1
    i = 0
    t1 = 0
    for tree in sets:
        if v1 in tree:
            t1 = i
            break
        i += 1

    #Find vertex 2
    i=0
    t2=0
    for tree in sets:
        if v2 in tree:
            t2 = i
            break
        i += 1

    if debug:
        print(sets[t1])
        print(sets[t2])

    if t1 == t2:
        return False, 0, 0
    else:
        return True, t1, t2

debug = False
f = open("test02.uwg", "r")
NVertices = int(f.readline())
NEdges = int(f.readline())

Edges = []
for i in range(NEdges):
    edge = f.readline().split(" ")
    Edges.append(Edge(int(edge[0]), int(edge[1]), int(edge[2])))

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
Edges.sort() #Possible thanks to __gt__ definition in edge
if debug:
    print('Ordered Edges:')
    print(*Edges, sep=' ')

#Edge iteration
for e in Edges:
    if debug:
        print('Current Edge: ')
        print(e)

    #verify if the vertices are already part of the same set
    status, t1, t2 = check_Set(e.vertex1, e.vertex2, Sets, debug)
    if status:
        print('Where not in same set')
    else:
        print('Where in same set')
        print('ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')