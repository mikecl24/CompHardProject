def check_Set(v1, v2, sets):
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


    if t1 == t2:
        return False, 0, 0
    else:
        return True, t1, t2

def Union(set1, set2, sets):
    for i in sets[set2]:
        sets[set1].append(i)
    del sets[set2]
    return sets