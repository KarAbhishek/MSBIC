from BioInformatics.Week7.cycle_to_chromosome import cycle_to_chromosome


def graph_to_genome(genome_graph):
    p = []
    recurse(p, genome_graph)
    for nodes in p:
        chromosome = cycle_to_chromosome(nodes)
        p.append(chromosome)
    return p


def odd_node(n):
    return n[0] % 2 != 0


def recurse(collect_tuple, genome_graph):
    if len(genome_graph) == 0 or (
                    collect_tuple != [] and (odd_node(collect_tuple[-1]) + 1 in i[1]
                                             for i in genome_graph)):
        return
    for idx, i in enumerate(genome_graph):
        if collect_tuple != [] and odd_node(collect_tuple[-1]) + 1 == i[0] or odd_node(collect_tuple[-1]) + 1 == i[1]:
            collect_tuple.append(i)
            recurse(collect_tuple, genome_graph[:idx] + genome_graph[idx + 1:])


strin = '(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)'
split_ls = strin[1:-1].split('), (')
genom_graph = [tuple(map(int, i.split(', '))) for i in split_ls]
print(graph_to_genome(genom_graph))
