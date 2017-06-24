import sys

def random_walk(edge, graph_cpy):
    if edge is None:
        edge = next(iter(graph_cpy.keys()))
    cycle = []
    while True:
        prev_edge = edge
        edge = graph_cpy[edge][0]
        cycle.append(edge)
        remove(graph_cpy, prev_edge)
        if not (graph_cpy is not None and edge in graph_cpy and graph_cpy[edge] is not None and graph_cpy[edge] != []):
            break
    return cycle

def remove(graph, edge):
    if len(graph[edge]) == 1:
        del graph[edge]
    else:
        del graph[edge][0]


def more_nodes(graph):
    return 0 < len(graph)


def unexplored_edge(cycle, graph):
    for idx, elem in enumerate(cycle):
        if elem in graph:
            return idx, elem

def eulerian_cycle(graph):
    cycle = random_walk(None, graph)
    while more_nodes(graph):
        edge_idx, edge = unexplored_edge(cycle, graph)
        cycle = cycle[edge_idx+1:] + cycle[:edge_idx+1] + random_walk(edge, graph)
    return cycle

def is_eulerian_cycle(hm):
    return is_balanced(hm) and not is_diconnected(hm)

def unformat_to_hm(ls):
    return {input.split(' -> ')[0]: input.split(' -> ')[1].split(',') for input in ls}

def is_balanced(hm):
    set_all_elem = {i for i in hm}.union({j for i in hm for j in hm[i]})
    for i in set_all_elem:
        indegree = sum([1 for j in hm if j == i])
        outdegree = sum([1 for j in hm for k in hm[j] if k == i])
        if indegree != outdegree:
            return False
    return True

def is_diconnected(hm):
    return len([True for i in hm if hm[i] == [] or hm[i] is None]) >= 1

def eulerian_path(hm):
    value_combos = list()
    for i in hm:
        value_combos += (hm[i])
    key_combos = list(hm.keys())
    source = None
    destination = None
    for i in (set(key_combos)|set(value_combos)):
        indegree = value_combos.count(i)
        outdegree = len(hm[i]) if i in hm else 0
        if indegree > outdegree:
            source = i
        elif indegree < outdegree:
            destination = i
    if source is not None and destination is not None:
        if source not in hm:
            hm[source] = [destination]
        else:
            hm[source].append(destination)
    ec_ret = eulerian_cycle(hm)
    if source is not None and destination is not None:
        fulcrum = [i for i in range(len(ec_ret)-1) if ec_ret[i] == source and ec_ret[i+1] == destination]
        final_ret = ec_ret[fulcrum[0]+1:] + ec_ret[:fulcrum[0]+1]
    else:
        final_ret = ec_ret
    return final_ret


def de_brujin_graph(list_of_k_mers):
    prefix_hm = {}
    for k_mer in list_of_k_mers:
        prefix = k_mer[:-1]
        suffix = k_mer[1:]
        add_value_to_key(prefix_hm, prefix, suffix)
    return prefix_hm

def add_value_to_key(hm, key, value):
    try:
        hm[key] += [value]
    except:
        hm[key] = [value]

def arrow_format(hm):
    return '\n'.join(['%s -> %s' % (key, ','.join(value)) for (key, value) in hm.items()])

def string_spelled_by_genome(list_of_strings):
    string = list_of_strings[0]
    for i in list_of_strings[1:]:
        string += i[-1]
    return string

def string_reconstruction(k_mer_list, k):
    de_brujin_graph_for_kmers = de_brujin_graph(k_mer_list)
    e = eulerian_cycle(de_brujin_graph_for_kmers)
    return ''.join([item[-1] for item in e[:-1]])#string_spelled_by_genome(e[:-1])

def universal_string_problem(k):
    k_mer_list = [bin(i)[2:].zfill(k) for i in range(2**k)]
    return string_reconstruction(k_mer_list, k)

if __name__ == '__main__':
    #file = open('data/string_reconstruction')

    #lines = file.read().splitlines()
    k_out = 2#int(lines[0])
    #ext_list_out = lines[1:]

    output = universal_string_problem(k_out)

    print(output)
