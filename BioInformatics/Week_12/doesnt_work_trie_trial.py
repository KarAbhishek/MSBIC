class IdGen:
    def __init__(self, id_local=0):
        self.id = id_local

    def get_id(self):
        temp = self.id
        self.id += 1
        return temp


def trie_construction(string_lists):
    # for single_string in string_lists:
    curr_tree = []
    # idx = id_gen.get_id()

    create_tree(curr_tree, node_idx, string_lists[0])  # , idx)
    print(curr_tree)

#
# def create_tree(tree, single_string, curr_index):
#     while len(single_string) >= 2:
#         curr_string = single_string[0]
#         # tree[]
#         if curr_string in tree[]:
#             pass
#             # reuse
#         else:
#             edge_end_idx = id_gen.get_id()
#         tree.append((curr_string, (curr_index + '->' + single_string[1])))
#         single_string = single_string[1:]


def create_tree(tree, node_idx, single_string):
    while len(single_string) >= 2:
        curr_char = single_string[0]
        if curr_char in tree[node_idx]:  # Every tree contains ordered numbered nodes which has node index as an element
            # reuse node
            pass
        else:
            # create node
            tree[]
            # formalities with capturing the node
            pass

        node_idx += 1
        single_string = single_string[1:]

if __name__ == '__main__':
    file = open('input_1.txt')
    id_gen = IdGen(1)
    string_lists_out = file.read().splitlines()
    # print(string_lists_out[0])
    out = trie_construction(string_lists_out)
    fmt_out = lambda x:str(x[0])+'->'+str(x[1])+':'+str(x[2])
    print(out)