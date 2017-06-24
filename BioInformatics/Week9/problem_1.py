from copy import deepcopy

def create_adjacency_list(lines):
    hm = {}
    for line in lines:
        outgoing_edge, incomin_n_weight = (line.split('->'))
        outgoing_edge = int(outgoing_edge)
        val = tuple(map(int, incomin_n_weight.split(':')))
        try:
            hm[outgoing_edge][val[0]] = val[1]
        except:
            hm[outgoing_edge] = {val[0]: val[1]}
    return hm


def find_leaves(adjacency_list):
    leaves = []
    for key in adjacency_list:
        if len(adjacency_list[key]) == 1:
            leaves.append(key)
    return leaves


def traversal_on_steroids(adj_list, leaves):
    dist_i = []
    for leaf_idx_i, leaf_i in enumerate(leaves):
        dist_j = []
        for leaf_idx_j, leaf_j in enumerate(leaves):
            dist_j.append(traversal(deepcopy(adj_list), start=leaf_i, destination=leaf_j, weight=0))
        dist_i.append(dist_j)

    return dist_i


def traversal(adj_list, start, destination, weight):
    if start == destination:
        return weight

    if not adj_list or start not in adj_list:
        return float('inf')#assert False # 'Did not find path'

    bkp_adj = adj_list
    dist = []
    for end in adj_list[start]:
        curr_weight = adj_list[start][end]
        adj_list = deepcopy(bkp_adj)
        # weight += curr_weight
        remove(edge=(start, end), from_list=adj_list)
        dist.append(traversal(adj_list, end, destination, curr_weight + weight))
    return min(dist)


def remove(edge, from_list):
    start = edge[0]
    end = edge[1]
    if not from_list[start]:
        del from_list[start]
    del from_list[end][start]
    if not from_list[end]:
        del from_list[end]

if __name__ == '__main__':
    file = open('problem_1_data.txt')
    lines = file.read().splitlines()
    adjacency_list = create_adjacency_list(lines[1:])
    leaves = find_leaves(adjacency_list)
    if len(leaves) != int(lines[0]):
        assert 'Smells Fishy'
    distance_matrix = [[0 for y in leaves] for y in leaves]
    joiner = lambda x: ' '.join(map(str, x))
    print('\n'.join(map(joiner, traversal_on_steroids(adjacency_list, leaves))))

