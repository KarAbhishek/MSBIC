from BioInformatics.Week7.cycle_to_chromosome import cycle_to_chromosome
from BioInformatics.Week7.find_cycles import eulerian_cycle, find_cycles
#
# def graph_to_genome(genome_graph):
#     p = list()
#     for cycle in get_cycles(genome_graph):#eulerian_cycle(find_cycles(genome_graph)):
#         nodes = cycle
#         chromosome = cycle_to_chromosome(nodes)
#         p.append(chromosome)
#     return p

def graph_to_genome(genome_graph):
    hm = {i: -1 for i in range(len(genome_graph) * 2)}
    for i in genome_graph:
        hm[i[0] - 1] = i[1] - 1
        hm[i[1] - 1] = i[0] - 1
    p = []
    visited = []
    for i in genome_graph:
        source = i[0]
        if source not in visited:
            visited.append(source)
            dest = source - 1 if source % 2 == 0 else source + 1
            find_cycle(source, dest, hm, p, visited, [])
    return p

def get_cycles(genome_graph):
    cycle = [[]]
    for i in range(len(genome_graph)-1):
        cycle[-1].append(genome_graph[i][0])
        cycle[-1].append(genome_graph[i][1])
        if abs(genome_graph[i][1] - genome_graph[i+1][0]) != 1:
            #new cycle
            cycle[-1] = cycle[-1][-1:] + cycle[-1][:-1]
            cycle.append([])

    cycle[-1].append(genome_graph[i+1][0])
    cycle[-1].append(genome_graph[i+1][1])
    cycle[-1] = cycle[-1][-1:] + cycle[-1][:-1]
    return cycle


def find_cycle(source, dest, hm, p, visited, p_fragment):
    elem = source // 2 if source % 2 == 0 else -(source + 1) // 2
    p_fragment.append(elem)
    next_elem = hm[source - 1] + 1
    visited.append(next_elem)
    if next_elem == dest:
        p.append(p_fragment)
        return
    new_source = next_elem - 1 if next_elem % 2 == 0 else next_elem + 1
    visited.append(new_source)
    find_cycle(new_source, dest, hm, p, visited, p_fragment)


if __name__ == '__main__':
    strin = '(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)'
    split_ls = strin[1:-1].split('), (')
    genom_graph = [tuple(map(int, i.split(', '))) for i in split_ls]
    ls = []
    chu = graph_to_genome(genom_graph)
    for i in chu:
        add = lambda x:'+'+str(x) if x > 0 else str(x)
        print('(' + ' '.join((map(add, i))) + ')', end ='')