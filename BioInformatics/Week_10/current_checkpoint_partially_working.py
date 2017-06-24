from collections import defaultdict
from copy import deepcopy

def traverse_tree(leaves, tree, true_leaves):
    repeat = len(leaves)
    # print(leaves, tree)

    top_node = topo_sort(tree)
    ret = ['' for idx in range(repeat)]
    for idx in range(repeat):
        tree_copy = deepcopy(tree)
        tree_copy.update(leaves[idx])
        adder_list = []
        traverse(top_node, tree_copy, adder_list, true_leaves, idx)
        backtrack_parsed(ret, idx, adder_list, true_leaves)
    return ret


def backtrack_parsed(ret, idx, parsed_tree, true_leaves):
    print(parsed_tree)
    for i_idx, i in enumerate(parsed_tree):
        # true_leaves[][idx][i_idx]
        ret[idx] += (find_min_elem(i)[0])


def topo_sort(tree):
    # node = list(tree.keys())
    return [node for node in tree for other_nodes in tree if node not in tree[other_nodes]][0]
    # return [lead_node for lead_node in tree if node not in tree[lead_node]][0]


def find_min_elem(parent_score_map):
    # if type(parent_score_map) == list:
    #     parent_score_map = parent_score_map[1]
    min_key = min(parent_score_map, key=parent_score_map.get)
    return min_key, parent_score_map[min_key]


def traverse(node, tree, adder_list, true_leaves, idx):
    # if node in leaves:
    #     score = {'A': float('inf'), 'C': float('inf'), 'G': float('inf'), 'T': float('inf')}
    #     curr_nucleot = leaves[node].pop()
    #     score[curr_nucleot] = 0
    #     return deepcopy(score)

    if type(node) == str:
        score = {'A': float('inf'), 'C': float('inf'), 'G': float('inf'), 'T': float('inf')}
        score[node] = 0
        true_selection = node
        # print('Leaf is ', node)
        non_sense = 122
        return (non_sense, deepcopy(score))

    score_min_list = []
    for n_idx, child_node in enumerate(tree[node]):
        # if type(child_node) == str:

            # print('True node', true_leaves[node][n_idx], child_node)
        parent_score_map = traverse(child_node, tree, adder_list, true_leaves, idx)
        # if type(child_node) == str:
        #     parent_score_map = [node, parent_score_map]
        min_nucleo, min_elem = find_min_elem(parent_score_map)
        score_min_list.append((min_nucleo, min_elem))

    curr_score_map = defaultdict(int)

    for selected_nucleotide in 'ACGT':
        # curr_nuc_scores = []
        for min_nucleo, min_elem in score_min_list:
            if selected_nucleotide != min_nucleo:
                curr_score_map[selected_nucleotide] += min_elem + 1
            else:
                curr_score_map[selected_nucleotide] += min_elem


    curr_score_map = dict(curr_score_map)
    true_selection = find_min_elem(curr_score_map)
    # print('true_selection', true_selection)
    # print('True node', true_leaves[node][n_idx], child_node)
    adder_list.append(curr_score_map)
    # curr_score_map[selected_nucleotide] = min(curr_nuc_scores)

    #     score_map_list.append(curr_score_map)
    # curr_score_map_stub = defaultdict()
    # for nucleotide in 'ACGT':
    #     curr_score_map_stub[nucleotide] = sum([score_map[nucleotide] for score_map in score_map_list])
    if type(child_node) == str:
        xx = node
    else:
        xx =
    return [xx, curr_score_map]  # min(curr_score_map_stub.values()), curr_score_map_stub


def get_tree(unformatted_tree):
    tree = defaultdict(list)
    for i in unformatted_tree:
        edge_start, edge_end = list(map(int, i.split('->')))
        tree[edge_start].append(edge_end)
    return dict(tree)


def get_true_leaves(input):
    hm = defaultdict(list)
    for inp in input:
        a, b = inp.split('->')
        hm[int(a)].append(b)
    # print(dict(hm))
    return (dict(hm))



def format_leaves(input):
    _, b = input[0].split('->')

    repeat = len(b)

    formatted_input = [defaultdict(list) for _ in range(repeat)]
    for idx in range(repeat):
        for i in input:
            a, b = i.split('->')
            formatted_input[idx][int(a)].append(b[idx])

    return list(map(dict, formatted_input))


if __name__ == '__main__':
    file = open('small_parsimony_data.txt')
    lines = file.read().splitlines()
    limit = int(lines[0])
    leaves_out = (format_leaves(lines[1: limit+1]))
    true_leaves = get_true_leaves(lines[1: limit + 1])
    tree_out = get_tree(lines[limit + 1:])
    print(tree_out)
    print(traverse_tree(leaves_out, tree_out, true_leaves))
