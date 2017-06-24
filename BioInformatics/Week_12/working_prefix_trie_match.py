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


def trie_matching(text, trie):
    index_ls = []
    for idx, v in enumerate(text):
        prefix_trie_matching(text, trie, idx, v, index_ls)

    return index_ls


def prefix_trie_matching(text, trie, idx, v, index_ls):
    bkp_idx = idx
    start = 0
    while v in trie[start]:
        start = trie[start].get(v)
        if not trie[start]:  # Is a leaf
            index_ls.append(idx)
            break
        bkp_idx += 1
        if bkp_idx < len(text):
            v = text[bkp_idx]
        else:  # Ran out of things to compare in Text
            break


if __name__ == '__main__':
    fi = open('match.txt')

    lines = fi.read().splitlines()
    genome = lines[0]
    dna = lines[1:]

    trie, edges = trie_construction(dna)
    print('\n'.join(map(lambda x: str(x[0]) + '->' + str(x[1]) + ':' + x[2], edges)))
    indices = trie_matching(genome, trie)
    print(' '.join([str(x) for x in indices]))