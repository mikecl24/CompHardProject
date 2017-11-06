from Edge import Edge

gloB = 0

def Grow(NV, T, edges, total, total_P, A_param=[]):
    global gloB
    res = gloB+1
    A_res = []
    FF = []
    for e in edges:
        # XOR in T
        if (e.vertex1 in T and e.vertex2 not in T) or (e.vertex2 in T and e.vertex1 not in T):
            FF.append(e)

    F = sorted(FF, key=lambda x: (x.weight_p+x.weight))

    if len(F) > 0:
        for edge in F:
            T_temp = set(T)
            T_temp.add(edge.vertex1)
            T_temp.add(edge.vertex2)
            A_temp = A_param[:]
            A_temp.append(edge)
            edges_temp = edges[:]
            for i in range(F.index(edge)):
                del edges_temp[edges_temp.index(F[i])]
            del edges_temp[edges_temp.index(edge)]
            if total+edge.weight > gloB or total_P+edge.weight_p > gloB:
                continue
            B, A = Grow(NV, T_temp, edges_temp, total+edge.weight, total_P+edge.weight_p, A_temp)
            if B < res and len(A) == NV-1:
                res = B
                A_res = A[:]

                if res < gloB:
                    gloB = B
                    print(res)
                    print(*A_res,sep=' ' )

        return res, A_res
    # is a spanning tree
    else:
        #print(*A_param, sep=' ')
        if total > total_P:
            return total, A_param
        else:
            return total_P, A_param



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

#Add the prime weights and get max B

for e in Edges:
    e.weight_p = Edges[NEdges - 1 - Edges.index(e)].weight
    gloB += e.weight


T = {1}
init = []
B, A = Grow(NVertices, T, Edges, 0, 0)
print('Result')
print(B)
print(*A, sep=' ')
