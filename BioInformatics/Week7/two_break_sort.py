#single_team
from BioInformatics.Week7.colored_edges import colored_edges
from BioInformatics.Week7.trial import graph_to_genome
from BioInformatics.Week7.find_cycles import two_break_distancio


def two_break_sorting(p, q):
    curr_synt = [p]
    while two_break_distancio(p, q) > 0:
        cycles = mix_and_match(colored_edges(p), colored_edges(q))
        p = two_break_on_genome(p, cycles[0][0], cycles[0][1], cycles[0][3], cycles[0][2])
        curr_synt.append(p)
    return curr_synt

def mix_and_match(red_cycle, blue_cycle):
    cycles = []
    hm = {x: [0 for y in range(2)] for x in range(len(red_cycle) + len(blue_cycle))}
    visited = [0 for x in range(len(red_cycle) + len(blue_cycle))]
    for red_edge in red_cycle:
        hm[red_edge[0] - 1][0] = red_edge[1] - 1
        hm[red_edge[1] - 1][0] = red_edge[0] - 1
    for blue_edge in blue_cycle:
        hm[blue_edge[0] - 1][1] = blue_edge[1] - 1
        hm[blue_edge[1] - 1][1] = blue_edge[0] - 1

    for edge_idx in range(len(red_cycle) + len(blue_cycle)):
        if not visited[edge_idx]:
            visited[edge_idx] = True
            start = edge_idx
            cycle = [start + 1]
            link_till_end(start, edge_idx, hm, cycle, cycles, visited, 0)
    return cycles


def link_till_end(start, edge_idx, hm, cycle, cycles, visited, colour):
    edge_idx = hm[edge_idx][colour]
    if edge_idx == start:
        cycles.append(cycle)
        return
    cycle.append(edge_idx + 1)
    visited[edge_idx] = True
    colour = 0 if colour == 1 else 1
    link_till_end(start, edge_idx, hm, cycle, cycles, visited, colour)


def remove_it(graph, edge, tail_edge):
    if edge not in graph:
        temp = tail_edge
        tail_edge = edge
        edge = temp
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
    return hm



def two_break_on_genome_graph(genome_graph, i, i_prime, j, j_prime):
    genome_graph = make_hm(genome_graph)
    remove_it(genome_graph, i, i_prime)
    remove_it(genome_graph, j, j_prime)
    add_elem(genome_graph, i, j)
    add_elem(genome_graph, i_prime, j_prime)
    print(back_to_tuple(genome_graph))
    return back_to_tuple(genome_graph)


def back_to_tuple(genome_graph):
    new_set = set()
    for i in genome_graph:
        for j in genome_graph[i]:
            new_set.add((i, j))
    return list(new_set)


def two_break_on_genome(p, i, i_prime, j, j_prime):
    genome_graph = colored_edges(p)
    genome_graph = two_break_on_genome_graph(genome_graph, i, i_prime, j, j_prime)
    p = graph_to_genome(genome_graph)
    return p


def format_output(out):
    # um = lambda x: '+' + str(x) if x > 0 else str(x)
    # for i in (two_break_sorting([[1, -2, -3, 4]], [[1, 2, -4, -3]])):
    #     print str(''.join(str([list(map(um, s)) for s in i]))).replace('[', '(').replace(']',')')#] == range(4)[::-1]
    print_str = ''
    for i in out:
        print_str += '('
        for j in i:
            print_str += str(j).replace('[', '(').replace(']', ')')
        print_str += ')\n'
    print(print_str)

# genome_graph = [(2, 4), (3, 8), (7, 5), (6, 1)]
# a = two_break_on_genome_graph(genome_graph, 1, 6, 3, 8)
# print(a)

get_str = '(+1 -2 -3 +4)'
p_ = [list(map(int, get_str[1:-1].split(' ')))]
get_str = '(+1 +2 -4 -3)'
q_ = [list(map(int, get_str[1:-1].split(' ')))]
format_output(two_break_sorting(p_, q_))