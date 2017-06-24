def trie_construction(patterns):
    # edges = []
    from collections import OrderedDict
    edge_dict = OrderedDict()
    for pattern in patterns:
        origin_point = 0
        for char in pattern:
            if (origin_point, len(edge_dict) + 1) not in edge_dict:
                # edges.append(origin_point, new_point, pattern)
                edge_dict[origin_point, len(edge_dict) + 1] = char
                origin_point = len(edge_dict)
    return edge_dict


def trie_construction_reboot(patterns):
    edges = [[]]
    for pattern in patterns:
        for char_idx, char in enumerate(pattern):
            if not is_char_in_edges(char_idx, char, edges):
                edges[-1].append(len(edges)+1)


def trie_construction_part_2(patterns):
    # edges = [[]]
    edges = []
    for pattern in patterns:

        for edge_idx in range(len(pattern)+1):

            new_idx = len(edges) + 1
            edges.append(new_idx)


def is_char_in_edges(char_idx, char, edges):
    for previous_edge in edges:
        if previous_edge[char_idx] == char:
            return True
    return False

class IdGen:
    id_var = 0
    @staticmethod
    def get_id():
        temp = IdGen.id_var
        IdGen.id_var += 1
        return temp

def trie_construction_new(patterns):

    check_point = {}
    edges = []
    for pattern in patterns:
        extend_edge = False
        for char_idx, char in enumerate(pattern):
            if extend_edge:
                # extend edge
                lagging_edge = IdGen.get_id()  # len(edges) + 1
                edges.append([leading_edge, lagging_edge, char])
                leading_edge = lagging_edge
                check_point[char_idx] = char
                pass
            elif is_new_pattern(check_point, char, char_idx):
                # create new edge
                leading_edge = IdGen.get_id()  # len(edges) + 1
                lagging_edge = IdGen.get_id()  # len(edges) + 2

                check_point[char_idx] = char
                edges.append([leading_edge, lagging_edge, char])
                extend_edge = True
                leading_edge = lagging_edge
                pass
            else:
                # Leave it

                pass
    return edges


def is_new_pattern(check_point, char, char_idx):
    return not (char_idx in check_point and char in check_point[char_idx])



if __name__ == '__main__':
    file = open('input.txt')
    patterns_out = file.read().splitlines()
    out = trie_construction_new(patterns_out)
    print(out)