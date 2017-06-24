from copy import deepcopy


def limb_len(j, dist_mat):
    min_arr = []
    for i in range(len(dist_mat)):
        for k in range(len(dist_mat)):
            val = (dist_mat[i][j]+dist_mat[j][k]-dist_mat[i][k])//2
            if val > 0:
                min_arr.append(val)

    return min(min_arr)


def remove(edge, from_list):
    start = edge[0]
    end = edge[1]
    if not from_list[start]:
        del from_list[start]
    del from_list[end][start]
    if not from_list[end]:
        del from_list[end]


def traverse(adj_list, start, destination, weight=0, path=[]):
    # print(adj_list)
    if start == destination:
        return path+[(start, weight)]
        # return weight
    if not adj_list or start not in adj_list:
        return  # float('inf')#assert False # 'Did not find path'
    bkp_adj = adj_list
    # dist = []
    for end in adj_list[start]:
        curr_weight = adj_list[start][end]
        adj_list = deepcopy(bkp_adj)
        remove(edge=(start, end), from_list=adj_list)
        reto = traverse(adj_list, end, destination, curr_weight + weight, path + [(start, weight)])
        if reto is not None:
            return reto  # min(dist)


def add_leaf(T, leaf, edge_start, edge_end, x, weight, stable_n):
    my_T = {i: {j: k for j, k in T[i]} for i in T}
    path = traverse(my_T, edge_start, edge_end)
    break_point = None
    for idx in range(1, len(path)):
        curr_edge_start, start_weight = path[idx - 1]
        curr_edge_end, end_weight = path[idx]
        if start_weight == x:
            break_point = curr_edge_start
            # Already Done
        elif start_weight < x < end_weight:
            del my_T[curr_edge_start][curr_edge_end]
            del my_T[curr_edge_end][curr_edge_start]
            break_point = max(list(T.keys()) + [stable_n]) + 1  # Change this
            # create edge start_edge -> break_point ->
            w1 = x - start_weight
            w2 = end_weight - x
            my_T.update({break_point: {curr_edge_start: w1, curr_edge_end: w2}})
            my_T.setdefault(curr_edge_start, {}).update({break_point: w1})
            my_T.setdefault(curr_edge_end, {}).update({break_point: w2})
        pass
    T = {i: [(j, my_T[i][j]) for j in my_T[i]] for i in my_T}
    T.setdefault(leaf, []).append((break_point, weight))
    T[break_point].append((leaf, weight))
    return T


def perfect_leaves(dist_mat, n):
    for i in range(len(dist_mat)):
        for k in range(len(dist_mat)):
            if dist_mat[i][k] == dist_mat[i][n] + dist_mat[n][k]:
                return i, k
    return None, None


def neighbor_joining_matrix(dist_mat):
    total_dist = get_total_distances(dist_mat)
    dist_mat_star = deepcopy(dist_mat)
    for i in dist_mat:
        for j in dist_mat:
            if i == j:
                dist_mat_star[i][j] = 0
            else:
                dist_mat_star[i][j] -= total_dist[i]
    return dist_mat_star


def get_total_distances(dist_mat):
    total_distance = {}
    for i in dist_mat:
        total_distance[i] = min(list(dist_mat[i].values()))
    return total_distance


def find_matrix_min_2(dist_mat):
    min_elem = float('inf')
    for i in dist_mat:
        for j in dist_mat:
            if i == j: continue
            comp_elem = dist_mat[i][j]
            if comp_elem < min_elem:
                min_elem = comp_elem
                min_pos = (i, j)

    return min_elem, min_pos


def recurse(nn, stable_n, dist_mat):
    if nn == 2:
        return {0: [(1, dist_mat[0][1]), ], 1: [(0, dist_mat[1][0]), ]}

    dist_mat_star = neighbor_joining_matrix(dist_mat)

    find_matrix_min_2(dist_mat_star)

    # limb_l = limb_len(nn - 1, dist_mat_star)
    # dist_mat_star_bald = create_bald(dist_mat_star, limb_l, nn-1)
    # (i, k) = perfect_leaves(dist_mat_star_bald, nn - 1)
    # x = dist_mat_star_bald[i][nn - 1]
    # dist_mat_star_trim = create_trim(dist_mat_star, nn-1)
    # T = recurse(nn - 1, stable_n, dist_mat_star_trim)
    # T = add_leaf(T, nn - 1, i, k, x, limb_l, stable_n)
    return T


def create_bald(dist_mat, ll, target):
    dist_mat_copy = deepcopy(dist_mat)
    for i in dist_mat_copy:
        for j in dist_mat_copy:
            if i != j and (i == target or j == target):
                dist_mat_copy[i][j] -= ll
    return dist_mat_copy


def create_trim(dist_mat, j):
    dist_mat_copy = deepcopy(dist_mat)
    del dist_mat_copy[j]
    for i in dist_mat_copy:
        del dist_mat_copy[i][j]
    return dist_mat_copy


def additive_phylogeny(n, dist_mat):
    dist_mat = {idx: {idx_j: j for idx_j, j in enumerate(i)} for idx, i in enumerate(dist_mat)}
    T = recurse(n, n - 1, dist_mat)
    return T


if __name__ == '__main__':
    file_ob = open('neighbor_joining.txt')
    lines = file_ob.read().splitlines()
    splitter = lambda x: list(map(int, x.split()))
    d = (list(map(splitter, lines[1:])))
    T = additive_phylogeny(int(lines[0]), d)
    # print T

    for u in T:
        for v, w in T[u]:
            print(str(u)+'->'+str(v)+':'+str(w))

    file_ob.close()