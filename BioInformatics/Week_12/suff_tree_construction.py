def suffix_tree_const(strin):
    ls = []
    for i in range(len(strin)):
        ls.append(strin[i:])
    maybe_suffix_tree(ls)


def maybe_suffix_tree(ls_strings):
    tree = []
    for strin in ls_strings:
        make_tree(strin, tree)


def make_tree(strin, tree):
    edge_start = 0
    new_id = 1
    for char_idx, char in enumerate(strin):
        # Change the edge_end w.r.t whether u have seen the end before

        if char_idx in tree:
            temp = [i[1] for i in tree[char_idx] if i[2] == char][0]

        if temp:
            edge_end = temp
        else:
            edge_end = new_id
            tree[char_idx].append((edge_start, edge_end, char))
        print(edge_start, '->', edge_end, ':', char)
        edge_start = edge_end

if __name__ == '__main__':
    string_out = 'ATAAATG$'
    suffix_tree_const(string_out)
