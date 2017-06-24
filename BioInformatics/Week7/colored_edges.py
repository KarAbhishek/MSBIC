from BioInformatics.Week7.chromosome_to_cycle import chromosome_to_cycle

def colored_edges(p):
    edges = []
    for chromosome in p:
        nodes = chromosome_to_cycle(chromosome)
        for j in range(len(chromosome)):
            edges.append((nodes[2*j-1], nodes[2*j]))
    return edges

if __name__ == '__main__':
    inp = '(+1 +2 +3 +4 +5 +6)'
    fmt_p = inp[1:-1].split(')(')
    fmt_p = [list(map(int, i.split(' '))) for i in fmt_p]
    print(str(colored_edges(fmt_p))[1:-1])