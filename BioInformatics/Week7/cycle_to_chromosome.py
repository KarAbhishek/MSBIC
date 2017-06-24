def cycle_to_chromosome(nodes):
    chromosome = []
    for j in range(1, len(nodes)//2+1):
        if nodes[2*j-2] < nodes[2*j - 1]:
            chromosome.append(nodes[2*j-1]//2)
        else:
            chromosome.append(-nodes[2*j - 2]//2)
    return chromosome

if __name__ == '__main__':
    seq_set = '(2 1 4 3 6 5 7 8)'
    seq_set = seq_set[1:-1]
    split_seq = seq_set.split(' ')
    nodes = list(map(int, split_seq))
    forma = lambda x:'+'+str(x) if x>0 else str(x)
    print('('+' '.join(list(map(forma, cycle_to_chromosome(nodes))))+')')