from BioInformatics.Week9.limb_length import limb_len
def additive_phylogeny(D, n):
    if n == 2:
        pass
        # return tree
    limb_length = limb_len(D, n)
    for j in range(1,n):
        D[n][j] = D[j][n] = D[j][n] -limb_length
    i,k = perfect_leaves(D, n)
    x = D[i][n]
    remove(D, n)
    T = additive_phylogeny(D, n-1)
    v = new_node(dist=x, origin=i, path=[i,k])
    add_leaf(n, T, v, limb_length)
    return T


def perfect_leaves(dist_mat, n):
    for i in range(len(dist_mat)):
        for k in range(len(dist_mat)):
            if dist_mat[i][n]+dist_mat[n][k] == dist_mat[i][k]:
                return i, k
    return None, None

def remove(D, n):
    import numpy as np
    D = np.delete(D, (n), axis=0)
    D = np.delete(D, (n), axis=1)
    return D.tolist()