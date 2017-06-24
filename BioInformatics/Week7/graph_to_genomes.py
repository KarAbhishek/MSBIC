from functools import reduce
from math import ceil
from BioInformatics.Week7.cycle_to_chromosome import cycle_to_chromosome


def init_select(tuple_collection, with_elem):
    for idx, i in enumerate(tuple_collection):
        if with_elem in i:
            return idx, i


def select(genome_graph):
    return


def graph_to_genome(genome_graph, visited_collection):
    cycle_list = []

    # def unioner(x, y):
    #     return x.union(y)

    # sol_tuple_set = reduce(unioner, map(set, genome_graph))
    # idx, i = init_select(genome_graph, min(sol_tuple_set))

    l = [(singl[0], singl) for singl in genome_graph]
    sorter = lambda x: x[0]
    l = sorted(l, key = sorter)
    #cycle_list.append([])
    while l:
        i = l[0][1]
        if ceil(i[0] / 2) not in visited_collection and ceil(i[1] / 2) not in visited_collection: #New Cycle
            visited_collection.append(ceil(i[0] / 2))
            visited_collection.append(ceil(i[1] / 2))
            cycle_list.append([])
        #else:



        cycle_list[-1].append(i[0])
        cycle_list[-1].append(i[1])
        #genome_graph = genome_graph[:idx]+genome_graph[idx+1:]
        del l[0]
        #idx, i = select(genome_graph, min(sol_tuple_set))
    ret = []

    def rotate(x):
        min_el = min(x)#[0] - x[1]
        axis = [axis for axis, i in enumerate(x) if i == min_el][0]
        # if x[0] == x[axis]+1:
        #     axis = -1
        # if axis%2 == 0:
        #     axis = axis-1

        return x[axis:] + x[:axis]

    for i in cycle_list:
        ret += cycle_to_chromosome(rotate(i))
    return ret


strin = '(1, 4), (3, 6), (5, 7), (8, 9), (10, 11), (12, 14), (13, 15), (16, 18), (17, 19), (20, 22), (21, 24), (23, 26), (25, 27), (28, 29), (30, 32), (31, 33), (34, 36), (35, 38), (37, 39), (40, 42), (41, 44), (43, 2), (45, 48), (47, 50), (49, 51), (52, 54), (53, 56), (55, 57), (58, 60), (59, 62), (61, 63), (64, 66), (65, 68), (67, 69), (70, 72), (71, 74), (73, 76), (75, 78), (77, 79), (80, 81), (82, 84), (83, 86), (85, 87), (88, 90), (89, 91), (92, 94), (93, 46), (96, 98), (97, 99), (100, 102), (101, 103), (104, 106), (105, 107), (108, 109), (110, 111), (112, 114), (113, 115), (116, 117), (118, 119), (120, 122), (121, 123), (124, 125), (126, 127), (128, 130), (129, 131), (132, 134), (133, 135), (136, 138), (137, 139), (140, 141), (142, 144), (143, 145), (146, 147), (148, 149), (150, 152), (151, 95), (154, 155), (156, 158), (157, 159), (160, 161), (162, 163), (164, 166), (165, 168), (167, 169), (170, 171), (172, 174), (173, 175), (176, 178), (177, 180), (179, 182), (181, 184), (183, 186), (185, 187), (188, 190), (189, 191), (192, 194), (193, 196), (195, 153), (198, 200), (199, 201), (202, 204), (203, 205), (206, 207), (208, 210), (209, 211), (212, 214), (213, 215), (216, 217), (218, 219), (220, 222), (221, 223), (224, 226), (225, 227), (228, 230), (229, 232), (231, 234), (233, 235), (236, 238), (237, 239), (240, 241), (242, 244), (243, 245), (246, 197), (248, 250), (249, 252), (251, 253), (254, 255), (256, 258), (257, 260), (259, 262), (261, 263), (264, 265), (266, 267), (268, 270), (269, 272), (271, 273), (274, 276), (275, 278), (277, 280), (279, 281), (282, 283), (284, 286), (285, 247), (288, 290), (289, 292), (291, 293), (294, 295), (296, 297), (298, 299), (300, 302), (301, 303), (304, 306), (305, 307), (308, 310), (309, 312), (311, 314), (313, 316), (315, 318), (317, 319), (320, 322), (321, 323), (324, 325), (326, 327), (328, 330), (329, 332), (331, 333), (334, 336), (335, 338), (337, 339), (340, 287)'
split_ls = strin[1:-1].split('), (')
genom_graph = [tuple(map(int, i.split(', '))) for i in split_ls]
ls = []
chu = graph_to_genome(genom_graph, ls)
print(chu)