class IdGen:
    def __init__(self, id_local=0):
        self.id = id_local

    def get_id(self):
        temp = self.id
        self.id += 1
        return temp


def trie_construction(single_string, final_ls, prev_node, idx, node_reuse):
    if not single_string:
        return
    if not (idx < len(final_ls) and final_ls[idx][2] == single_string[0]) or not node_reuse:
        new_node = id_gen.get_id()
        final_ls.append([prev_node, new_node, single_string[0]])
        node_reuse = False
    else:
        new_node = final_ls[idx][1]  # Node re-use
    trie_construction(single_string[1:], final_ls, new_node, idx + 1, node_reuse)  # [1:])


def trie_prep(string_lists):
    final_ls = []
    for single_string in string_lists:
        trie_construction(single_string, final_ls, prev_node=0, idx=0, node_reuse=True)
    return final_ls

def TrieConstruction(Patterns):
    from collections import defaultdict
    Trie = defaultdict(list)
    Trie.update({0: [[0, '']]})  # a graph consisting of a single node root
    for Pattern in Patterns:
        currentNode = 0
        for currentSymbol in Pattern:
            temp = None
            if currentNode in Trie:
                temp = [i for i in Trie[currentNode] if i[1] == currentSymbol][0]  # there is an outgoing edge from currentNode with label currentSymbol
                if temp:
                    currentNode = temp[0]  # ending node of this edge
            if not temp:
                newNode = id_gen.get_id()  # add a new node newNode to Trie
                Trie[currentNode].append([newNode, currentSymbol])  # add a new edge from currentNode to newNode with label currentSymbol
                print(currentNode, newNode, currentSymbol)
                currentNode = newNode
    return Trie

if __name__ == '__main__':
    file = open('input_1.txt')
    id_gen = IdGen(1)
    string_lists_out = file.read().splitlines()
    out = TrieConstruction(string_lists_out)
    fmt_out = lambda x:str(x[0])+'->'+str(x[1])+':'+str(x[2])
    print(out)
    #print('\n'.join(list(map(fmt_out, out))))



