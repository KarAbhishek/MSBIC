from BioInformatics.string_reconstruction_orig import unformat_to_hm
def degree(node, graph):
    value_combos = list()
    for i in graph:
        value_combos += (graph[i])
    key_combos = list(graph.keys())
    indegree = value_combos.count(node)
    if node in graph:
        outdegree = len(graph[node])
    else:
        outdegree = 0
    return indegree, outdegree


def isolated_cycle(graph):
    cycle = [graph]
    deg_cycle = degree(cycle[-1], graph)
    while deg_cycle[0] == 1 and deg_cycle[1] == 1:
        deg_cycle = degree(cycle[-1], graph)
        cycle.append(deg_cycle[cycle[-1]][0])
        if deg_cycle[cycle[-1]][0] == deg_cycle[cycle[-1]][1]:
            return cycle
    return None


def maximal_non_branching_paths(graph):
    paths = []
    for node in graph:
        deg_node = degree(node, graph)
        if not (deg_node[0] == 1 and deg_node[1] == 1):
            if deg_node[1] > 0:
                w = graph[node]
                for outgoing_edge in w:
                    non_branching_path = [outgoing_edge]
                    deg_w = degree(node, graph)
                    while deg_w[0] == 1 and deg_w[1] == 1:
                        non_branching_path.append(outgoing_edge)
                        w = graph[w]
                    paths.append(non_branching_path)
    for cycle in isolated_cycle(graph):
        paths.append(cycle)
    return paths

maximal_non_branching_paths(unformat_to_hm(['1 -> 2','2 -> 3','3 -> 4,5','6 -> 7','7 -> 6']))
