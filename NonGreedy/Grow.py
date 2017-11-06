
def Grow(T, edges, total, total_P, A_param=[]):
    res = 1000000000000
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
            if total+edge.weight > 2673 or total_P+edge.weight_p > 2673:
                continue
            B, A = Grow(T_temp, edges_temp, total+edge.weight, total_P+edge.weight_p, A_temp)
            if B < res and len(A) == 99:
                res = B
                A_res = A[:]

                if res < 2673:
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

