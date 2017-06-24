from BioInformatics.Week7.cycle_to_chromosome import cycle_to_chromosome
from functools import reduce


def graph_to_genome(genome_graph):
    p = []
    for nodes in genome_graph:
        chromosome = cycle_to_chromosome(nodes)
        p.append(chromosome)
    return p


def select(tuple_collection, with_elem):
    for idx, i in enumerate(tuple_collection):
        if with_elem in i:
            return idx, i


# def recurse(tupl, tupl_list, ls):
#     if len(tupl_list) == 0:
#         return
#     selected_idx, selected_tupl = [(tupl_idx, tupl_i) for tupl_idx, tupl_i in enumerate(tupl_list) if tupl_i == max(tupl)+1][0]
#     if selected_idx is None:
#         return
#     ls.append(selected_tupl)
#     recurse(selected_tupl, tupl_list[:selected_idx]+tupl_list[selected_idx+1:], ls)


def graph_to_genom(collected_tuples, ls):
    if len(collected_tuples) == 0:
        return

    def unioner(x, y): return x.union(y)
    sol_tuple_set = reduce(unioner, map(set, collected_tuples))
    selected_idx, selected_tuple = select(tuple_collection=collected_tuples, with_elem=min(sol_tuple_set))
    if ls == [] or min(selected_tuple) != min(ls[-1][0])+1:# cycle_break
        #mini_ls = selected_tuple #mini_ls reboot
        ls.append([selected_tuple])
    else:
        ls[-1].append(selected_tuple)
    graph_to_genom(collected_tuples[:selected_idx] + collected_tuples[selected_idx + 1:], ls)

#
# def graph_to_genom(collected_tuples, ls):
#
#     sol_tuple_set = {tupl[0] for tupl in collected_tuples}
#     selected_idx, selected_tuple = select(tuple_collection=collected_tuples, with_elem=min(sol_tuple_set))
#     # ls = []
#     ls.append(selected_tuple)
#     graph_to_genom(collected_tuples[:selected_idx]+collected_tuples[selected_idx+1:], ls)


strin = '(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)'
split_ls = strin[1:-1].split('), (')
genom_graph = [tuple(map(int, i.split(', '))) for i in split_ls]
ls = []
graph_to_genom(genom_graph, ls)
print(ls)