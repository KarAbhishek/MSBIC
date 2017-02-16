import random

def random_motif_search(dna, k, t):
    bla = [random.randint(0, len(dna[0])-k) for i in (range(t))]
    motif = [i[bla[idx]:bla[idx]+k] for idx, i in enumerate(dna)]
    best_motif = motif
    best_score = score(best_motif)
    while True:
        pro_file = create_profile(motif)
        motif = [most_probable_kmer_given_profile(dna_single, k, pro_file) for dna_single in dna]
        scor = score(motif)
        if scor < score(best_motif):
            best_motif = motif[:]
            best_score = scor
        else:
            return best_score, best_motif

def hamming_distance(str1, str2):
    count = 0
    for idx, elem in enumerate(str1):
        if str2[idx] != elem:
            count += 1
    return count


def most_probable_kmer_given_profile(text, k, profile):
    hm = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    max_pro = float('-inf')
    for i in range(len(text) - k + 1):
        k_mer = text[i:i + k]
        pro = 1.0
        for idx, single_char in enumerate(k_mer):
            pro *= profile[hm[single_char]][idx]
        if pro > max_pro:
            max_pro = pro
            max_k = k_mer
    return max_k


def create_profile(motif):
    hm = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    l = [[0 for x in range(len(motif[0]))] for y in range(4)]
    for i in range(len(motif[0])):
        # hm = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for x in range(len(motif)):
            l[hm[motif[x][i]]][i] += 1.0 / len(motif)
    l = add_pseudo_counts(l)
    return l

def add_pseudo_counts(true_profile):
    for i in range(len(true_profile)):
        for j in range(len(true_profile[0])):
            n, d = (float(true_profile[i][j])).as_integer_ratio()
            true_profile[i][j] = (n+1.0)/(d+4.0)
    return true_profile

def numToSymbol(sym):
    if sym == 0:
        return 'A'
    if sym == 1:
        return 'C'
    if sym == 2:
        return 'G'
    if sym == 3:
        return 'T'


def consensus_string(motif):
    l = create_profile(motif)
    string = '0' * len(l[0])
    for i in range(len(l[0])):
        maxim = float('-inf')
        for j in range(len(l)):
            if l[j][i] > maxim:
                maxim = l[j][i]
                string = string[:i] + numToSymbol(j) + string[i + 1:]
    return string


# def score(motif):
#     l = create_profile(motif)
#     #string = '0'*len(l[0])
#     sum_em = 0
#     for i in range(len(l[0])):
#         maxim = float('inf')
#         for j in range(len(l)):
#             if l[j][i] < maxim:
#                 maxim = l[j][i]
#                 sum_em += maxim*len(motif)
#     return sum_em

def score(motifs):
    pro_fil = create_profile(motifs)
    sum_em = 0
    for j in range(len(pro_fil[0])):
        maxim = float('-inf')
        for i in pro_fil:
            if i[j] > maxim:
                maxim = i[j]
        sum_em += (1 - maxim) * len(motifs)
    return sum_em

# def score(motifs):
#     consensus = consensus_string(motifs)
#     return min([hamming_distance(consensus, motif) for motif in motifs])




file = open('data/rand')
lines = file.read().splitlines()
K, T = map(int, lines[0].split(' '))
#t = int(lines[0][2])
DNA = lines[1:]
min_b1 = float('inf')
the_one = []
for i in range(1000):
    b1, b2 = random_motif_search(DNA, K, T)
    if b1<min_b1:
        min_b1 = b1
        the_one = b2

print('\n'.join(the_one))




