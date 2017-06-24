from collections import defaultdict


class IdGenerator:
    def __init__(self, iid=0):
        self.id = iid

    def get_id(self):
        temp = self.id
        self.id += 1
        return temp


def neighbor_joining(dist_mat, n):
    if n == 2:
        keysez = list(dist_mat.keys())
        tmp = [dict(dist_mat[i]) for i in keysez][0]
        stub = [tmp[i] for i in tmp if tmp[i] != 0][0]
        return [[keysez[0], keysez[1], stub], [keysez[1], keysez[0], stub]]
    dist_mat_star, total_distance = neighbor_joining_matrix(dist_mat, n)
    _, (i, j) = find_matrix_min_2(dist_mat_star)
    delta = (total_distance[i] - total_distance[j]) // (n - 2)
    limb_length_i = 0.5 * (dist_mat[i][j] + delta)
    limb_length_j = 0.5 * (dist_mat[i][j] - delta)
    m = add_row(dist_mat, i, j)
    delete_rows_and_cols(dist_mat, i, j)
    # print(dist_mat)
    T = neighbor_joining(dist_mat, n - 1)
    T += ([m, i, limb_length_i], [m, j, limb_length_j], [i, m, limb_length_i], [j, m, limb_length_j])
    return T


# def np_dist_manipulation():
#     np.array([0,13])

def delete_rows_and_cols(dist_mat, i, j):
    del dist_mat[i]
    del dist_mat[j]
    for m in dist_mat:
        del dist_mat[m][i]
        del dist_mat[m][j]


def add_row(dist_mat, i, j):
    from copy import deepcopy

    new_dist_mat = deepcopy(dist_mat)
    # print(new_dist_mat)
    l = []
    iid = id_gen_out.get_id()

    dist_mat_keys = list(dist_mat.keys())

    for key in dist_mat_keys:
        dist_mat[iid][key] = 0.5 * (dist_mat[key][i] + dist_mat[key][j] - dist_mat[i][j])
        dist_mat[key][iid] = 0.5 * (dist_mat[key][i] + dist_mat[key][j] - dist_mat[i][j])
    dist_mat[iid][iid] = 0
    # print('Chalu', dist_mat)
    return iid

    # for m in dist_mat:
    #     dist_mat[m].update({iid: })
    #         print(dist_mat[n], end=' ')
    # pass


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


def neighbor_joining_matrix(dist_mat, n):
    total_distance = {}
    for i in dist_mat:
        total_distance[i] = (sum([dist_mat[i][j] for j in dist_mat[i]]))
    # print(total_distance)

    dist_mat_star = defaultdict(dict)
    for i in dist_mat:
        for j in dist_mat:
            if i == j:
                dist_mat_star[i][j] = 0
            else:
                dist_mat_star[i][j] = (n - 2) * dist_mat[i][j] - total_distance[i] - total_distance[j]
    return dict(dist_mat_star), total_distance


def format_out(out):
    for i in out:
        print(str(i[0]) + '->' + str(i[1]) + ':' + str(i[2]))


if __name__ == '__main__':
    file = open('neighbor_join_data')
    lines = file.read().splitlines()
    n = int(lines[0])
    dist_mat_out = defaultdict(defaultdict)
    id_gen_out = IdGenerator(n)
    for line_idx, line in enumerate(lines[1:]):
        values = line.split()
        dist_mat_out.update({line_idx: {idx: int(value) for idx, value in enumerate(values)}})
    out = (neighbor_joining(dist_mat_out, n))

    format_out(out)
