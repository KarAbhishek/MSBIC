from BioInformatics.Week7.colored_edges import colored_edges


def find_cycles(graph):
    hm = {}
    for first, second in graph:
        add_elem(hm, first, second)
        add_elem(hm, second, first)
    return hm


def add_elem(hm, source, dest):
    if source in hm and dest in hm[source]:
        return
    try:
        hm[source].append(dest)
    except KeyError:
        hm[source] = [dest]


def in_degree_and_out_degree(real_hm):
    degree_map = {}
    #out-degree
    for i in real_hm:
        for j in real_hm[i]:
            if j in degree_map:
                degree_map[j][0] += 1
            else:
                degree_map[j] = [1]
    #in-degree
    for i in real_hm:
        degree_map[i].append(len(real_hm[i]))

    print(degree_map)
    print(is_balanced(degree_map))


def is_balanced(degree_map):
    for i in degree_map:
        m, n = degree_map[i]
        if m != n:
            return False
    return True


def random_walk(edge, graph_cpy):
    if edge is None:
        edge = next(iter(graph_cpy.keys()))
    cycle = []
    while True:
        prev_edge = edge
        edge = graph_cpy[edge][0]
        cycle.append(edge)
        remove(graph_cpy, prev_edge)
        remove_it(graph_cpy, edge, prev_edge)
        if not (graph_cpy is not None and edge in graph_cpy and graph_cpy[edge] is not None and graph_cpy[edge] != []):
            break
    return cycle

def remove(graph, edge):
    if len(graph[edge]) == 1:
        del graph[edge]
    else:
        del graph[edge][0]

def remove_it(graph, edge, tail_edge):
    if len(graph[edge]) == 1:
        del graph[edge]
    else:
        for idx, i in enumerate(graph[edge]):
            if i == tail_edge:
                del graph[edge][idx]

def unexplored_edge(cycle, graph):
    for idx, elem in enumerate(cycle):
        if elem in graph:
            return idx, elem

def more_nodes(graph):
    return 0 < len(graph)


def eulerian_cycle(graph):
    cycle = random_walk(None, graph)
    cycle_num = 1
    print(cycle)
    while more_nodes(graph):
        edge_t = unexplored_edge(cycle, graph)
        if edge_t is None:

            print('New Cycle')
            cycle = random_walk(None, graph)
        else:
            edge_idx, edge = edge_t
            cycle = cycle[edge_idx+1:] + cycle[:edge_idx+1] + random_walk(edge, graph)
        print(cycle)
        cycle_num += 1
    print('cycle_num is ', cycle_num)
    return cycle_num, [cycle[-1]]+cycle


def blocks(p):
    block_size = 0
    for i in p:
        block_size += len(i)
    return block_size

def two_break_distancio(p, q):
    p_q_comb = colored_edges(p) + colored_edges(q)
    hm = find_cycles(p_q_comb)
    in_degree_and_out_degree(hm)
    cycles_p_q = eulerian_cycle(hm)
    return blocks(p) - cycles_p_q[0]


if __name__ == '__main__':
    seq_set = '' #Enter string here
    seq_set = seq_set[1:-1]
    spl = lambda x: x.split(' ')
    split_seq = list(map(spl, seq_set.split(')(')))
    p_ = [list(map(int, i)) for i in split_seq]
    seq_set = '' #Enter string here
    seq_set = seq_set[1:-1]

    split_seq = list(map(spl, seq_set.split(')(')))
    q_ = [list(map(int, i)) for i in split_seq]

    print(two_break_distancio(p_, q_))