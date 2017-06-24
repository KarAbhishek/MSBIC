class IdGen:
    id_var = 0

    @staticmethod
    def get_id():
        temp = IdGen.id_var
        IdGen.id_var += 1
        return temp


def trie_construction(ls_of_strings):
    trie = [{}]
    edges = []

    IdGen.get_id()
    for single_string in ls_of_strings:
        make_tree(single_string, trie, edges)
    return trie, edges


def make_tree(single_string, trie, edges):
    edge_start = 0
    for j in single_string:
        if j in trie[edge_start]:
            edge_end = trie[edge_start].get(j)
        else:
            edge_end = IdGen.get_id()
            trie[edge_start].update({j: edge_end})
            edges.append((edge_start, edge_end, j))
            trie.append({})
        edge_start = edge_end


if __name__ == '__main__':
    file = open('input_1.txt')
    string_lists_out = file.read().splitlines()
    trie, edges = trie_construction(string_lists_out)
    print('\n'.join(map(lambda x: str(x[0]) + '->' + str(x[1]) + ':' + x[2], edges)))