class IdGen:
    id_var = 0

    @staticmethod
    def get_id():
        temp = IdGen.id_var
        IdGen.id_var += 1
        return temp

def make_prefix_tree(ls_of_strings):
    len_of_ls = max([len(single_string) for single_string in ls_of_strings])
    ls = [[] for _ in range(len_of_ls)]
    IdGen.get_id()
    ls2 = []
    for single_string in ls_of_strings:
        make_tree(single_string, ls, ls2)
    from operator import itemgetter
    return sorted(ls2, key=itemgetter(0))


def make_tree(strin, tree, ls):
    edge_start = 0
    reuse = True
    for char_idx, char in enumerate(strin):
        # Change the edge_end w.r.t whether u have seen the end before

        temp = [i[1] for i in tree[edge_start] if i[2] == char] if edge_start < len(tree) else None
        temp = temp[0] if temp else None

        if temp and reuse:
            edge_end = temp
        else:
            edge_end = IdGen.get_id()
            tree[char_idx].append((edge_start, edge_end, char))
            ls.append([edge_start, edge_end, char])
            reuse = False
        edge_start = edge_end


if __name__ == '__main__':
    file = open('input_1.txt')
    string_lists_out = file.read().splitlines()
    out = make_prefix_tree(string_lists_out)
    fmt_out = lambda x: str(x[0]) + '->' + str(x[1]) + ':' + str(x[2])
    print('\n'.join(list(map(fmt_out, out))))