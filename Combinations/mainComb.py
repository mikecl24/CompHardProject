from itertools import combinations

from functionsC import spanningTreeCheck

from NonGreedy.Edge import Edge

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

# worst case max B
B=0
for e in Edges:
    B += e.weight

#generate combinations
comb = combinations(Edges, NVertices-1)

for c in comb:
    # check that the sum of weights is not over previous found best
    sum = 0
    for e in c:
        sum += e.weight
    if sum > B:
        continue

    # check that the sum of weights of the mirror is not over previous found best
    sump = 0
    for e in c:
        sump += Edges[NEdges - 1 - Edges.index(e)].weight
    if sump > B:
        continue

    #Check if its a spanning tree
    if not spanningTreeCheck(c, NVertices):
        continue

    copy = c
    if sum < sump:
        B = sump
        print(B)
        continue
    else:
        B = sum
        print(B)
        continue

print("Smallest B: " + str(B))
print(*copy, sep=' ')
