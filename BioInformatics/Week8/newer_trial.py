from operator import itemgetter


def dummy_mass_table():
    return {4: 'X', 5: 'Z'}

def spectral_vector_into_peptide_vector(spec_vec):
    dag, last_elem = DAG(spec_vec)
    # back-track
    return backtrack_spec(last_elem[0], last_elem[1], dag)

def load_integer_mass_table():
    hm = {}
    file = open('../data/integer_mass_table')
    lines = file.read().splitlines()
    for line in lines:
        k, v = line.split(' ')
        hm[int(v)] = k
    return hm

def backtrack_spec(past_elem, curr_elem, dag, hm=load_integer_mass_table()):
    if curr_elem == 0:
        return hm[past_elem - curr_elem]
    return backtrack_spec(curr_elem, dag[curr_elem][1], dag, hm) + hm[past_elem - curr_elem]


def DAG(spec_vect, hm=load_integer_mass_table()):
    # graph = {}
    graph = {mass: [0, 'X'] for mass in range(1, len(spec_vect) + 1)}
    graph.update({0:[0, 'O']})
    for mass_minus_one in range(len(spec_vect)):
        mass = mass_minus_one + 1
        intensity = spec_vect[mass_minus_one]
        new_hm = []
        for amino_mass in hm:
            if mass >= amino_mass:
                diff = mass - amino_mass
                ind_dag_wt = intensity + graph[diff][0]
                new_hm.append((ind_dag_wt, diff))
            else:
                new_hm.append((float('-inf'), 'X'))
        max_dag_wt, max_prev = sorted(new_hm, key=itemgetter(0)).pop()
        graph[mass] = [max_dag_wt, max_prev]
        last_elem = mass, max_prev

    return graph, last_elem


def decoding_all_ideal_spectra(self, spec_graph, spectrum_end_elem):
    super_set = {0:[elem[2] for elem in spec_graph if elem[0] == 0]}
    for start_elem, end_elem, diff in spec_graph:
        for i in super_set[start_elem]:
            if end_elem not in super_set:
                super_set[end_elem] = [i + diff]
            else:
                super_set[end_elem].append(i + diff)
    return super_set[spectrum_end_elem]



inp_spec_vec = '-17 4 -3 -1 5 -14 -4 -4 28 30 7 23 27 -19 26 -15 15 -20 -7 -12 -1 15 -9 3 30 -15 -2 -4 26 18 17 19 20 4 25 -1 14 -20 1 9 5 5 12 -4 -18 28 -2 19 -16 5 -20 19 17 22 -20 26 4 15 -1 -8 16 -14 15 -14 19 3 18 8 0 -14 -11 22 -4 -14 15 1 -10 12 -11 -20 14 -4 -12 8 -16 -14 15 -15 15 -11 28 19 -10 17 12 28 23 -2 3 -19 -9 -18 -3 24 21 -19 -8 -17 -17 16 20 5 24 18 -8 -17 18 11 30 -1 -10 18 -11 7 -5 -13 14 13 -19 -8 30 4 17 26 -19 18 14 29 -2 -19 8 -12 -17 11 26 7 13 1 29 -17 0 -9 5 30 3 -2 25 28 6 5 4 -10 -4 -8 7 -18 4 21 15 30 8 -13 28 14 19 26 -8 1 11 -8 20 -18 26 30 -12 26 4 7 -11 30 -17 -7 -19 20 28 -20 6 -8 -15 -14 -16 -10 24 -17 18 25 9 5 12 7 21 28 -12 -6 29 -10 4 10 -15 23 -7 29 -14 27 2 7 16 1 -2 7 -10 -6 -8 17 -19 -7 -11 4 -11 11 -16 1 16 5 -8 2 2 -10 -13 6 27 22 -18 14 15 9 12 22 -1 -10 12 -9 8 5 24 -16 22 -7 16 26 18 -18 -17 -20 10 -6 -6 6 13 14 -16 -16 -4 -15 -11 -12 20 -2 -20 -18 -5 5 29 -19 6 -12 -5 17 26 21 24 -3 1 -19 0 15 22 9 -6 13 12 10 -5 6 15 -14 4 -12 18 -20 29 14 -12 13 20 -19 8 -15 -18 13 -19 19 14 -20 13 28 -7 -18 16 3 -11 23 -1 16 27 25 -13 14 -14 14 6 27 2 16 8 -4 20 25 -11 -7 -5 -10 -13 -9 -14 7 23 -12 8 4 17 -5 12 3 -7 19 -16 25 20 17 -19 -3 -14 3 22 19 5 -4 -10 28 15 15 -20 -9 22 26 24 -12 3 0 10 -2 -12 15 18 12 23 5 -7 7 4 0 -1 -2 18 -5 14 24 16 24 19 21 14 -19 -8 22 -2 19 -11 27 -17 5 9 -4 5 25 1 1 24 21 -16 -19 24 14 4 15 3 15 -19 14 27 3 1 30 23 -13 4 4 1 16 26 14 -2 8 -5 -9 12 28 -20 10 10 5 -9 -12 25 -1 -17 29 2 -15 8 -2 17 28 20 22 -13 7 14 28 3 10 3 -1 -4 22 2 14 13 -17 -15 -1 -20 -13 -16 -17 -4 -4 -10 13 2 -8 22 -2 28 26 0 16 -15 -2 7 11 3 4 13 18 30 -3 -6 12 5 23 4 15 4 6 -7 20 0 16 12 -18 -20 27 24 -3 25 1 -13 -9 15 26 -13 6 27 -13 13 -5 -5 -19 -6 25 17 -4 -7 25 25 20 9 -2 -13 19 6 -1 -14 23 -17 -11 1 -11 -1 -5 8 -16 15 22 3 -14 28 16 26 24 4 8 16 14 2 26 -17 -16 -2 -6 -4 4 5 -7 4 16 9 -15 17 16 20 3 -12 27 0 19 10 15 -4 -11 7 24 11 12 -16 -14 -15 -2 4 14 3 9 16 17 -4 -11 6 -9 15 -20 11 -6 -11 18 20 16 28 21 4 -17 -14 -16 -18 19 21 23 12 -8 -20 -9 -8 4 -18 30 25 -1 30 16 -14 -10 3 0 7 -3 -20 -14 -8 20 -4 7 -19 -1 14 14 1 16 27 5 6 21 29 19 -13 -14 13 26 0 8 -12 -11 17 5 1 28 1 12 -20 -4 -14 6 21 10 -2 12 23 6 19 30 -14 -10 -2 9 19 3 20 10 27 12 -20 -1 20 21 15 16 -16 27 -16 19 20 -7 -16 11 -6 -8 5 9 -2 15 -2 11 16 12 -3 24 -17 17 23 17 28 23 6 5 -12 16 -15 0 3 14 18 30 22 17 24 22 17 -10 27 -6 -6 5 -5 1 11 18 27 24 21 -8 6 28 -9 24 2 24 -2 10 0 -5 -4 15 23 30 -6 7 -19 -8 -16 28 11 17 1 -8 18 -20 4 23 22 -10 19 -7 -15 1 -7 5 26 4 5 -15 10 30'
spec_vec = list(map(int, inp_spec_vec.split()))
print(spectral_vector_into_peptide_vector(spec_vec))