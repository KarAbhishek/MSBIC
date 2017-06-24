from collections import defaultdict


def is_leaf(node):
    pass


def parsimoner(leaves, tree):
    if len(leaves) < 1:
        assert False
    for idx in range(len(leaves[0])):
        characters = []
        for leaf in leaves:
            characters.append(leaf[idx])
        small_parsimony(characters, tree)


def small_parsimony(characters, tree):
    tag = defaultdict()
    s = defaultdict(dict)
    for v in tree:
        tag[v] = 1
        if is_leaf(v):
            for k in 'ACGT':
                if characters[v] == k:
                    s[k][v] = 0
                else:
                    s[k][v] = 0
    ripes = {}
    while len(ripes) > 0:
        v = ripes.pop()
        tag[v] = 1
        for k in 'ACGT':
            s[k][v] = min([s[i][get_daughter(v)]+delta[i][k] for i in 'ACGT']) + min([s[i][get_son(v)]+delta[i][k] for i in 'ACGT'])

        ripes |= get_ripes(tree)
    pass


def get_ripes(tree):
    pass


def get_daughter(tree, v):
    return tree[v][0]


def get_son(v):
    return tree[v][1]


def get_tree(lines):
    tree = defaultdict(list)
    for i in lines:
        edge_start, edge_end = list(map(int, i.split('->')))
        tree[edge_start] = edge_end
    return dict(tree)


def format_leaves(input):
    formatted_input = []
    for i in input:
        a, b = i.split('->')
        formatted_input.append([int(a), b])

    return formatted_input


if __name__ == '__main__':
    file = open('small_parsimony_data.txt')
    lines = file.read().splitlines()
    limit = int(lines[0])
    print(format_leaves(lines[1: limit+1]))
    tree = get_tree(lines[limit+1:])
    print(tree)
