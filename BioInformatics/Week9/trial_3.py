from BioInformatics.Week9.limb_length import limb_len
import random
from copy import deepcopy


def create_bald(dist_mat, ll, target):
    dist_mat_copy = deepcopy(dist_mat)
    for i in dist_mat_copy:
        for j in dist_mat_copy:
            if i!=j and (i==target or j ==target):
                dist_mat_copy[i][j] -= ll
    return dist_mat_copy


def create_trim(dist_mat, j):
    dist_mat_copy = deepcopy(dist_mat)
    del dist_mat_copy[j]
    for i in dist_mat_copy:
        del dist_mat_copy[i][j]
    return dist_mat_copy


def additive_phylogeny(dist_mat):
    dist_mat = {idx: {idx_j: j for idx_j, j in enumerate(i)} for idx, i in enumerate(dist_mat)}
    T = recurse(dist_mat)

    return T


def perfect_leaves(dist_mat, n):
    for i in dist_mat:
        for k in dist_mat:
            if dist_mat[i][k] == dist_mat[i][n] + dist_mat[n][k]:
                return i, k
    return None, None


def add_new_node(T, v, n, ll):
    pass


def recurse(dist_mat):
    # Base Case when there is one node create the tree with those elements
    if len(dist_mat) == 2:
        edge_lead, edge_end = list(dist_mat.keys())
        print(edge_lead, '->', edge_end, ':', dist_mat[edge_lead][edge_end])
        return  {edge_lead: {edge_end: dist_mat[edge_lead][edge_end]}}# {edge_lead: edge_end}
    # select the last element instead of taking random elements everytime
    n = len(dist_mat) - 1
    # get the limb_len for the selected element
    limb_l = limb_len(n, dist_mat)
    # create d_bald
    dist_mat_bald = create_bald(dist_mat, limb_l, n)

    # checkpoint
    print(dist_mat)

    # find leaves which are suitable for making a tree out of the dist_matrix by breaking the single node in parts
    i, k = perfect_leaves(dist_mat_bald, n)

    # Find the distance of prospective node from i after peeking at bald matrix
    x = dist_mat_bald[i][n]


    dist_mat_trimmed = create_trim(dist_mat_bald, n)
    T = recurse(dist_mat_trimmed)

    # add a new node with weight limb length after traversing through i and k and finding a spot exactly x dist away
    traversal(T, i, k, 0, False, x)
    # add_new_node(T, (i, k), n, weight=limb_l)
    return T


def traversal(adj_list, start, destination, weight, FoundAt, x):
    if start == destination:
        return weight

    print('I am X', x)
    if weight == x:
        FoundAt = True
        print('Yes sir')
    if not adj_list or start not in adj_list:
        return float('inf')

    bkp_adj = adj_list
    dist = []
    for end in adj_list[start]:
        curr_weight = adj_list[start][end]
        adj_list = deepcopy(bkp_adj)
        remove(edge=(start, end), from_list=adj_list)
        dist.append(traversal(adj_list, end, destination, curr_weight + weight, FoundAt, x))
    return min(dist)


def remove(edge, from_list):
    start = edge[0]
    end = edge[1]
    del from_list[start][end]
    if not from_list[start]:
        del from_list[start]
    # del from_list[end][start]
    # if not from_list[end]:
    #     del from_list[end]

if __name__ == "__main__":

    file = open('additive_data.txt')
    lines = file.read().splitlines()
    splitter = lambda x: list(map(int, x.split()))
    ret = []
    dist_mat_out = list(map(splitter, lines[1:]))
    out = additive_phylogeny(dist_mat_out)
    print(out)
    # joiner = lambda x: ''.join(map(str, x))
    # outer = sorted(map(joiner, ret))
    #
    # print('\n'.join(outer))