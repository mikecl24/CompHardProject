def Grow2(edges, nv):
    graph = dict()
    for i in range(1,nv+1):
        graph[i]=[]

    for e in edges:
        graph[e.vertex1].append(e)
        graph[e.vertex2].append(e)

    #MST
    T = set()
    A = []
    flag = True
    while flag:
        #Add obligatory edges
        flag = False
        for v in graph:
            if len(graph[v])==1:
                A.append(graph[v][0])
                T.add(graph[v][0].vertex1)
                T.add(graph[v][0].vertex2)
                graph[graph[v][0].vertex1] = []
                graph[graph[v][0].vertex2] = []
                #del graph[graph[v][0].vertex1][graph[graph[v][0].vertex1].index(graph[v][0])]
                #del graph[graph[v][0].vertex2][graph[graph[v][0].vertex2].index(graph[v][0])]
                flag = True
    #print(T)
    for i in range(1, len(graph)+1):
        print(str(i) + ': ')
        print(*graph[i], sep=' ')
        if len(graph[i]) == 0:
            continue
        #else:
            #branch
