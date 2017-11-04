def Grow(T, edges, total, total_P, A_param=[]):
    res = 1000000000000
    A_res = []
    F = []
    for e in edges:
        # XOR in T
        if (e.vertex1 in T and e.vertex2 not in T) or (e.vertex2 in T and e.vertex1 not in T):
            F.append(e)

    if len(F)>0:
        for edge in F:
            T_temp = set(T)
            T_temp.add(edge.vertex1)
            T_temp.add(edge.vertex2)
            A_temp = A_param[:]
            A_temp.append(edge)
            edges_temp = edges[:]
            del edges_temp[edges_temp.index(edge)]
            B, A = Grow(T_temp, edges_temp, total+edge.weight, total_P+edge.weight_p, A_temp)
            if B<res:
                res = B
                A_res = A[:]
        return res, A_res
    # is a spanning tree
    else:
        print(*A_param, sep=' ')
        if total > total_P:
            return total, A_param
        else:
            return total_P, A_param

