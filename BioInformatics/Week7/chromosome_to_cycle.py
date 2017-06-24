def chromosome_to_cycle(chromosome):
    nodes = [0 for x in range(2*len(chromosome))]
    for j in range(len(chromosome)):
        i = chromosome[j]
        if i > 0:
            nodes[2 * j] = 2*i-1
            nodes[2 * j+1] = 2 * i
        else:
            nodes[2 * j] = 2 * abs(i)
            nodes[2 * j+1] = 2 * abs(i) - 1
    return nodes

# def chromosome_to_cycle(chromosome):
#     for j in range(len(chromosome)):
#         i = chromosome[j]
#         if i > 0:



if __name__ == '__main__':
    seq_set = '(+1 -2 -3 +4)'
    seq_set = seq_set[1:-1]
    split_seq = seq_set.split(' ')
    chromosome = list(map(int, split_seq))
    print('('+' '.join(map(str, chromosome_to_cycle(chromosome)))+')')
