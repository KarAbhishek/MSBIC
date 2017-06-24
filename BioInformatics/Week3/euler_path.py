import sys
import random

def random_walk(edge, graph_cpy):
    if edge is None:
        edge = next(iter(graph_cpy.keys()))
    cycle = []
    while True:
        prev_edge = edge
        edge = graph_cpy[edge][0]
        cycle.append(edge)
        remove(graph_cpy, prev_edge)
        try:
            if not (graph_cpy is not None and edge in graph_cpy and graph_cpy[edge] is not None and graph_cpy[edge] != []):
                break
        except:
            print()
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
        #try:
        edge_idx, edge = unexplored_edge(cycle, graph)
        cycle = cycle[edge_idx+1:] + cycle[:edge_idx+1] + random_walk(edge, graph)
        #except:
            #print()
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
    if source not in hm:
        hm[source] = [destination]
    else:
        hm[source].append(destination)
    ec_ret = eulerian_cycle(hm)
    fulcrum = [i for i in range(len(ec_ret)-1) if ec_ret[i] == source and ec_ret[i+1] == destination]
    return ec_ret[fulcrum[0]+1:] + ec_ret[:fulcrum[0]+1]


if __name__ == '__main__':
    file = open('data/input')

    lines = file.read().splitlines()
    hm = unformat_to_hm(lines)

    output = eulerian_path(hm)
    #
    formatted_output = '->'.join(output)
    #
    print(formatted_output)
