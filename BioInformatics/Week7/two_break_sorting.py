#double_team
from BioInformatics.Week7.find_cycles import two_break_distancio, colored_edges


def two_break_sorting(p, q):
    # red = colored_edges(q)
    # curr_synt = [p]
    # while two_break_distancio(p, q) > 0:
    #     cycles = mix_and_match(colored_edges(p), red)
    #     p = two_break_on_genome(p, cycles[0][0], cycles[0][1], cycles[0][2], cycles[0][3])
    #     curr_synt.append(p)
    return #curr_synt


def remove_it(graph, edge, tail_edge):
    if len(graph[edge]) == 1:
        del graph[edge]
    else:
        for idx, i in enumerate(graph[edge]):
            if i == tail_edge:
                del graph[edge][idx]


def add_elem(hm, source, dest):
    if source in hm and dest in hm[source]:
        return
    try:
        hm[source].append(dest)
    except KeyError:
        hm[source] = [dest]

def make_hm(graph):
    hm = {}
    for first, second in graph:
        add_elem(hm, first, second)
        add_elem(hm, second, first)
    return hm



def two_break_on_genome_graph(genome_graph, i, i_prime, j, j_prime):
    genome_graph = make_hm(genome_graph)
    remove_it(genome_graph, i, i_prime)
    remove_it(genome_graph, i_prime, i)
    remove_it(genome_graph, j, j_prime)
    remove_it(genome_graph, j_prime, j)
    add_elem(genome_graph, i, j)
    add_elem(genome_graph, j, i)
    add_elem(genome_graph, i_prime, j_prime)
    add_elem(genome_graph, j_prime, i_prime)
    back_to_tuple(genome_graph)
    return back_to_tuple(genome_graph)

def back_to_tuple(genome_graph):
    new_set = set()
    for i in genome_graph:
        for j in genome_graph[i]:
            new_set.add((i, j))
    return new_set

genome_graph = [(2, 4), (3, 8), (7, 5), (6, 1)]
a = two_break_on_genome_graph(genome_graph, 1, 6, 3, 8)
print(a)