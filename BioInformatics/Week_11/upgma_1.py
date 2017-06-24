class IdGenerator:
    def __init__(self, iid=0):
        self.id = iid

    def get_id(self):
        temp = self.id
        self.id += 1
        return temp


def upgma(dist_mat):
    tree = {str(i): {0: str(i)} for i in range(len(dist_mat))}
    while len(dist_mat) > 1:
        mat_min, min_pos = find_matrix_min(dist_mat, tree)
        # # print(mat_min, min_pos)
        # # # print(tree)
        merge_cluster(dist_mat, tree, min_pos)
        # # # print(tree)


def upgma_2(dist_mat):
    tree = {str(i+1): {0: [str(i+1)]} for i in range(len(dist_mat))}
    dist_mat = {str(idx+1): {str(idx_j+1): j for idx_j, j in enumerate(i)} for idx, i in enumerate(dist_mat)}
    while len(dist_mat) > 1:
        mat_min, min_pos = find_matrix_min_2(dist_mat)
        # # print(mat_min, min_pos)
        merge_cluster_2(dist_mat, tree, min_pos)
    return tree


def find_matrix_min(dist_mat, tree):
    min_elem = float('inf')
    for i_idx in range(len(dist_mat)):
        for j_idx in range(i_idx + 1, len(dist_mat)):
            comp_elem = dist_mat[i_idx][j_idx]
            if comp_elem < min_elem:
                min_elem = comp_elem
                min_pos = (str(i_idx), str(j_idx))

    # # # print('Here', [i for i in tree])
    return min_elem, min_pos


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


def merge_cluster(dist_mat, tree, min_pos):
    min_pos_x, min_pos_y = min_pos
    # # print(min_pos, 'tree_key')
    cache = {key: tree[tk] for key in min_pos for tk in tree if key in tk[0]}

    age = dist_mat[int(min_pos_x)][int(min_pos_y)] / 2

    update_matrix(dist_mat, min_pos, tree)
    del tree[min_pos_x]
    del tree[min_pos_y]
    tree['_'.join(min_pos)] = age, cache


def merge_cluster_2(dist_mat, tree, min_pos):
    min_pos_x, min_pos_y = min_pos
    # # print(min_pos, 'tree_key')
    cache = {key: tree[key] for key in min_pos}

    age = dist_mat[min_pos_x][min_pos_y] / 2.0

    iiid_gen = id_gen_out.get_id()
    update_matrix_2(dist_mat, min_pos, tree, iiid_gen)
    age_for_print_x = age - int(list(tree[min_pos_x].keys())[0])
    age_for_print_y = age - int(list(tree[min_pos_y].keys())[0])
    del tree[min_pos_x]
    del tree[min_pos_y]

    # tree[iiid_gen] = {age: cache}
    tree['_'.join(min_pos)] = {age: cache}
    # # print(iiid_gen, id_gen_out.get_id())
    ret.append([iiid_gen, '->', min_pos_x, ':', age_for_print_x])
    ret.append([iiid_gen, '->', min_pos_y, ':', age_for_print_y])
    ret.append([min_pos_x, '->', iiid_gen, ':', age_for_print_x])
    ret.append([min_pos_y, '->', iiid_gen, ':', age_for_print_y])
    print(' '.join(min_pos_x.split('_')), ' '.join(min_pos_y.split('_')))


def update_matrix(dist_mat, min_pos, tree):
    import numpy as np
    # dist_arr = np.array(dist_mat)
    dist_mat.append([])
    # new_dist_row = []
    for i in range(len(dist_mat)):
        if i in min_pos:
            continue

        len_c_i = len(list(tree[min_pos[0]].items())[0][1])
        len_c_j = len(list(tree[min_pos[1]].items())[0][1])
        new_dist_i = (dist_mat[i][int(min_pos[0])] * len_c_i + dist_mat[i][
            int(min_pos[1])] * len_c_j) / (len_c_i + len_c_j)
        dist_mat[i].append(new_dist_i)
        dist_mat[-1].append(new_dist_i)

    del dist_mat[-1][-1]
    dist_mat[-1][-1] = 0
    # = np.array(dist_mat)
    for j in range(len(dist_mat)):
        if str(j) in min_pos:
            del dist_mat[j]
            continue
    for j in range(len(dist_mat)):
        # if str(j) in min_pos:
        #     del dist_mat[j]
        #     continue
        for i in sorted(min_pos, reverse=True):
            del dist_mat[j][int(i)]



            # # print(np.array(dist_mat))


def update_matrix_2(dist_mat, min_pos, tree, new_row_name):
    # import numpy as np
    # dist_arr = np.array(dist_mat)
    # dist_mat.append([])
    # new_dist_row = []
    # # print_dist_mat(dist_mat)
    new_row_name = '_'.join(min_pos)
    dist_keys = list(dist_mat.keys())
    for i in dist_keys:
        if i in min_pos:
            continue

        len_c_i = len(list(tree[min_pos[0]].items())[0][1])  # len(tree[min_pos[0]])  #
        len_c_j = len(list(tree[min_pos[1]].items())[0][1])  # len(tree[min_pos[1]])  #
        new_dist_i = (dist_mat[i][min_pos[0]] * len_c_i + dist_mat[i][
            min_pos[1]] * len_c_j) / (len_c_i + len_c_j)
        mat = dist_mat.get(new_row_name, {})
        mat.update({i: new_dist_i, new_row_name: 0})
        dist_mat[new_row_name] = mat
        mat = dist_mat.get(i, {})
        mat.update({new_row_name: new_dist_i})
        dist_mat[i] = mat
        del dist_mat[i][min_pos[0]]
        del dist_mat[i][min_pos[1]]

    #dist_mat[new_row_name].update({new_row_name: 0})

    del dist_mat[min_pos[0]]
    del dist_mat[min_pos[1]]


    # # print(dist_mat)


# def # print_dist_mat(dist_mat):
#     # print('Dist mat here ')
#
#     for i in sorted(dist_mat.keys()):
#         for j in sorted(dist_mat[i].keys()):
#             # print(dist_mat[i][j], end=' ')
#         # print()


if __name__ == "__main__":

    file = open('upgma_data.txt')
    lines = file.read().splitlines()
    splitter = lambda x: list(map(float, x.split()))
    ret = []
    id_gen_out = IdGenerator(int(lines[0]))
    dist_mat_out = list(map(splitter, lines[1:]))
    out = upgma_2(dist_mat_out)
    # print(out)
    joiner = lambda x: ''.join(map(str, x))
    outer = sorted(map(joiner, ret))

    # print('\n'.join(outer))
