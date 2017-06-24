def upgma(D, n):
    clusters = {i: {} for i in range(1,n+1)}
    T = {i: [] for i in range(1,n+1)}
    age =[0 for v in T]
    while len(clusters) > 1:
        C_i, C_j = find_closest_clusters()
        C_new = merge(C_i, C_j)
        T['C_new'] = C_new
        age['C_new'] = D[C_i][C_j]//2
        remove(D, C_i); remove(D, C_j)
        del clusters[C_i]; del clusters[C_j]
        D = add_row_column(clusters, C_new, D)
        clusters['C_new'] = C_new


def add_row_column(clusters, C_new, D):
    import numpy as np
    dist_row = []
    for c in clusters:
        dist_row.append(distance(C_new, c))
    D.append(dist_row[:-1])
    D = np.concatenate((D, dist_row), 1)
file = open('upgma_data.txt')

def distance(D, C_i, C_j, c):
    return (D[C_i][c]*len(C_i)+D[C_j][c]*len(C_j)) // (len(C_i)+len(C_j))

upgma(D,n)

def remove(D, n):
    import numpy as np
    D = np.delete(D, (n), axis=0)
    D = np.delete(D, (n), axis=1)
    return D.tolist()