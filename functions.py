from Edge import Edge
# c is a list of edges
def spanningTreeCheck(c, nVertices):
    # check if Spanning Tree
    #   Has all vertices connected
    '''vert = set()
    for e in c:
        vert.add(e.vertex1)
        vert.add(e.vertex2)

    #does not cover all vertices thus not spanning
    if not len(vert) == nVertices:
    return False'''

    #   Is connected (all reachable from first)
    vert = set()
    vert.add(c[0].vertex1)
    vert.add(c[0].vertex2)

    listc = list(c)
    i = 0
    while not len(listc) == 0:
        if vert.__contains__(listc[i].vertex1) or vert.__contains__(listc[i].vertex2):
            vert.add(listc[i].vertex1)
            vert.add(listc[i].vertex2)
            listc.remove(listc[i])
            i = 0
        else:
            if i == len(listc)-1:
                return False
            else:
                i += 1
        if len(vert) == nVertices:
            return True
    return False