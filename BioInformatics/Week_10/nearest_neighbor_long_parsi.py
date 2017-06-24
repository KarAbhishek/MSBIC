from copy import deepcopy
from collections import defaultdict


def get_tree(edge_list):
    tree = defaultdict(dict)
    for node, child_node in edge_list:
        tree[node].update({child_node: 0})
    return dict(tree)


def format_output(tree):
    edge_list = []
    for node, child_nodes in tree.items():
        for child_node in child_nodes:
            edge_list.append((node, child_node))
    return edge_list


def tree_nearest_neighbors(edge, tree):
    a, b = edge

    edge_start_tree = {i: 0 for i in tree[a]}
    del edge_start_tree[b]
    w, x = edge_start_tree
    edge_end_tree = {i: 0 for i in tree[b]}
    del edge_end_tree[a]
    y, z = edge_end_tree

    tree_bkp_1 = deepcopy(tree)
    tree_bkp_1[a] = {b:0, y:0, w:0}
    del tree_bkp_1[y][b]
    tree_bkp_1[y].update({a:0})
    tree_bkp_1[b] = {a:0, x:0, z:0}
    del tree_bkp_1[x][a]
    tree_bkp_1[x].update({b:0})

    tree_bkp_2 = deepcopy(tree)
    tree_bkp_2[a] = {b:0, z:0, w:0}
    del tree_bkp_2[z][b]
    tree_bkp_2[z].update({a:0})
    tree_bkp_2[b] = {a:0, x:0, y:0}
    del tree_bkp_2[x][a]
    tree_bkp_2[x].update({b:0})
    return tree_bkp_1, tree_bkp_2


if __name__ == "__main__":
    f = open('4.txt', "r")
    lines = f.read().splitlines()
    splitter = lambda l: list(map(int, l.split('->')))
    v = map(splitter, lines[1:])
    out = tree_nearest_neighbors(tuple(map(int, lines[0].split())), get_tree(v))
    edge1, edge2 = map(format_output, out)
    edge_formatter = lambda x: '->'.join(map(str, x))
    print('\n'.join(map(edge_formatter, edge1)))
    print('')
    print('\n'.join(map(edge_formatter, edge2)))
    f.close()
