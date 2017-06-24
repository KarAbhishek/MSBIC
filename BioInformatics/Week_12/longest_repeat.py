
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



def binary_search(ls, elem):
    # Its all sorted
    return binary_search_helper(ls, 0, len(ls) - 1, elem)

def binary_search_helper(ls, start, end, elem):
    mid = (start+end) // 2
    if elem == ls[mid]:
        return mid
    elif elem < ls[mid]:
        return binary_search_helper(ls, start, mid, elem)
    else:
        return binary_search_helper(ls, mid+1, end, elem)

# Longest Repeat
def iterative_binary_search(ls, elem):
    start = 0
    end = len(ls)-1
    idxs = -1
    while start == mid or end == mid:
        mid = (start + end) // 2
        kmers = {ls[i: i + mid] for i in range(len(ls) - mid + 1)}
        trie, edges = trie_construction(kmers)
        indices = trie_matching(ls, trie)
        if elem == ls[mid]:
            idxs = mid
            break
        elif elem < ls[mid]:
            end = mid
            mid += (mid - start) // 2
        elif len(indices) > len(kmers):
            start = mid
            mid += (end - mid) // 2

    return idxs


if __name__ == '__main__':
    out = iterative_binary_search('ACAAGCCTAAATATTAAACTTCGGGTTTAAGGATGTTGTTGGTCACTACGACTCATATGGGGCGAAATAGAACCGGACATTATAGCTACGGCCCTTGTCATAGGTGGCCTCGTCATCGGGTATGAAGCGTGGTTACGACCGTCCTCTATAGGGCTGTGAAAGATAAGCACTACTTCTGATGTGATGTATAAGTTTCCGCTGTGAAAAATTAATCACATTGACCCCTGGACCTGTCAACGCTGTCTGAATTATCATAGACGGAAACGTAGCGTTCTGTAAAAGTACCTGATGCGGGGGCGCAAGTCGTGACTGCCCCCTAGAACACGTTCTTCCGAAGGCATTAATTGGAATGAGATGAAACTCGCTAGGATTTGCGCCATACTACCTTCGATATGTTCCAAATCATTCGCCGGTAATCACGCAGAAAATTCCATAGCAGTTTTGTATGAAGAGGGATAGTGGGAAGGTGGTGCTCGATTGCTGTGTCCGCCTAGCACGCAGTGCTTTTGCGTCATCTTTCTACTCTATACCAAAAGGGTCTGTGCGCCGCGGACTAAAATCCGGCCTAGATCCAATCATCAACGTTGCACCGGAATCCCCTTTAGTTGGCACTTAGCCCCGCGCGTAAGATGACTCTACAGAACAGGTGGAGTCGGCCCTTCTGTAAAAGTACCTGATGCGGGGGCGCAAGTCGTGACTGCCCCCTAGAAGAGCAAGCACGCCGGGAACGCGACGTCGCAGACATAAAACATACGCGGTTTCTGGAATCGCGCGCCCCCCAAGAGCGCTGATATTATGGAAGCATCAGCTGAGAGGTTTTTTTATGATAGCCTATATCGTGCGACAACCGGACAAAGCTTACATTGAGTATCAGTACTTACTCGGGTCTCCGATCAGGCTTCTGTAAAAGTACCTGATGCGGGGGCGCAAGTCGTGACTGCCCCCTAGAAGTACCGTAATTTTTTAAAGTAAACTACACTTCAGCTCCATTGTGCGTGGAGCCTTTTTCCGCAAACCAATTTGTACATTAGGGTTCTTAGTGCGGCCCTCGAAGATGGCTACTCCTTGACTCCTAGGTCGAAGACAGCATTGAGACAAGGCTAGCAGATGTTATTTCTCATTCCGGCCCCTGAGCAATGATTCACACAATGCC')
    print(out)
    # print iterative_binary_search([1,2,3], 1)
