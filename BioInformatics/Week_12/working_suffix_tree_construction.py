from BioInformatics.Week_12.working_trie import trie_construction


def suffix_tree_const(strin):
    ls = []
    for i in range(len(strin)):
        ls.append(strin[i:])
    trie, edges = trie_construction(ls)
    # print(edges)
    return trie


def construct_suffix_tree(trie, level, ret):
    ls = []
    for single_char in trie[level]:
        edge_end = trie[level][single_char]
        if not trie[edge_end]:
            ret.append(single_char)
            ls.append(''.join(ret))
            ret = []  # Filter only edges
        elif len(trie[edge_end]) > 1:
            ret.append(single_char)
            ls.append(''.join(ret))
            ret = []  # Filter only edges
            ls += construct_suffix_tree(trie, edge_end, ret)
            ret = []  # Reset edge case
        elif len(trie[edge_end]) == 1:
            ret.append(single_char)
            ls += construct_suffix_tree(trie, edge_end, ret)
            ret = []  # Filter only edges
    return ls


def get_suffix_tree(stub):
    trie = list(suffix_tree_const(stub))
    ret = []
    return construct_suffix_tree(trie, 0, ret)

if __name__ == '__main__':
    [print(i) for i in get_suffix_tree('ATAAATG$')]

