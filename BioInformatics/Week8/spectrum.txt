from operator import itemgetter

class Spectrum:
    def __init__(self):
        self.hm = self.load_integer_mass_table()
        self.rev_hm = self.load_mass_integer_table()

    def spectrum_graph(self, spectrum):
        # bkp = self.hm
        # self.hm = self.dummy_mass_table()
        retu = []
        spectrum = [0] + spectrum
        for i_idx in range(len(spectrum)):
            for j_idx in range(i_idx, len(spectrum)):
                diff = (spectrum[j_idx] - spectrum[i_idx])
                if diff in self.hm:
                    retu.append([spectrum[i_idx], spectrum[j_idx], self.hm[diff]])
        # self.hm = bkp
        return retu

    def load_integer_mass_table(self):
        hm = {}
        file = open('../data/integer_mass_table')
        lines = file.read().splitlines()
        for line in lines:
            k, v = line.split(' ')
            hm[int(v)] = k
        return hm

    def load_mass_integer_table(self):
        hm = {}
        file = open('../data/integer_mass_table')
        lines = file.read().splitlines()
        for line in lines:
            k, v = line.split(' ')
            hm[k] = int(v)
        return hm

    def dummy_rev_mass_table(self):
        return {'X': 4, 'Z': 5}

    def dummy_mass_table(self):
        return {4: 'X', 5: 'Z'}

    def decoding_ideal_spectrum(self, spec_graph):
        init_elems = [elem for elem in spec_graph if elem[0] != 0]
        super_set = {elem[1]: elem[2] for elem in spec_graph if elem[0] == 0 and elem[1] in self.hm}
        last = 0
        for start_elem, end_elem, diff in init_elems:
            super_set[end_elem] = super_set[start_elem] + diff
            last = super_set[end_elem]
        return last

    def decoding_all_ideal_spectra(self, spec_graph, spectrum_end_elem):
        super_set = {0:[elem[2] for elem in spec_graph if elem[0] == 0]}
        for start_elem, end_elem, diff in spec_graph:
            for i in super_set[start_elem]:
                if end_elem not in super_set:
                    super_set[end_elem] = [i + diff]
                else:
                    super_set[end_elem].append(i + diff)
        return super_set[spectrum_end_elem]

    def peptide_into_peptide_vector(self, amino_acid_string):
        intensity = self.morph_into_intensity(amino_acid_string)
        return self.intensity_to_peptide_vector(intensity)

    def intensity_to_peptide_vector(self, intensity):
        peptide_vector = []
        for i in range(max(intensity)):
            if i + 1 in intensity:
                peptide_vector.append('1')
            else:
                peptide_vector.append('0')
        return peptide_vector

    def morph_into_intensity(self, amino_acid_string):
        # self.hm = self.dummy_mass_table()
        summation = 0
        summation_set = []
        for i in amino_acid_string:
            summation += self.rev_hm[i]
            summation_set.append(summation)

        return summation_set

    def peptide_vector_into_peptide(self, peptide_vector):
        li = []
        for i in (idx for idx, x in enumerate(peptide_vector) if x == 1):
            li.append(i+1)
        ret = self.spectrum_graph(li)
        print(ret)
        return self.decoding_ideal_spectrum(ret)

    def score(self, peptide, spec_vec):
        try:
            summation = 0
            for i in self.morph_into_intensity(peptide):
                summation += spec_vec[i - 1]
            return summation
        except:
            return float('-inf')

    def peptide_id(self, proteome, spec):
        min_len = (len(spec) - 1) // max(self.hm) + 1
        max_len = (len(spec) - 1) // min(self.hm)

        best = []
        for k in range(min_len, max_len + 1):
            for i in range(len(proteome) - k):
                pep = proteome[i:i + k]
                s = self.score(pep, spec)
                best.append([s, pep])
        return sorted(best, key=itemgetter(0)).pop()

    def spectral_vector_into_peptide_vector(self, spec_vec):
        dag, last_elem = self.DAG(spec_vec)
        # back-track
        return self.backtrack_spec(last_elem[0], last_elem[1], dag)

    def backtrack_spec(self, past_elem, curr_elem, dag):
        if curr_elem == 0:
            return self.hm[past_elem - curr_elem]
        return self.backtrack_spec(curr_elem, dag[curr_elem][1], dag) + self.hm[past_elem - curr_elem]

    def DAG(self, spec_vect):
        # graph = {}
        graph = {mass: [0, 'X'] for mass in range(1, len(spec_vect) + 1)}
        graph[0] = [0, 'O']
        for mass_minus_one in range(len(spec_vect)):
            mass = mass_minus_one + 1
            intensity = spec_vect[mass_minus_one]
            new_hm = []
            for amino_mass in self.hm:
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

    def psm_search(self, spectral_vectors, proteome, threshold):
        psm_set = set()
        for spectrum_vector in spectral_vectors:
            peptide = self.peptide_id(proteome, spectrum_vector)
            if self.score(peptide, spectrum_vector) >= threshold:
                psm_set.add(peptide)
        return psm_set

    def spectral_dict_size(self, spec_vec, thres, max_score, has_prob=0.05):
        size = [[1] + [0 for y in range(1, max_score + 1)]]
        size += [[0 for y in range(max_score + 1)] for x in range(len(spec_vec) + 1)]
        for i in range(1, len(spec_vec) + 1):
            for score_cap in range(0, max_score + 1):
                size[i][score_cap] = self.eval_size(size, i, score_cap, spec_vec, max_score, has_prob)
        res = sum(size[len(spec_vec)][t] for t in range(thres, max_score + 1))
        return res

    def eval_size(self, size, i, score_cap, spec_vec, max_score, has_prob):
        summation = 0
        for int_mass in self.rev_hm.values():
            if (i - int_mass) >= 0 and spec_vec[i - 1] <= score_cap and (score_cap - spec_vec[i - 1]) < max_score + 1:
                summation += size[i - int_mass][score_cap - spec_vec[i - 1]]
        return summation*has_prob

if __name__ == '__main__':
    # input_fetched = '113 114 228 261 285 389 471 526 574 682 737 785 866 872 981 1009 1109 1122 1210 1269 1281 1368 1432 1465 1529 1616 1628 1687 1775 1788 1888 1916 2025 2031 2112 2160 2215 2323 2371 2426 2508 2612 2636 2669 2783 2784 2897'
    # input_data = list(map(int, input_fetched.split()))
    obj = Spectrum()
    # ret = obj.spectrum_graph(input_data)
    # joiner = lambda x:str(x[0])+':'+str(x[1])+'->'+str(x[2])
    # print('1st Answer')
    # print('\n'.join(list(map(joiner, ret))))
    #
    # print('\n2nd Answer')
    # ideal_spectrum = obj.decoding_ideal_spectrum(ret)
    # print(ideal_spectrum)
    #
    # ideal_spectrum = obj.decoding_all_ideal_spectra(ret, input_data[-1])
    # print(ideal_spectrum)
    # print('\n3rd Answer')
    # peptid_vector = obj.peptide_into_peptide_vector('HMDLDTTPDMDGHWRCVAIPMLILRHVHPTR')
    # print(' '.join(peptid_vector))

    # print('\n4th Answer')
    # inp_pep_vec = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1'
    # print(obj.peptide_vector_into_peptide(map(int, inp_pep_vec.split())))

    # print('\n5th Answer')
    # inp_spec_vec = '-16 0 15 20 -20 3 -13 -16 27 26 16 20 -17 22 17 -1 10 -6 2 -17 -18 28 -11 -1 12 10 19 20 7 18 -12 12 -2 -17 -15 10 21 8 9 17 25 -9 2 2 -7 -10 -17 22 20 3 9 27 21 30 4 25 -13 30 9 17 19 -8 20 3 -19 -4 -15 -16 -13 3 -19 29 -2 28 11 -6 14 19 -13 20 13 1 -9 10 0 -17 -14 29 26 22 -10 -18 3 3 16 -4 27 10 13 10 27 12 -2 21 -4 20 16 -18 24 9 -5 11 21 15 23 26 6 0 -6 11 21 18 -4 -5 6 23 23 1 10 -10 -1 27 14 14 -16 5 -16 17 4 -6 29 -17 -20 -5 -4 -8 -16 -15 8 24 -16 -1 27 -15 19 -19 13 -5 18 -7 24 12 23 14 9 -6 -20 20 17 30 -4 6 24 18 8 -16 -19 -19 18 13 -15 19 -14 6 16 18 23 -13 4 21 6 11 -8 7 4 21 21 -14 7 20 6 24 -13 -5 -6 -7 -5 15 10 23 -7 3 -5 4 -18 2 -14 11 1 18 -13 -12 0 24 11 21 30 -3 6 9 5 4 19 -9 -1 28 4 -19 4 -9 25 17 8 7 21 8 -13 -1 23 -15 -2 -13 27 11 10 27 -20 9 -20 25 -8 17 -17 -20 24 -18 21 30 -1 13 -2 28 16 8 25 14 1 7 -16 9 -16 17 14 25 -10 11 15 -16 19 -2 -5 0 15 0 10 16 -8 -12 -2 12 11 4 -5 22 16 -11 19 22 12 11 26 -18 -2 -9 10 24 -14 18 -17 -9 -13 -5 1 21 -4 23 -8 27 -7 -14 -12 -20 26 -15 2 6 4 27 15 13 -12 -15 -12 -19 23 -5 -18 19 20 29 -9 -20 -4 -17 26 28 -6 23 23 24 -10 15 14 11 10 5 -8 -13 -11 5 4 10 20 21 27 22 7 26 -14 -2 5 28 -2 16 -20 29 9 0 -11 13 14 22 9 6 20 3 8 28 29 25 19 28 7 -9 -14 3 24 30 10 10 13 7 -19 21 25 7 20 -18 -13 -5 20 9 8 10 11 0 -4 -12 2 -2 21 -7 28 -19 -11 10 5 21 -11 -20 -10 -7 -8 1 -4 20 21 14 11 -20 -3 13 16 23 5 3 -11 -3 24 23 18 -19 -15 -19 22 24 -10 22 18 17 -12 22 -6 14 -13 -8 -6 16 13 21 -3 1 -12 -12 -6 -16 7 9 2 5 7 10 -5 -2 9 16 -9 -8 -7 11 -14 1 -6 -12 22 -13 -17 -5 -17 -8 21 -14 17 21 29 -14 18 20 -7 16 -12 28 7 19 3 -2 15 27 15 20 9 2 -6 -2 4 -18 6 28 22 20 -10 -11 26 20 26 15 5 -20 9 20 -8 6 -19 25 -20 20 3 6 27 -11 19 -18 -14 -9 -8 -10 7 -2 26 3 -19 5 22 21 6 9 -11 10 19 30 -15 -5 3 -9 5 -5 -13 2 -10 26 -18 26 -15 6 8 -9 23 7 -18 29 -6 -12 -15 -2 29 13 -13 -13 -17 0 27 5 18 18 30 -6 5 3 -16 14 -9 8 -14 9 -1 -16 15 -20 21 -4 -8 -16 -13 16 -16 -8 10 -7 -14 -12 9 19 4 -5 3 30 -12 21 -2 29 29 -14 14 14 -17 -8 -3 12 -13 1 3 4 11 24 -9 -19 16 6 -4 28 -13 -18 -3 24 30 -10 30 27 4 26 -3 -13 -19 -7 -14 11 -11 17 27 -18 -8 7 13 -4 -19 6 21 -19 -15 -3 13 10 7 -3 -7 -20 -19 14 -12 5 20 -20 -12 9 19 24 14 24 2 -4 6 24 2 -1 -5 22 24 8 30 -6 -1 -1 -16 25 15 17 3 14 -14 20 -6 29 -1 18 -7 10 29 16 25 -10 -4 30 30 -9 18 -19 -12 3 26 30 2 15 16 28 28 5 -17 -2 7 -5 -16 15 17 20 -2 12 -19 -5 27 18 6 6 20 -18 15 12 26 6 -13 13 -14 -12 10 10 16 25 4 23 -3 -9 3 7 -13 11 4 -14 12 -14 -15 -15 -6 17 13 -4 28 -11 23 -17 -6 0 -12 14 -1 -10 24 -4 28 -18 -19 8 13 1 29 -16 -19 16 10 -3 -10 -10 11 9 26 18 30 4 -8 8 2 -18 9 20 -2 -8 -18 25 -20 25 14 -10 0 25 16 -17 -9'
    # spec_vec = list(map(int, inp_spec_vec.split()))
    # print(obj.spectral_vector_into_peptide_vector(spec_vec))

    # print('\n6th Answer')
    # inp1 = list(map(int,'27 -8 11 19 26 -15 -4 8 17 18 2 4 -11 -15 -16 -10 -13 7 -2 -13 7 2 10 -12 21 1 30 0 11 29 8 13 -10 27 -15 -3 -8 26 -7 15 -10 -13 -12 13 5 10 20 -18 26 27 -13 28 -3 24 -4 -20 1 -17 8 7 1 -10 6 28 18 10 -15 -10 28 0 13 27 -8 18 14 25 28 28 28 8 14 -10 11 20 -4 -16 5 -17 17 4 16 -2 25 -3 28 -8 9 5 -18 28 0 6 17 -14 8 5 20 -12 12 -4 29 -18 0 13 -7 12 -19 4 -2 -8 9 -16 22 11 15 8 -15 -13 -12 2 18 -16 7 12 13 -4 -7 19 17 -13 9 -5 -17 27 -15 20 3 27 0 10 9 6 29 10 -19 9 25 11 -8 -4 -7 10 -18 18 -18 15 13 -17 15 17 -9 -12 3 23 26 10 23 -2 2 -11 -18 4 27 -13 29 -8 -8 -6 -8 7 14 2 7 12 13 30 29 14 -4 23 -17 7 23 -6 20 13 2 -14 8 22 -7 -7 0 3 17 -14 11 24 -1 21 -18 0 -3 30 24 26 7 14 27 -11 7 15 -3 13 13 29 1 2 15 4 -6 17 -15 14 19 -3 -5 5 -18 26 -5 -9 6 4 1 -8 20 1 -11 26 -13 10 -9 9 -9 17 20 -14 -8 17 19 25 28 -11 0 -4 10 -19 -10 12 24 -9 28 -18 -12 -3 -12 -17 -6 -3 19 14 25 19 8 19 -8 9 13 4 -9 -11 -17 -8 4 -2 4 -9 25 -8 -5 -13 27 16 -19 -5 1 -13 8 7 -13 -8 -8 5 12 -2 -16 -15 10 3 14 14 4 28 26 4 -11 20 -19 3 -9 -14 14 12 16 -4 -18 12 -1 -13 16 7 -13 -11 -12 12 -3 -8 30 -18 25 10 -8 16 -15 12 9 10 -19 -14 -20 -8 -18 -9 -15 6 6 3 -11 -12 13 -15 -16 6 14 -3 9 29 -12 -15 9 9 9 17 -11 -19 -7 22 -3 25 26 -10 25 3 -11 27 -20 3 24 20 3 24 -20 28 27 8 -13 15 11 18 -4 23 -15 19 22 -19 10 22 -14 -5 1 -11 23 -6 5 0 -10 4 22 8 -18 9 -14 -2 1 9 -4 23 14 30 3 16 27 8 -16 -11 -7 5 -18 -18 19 0 0 21 -17 -1 -8 1 -10 22 15 17 11 20 9 9 -17 -15 20 26 12 -16 0 9 -1 13 -2 -20 30 28 30 -10 -17 2 -16 19 13 -20 -9 20 18 10 -7 -11 -11 18 -12 9 10 29 -10 -4 -16 10 23 28 -2 -15 28 -17 -9 6 6 -17 6 14 7 -19 12 -6 28 4 -7 -13 28 10 9 21 14 -9 20 -18 -18 -14 -20 6 8 7 -18 -3 24 9 -16 14 8 -4 -5 -6 24 3 -14 -2 26 29 0 -2 -13 5 3 28 -1 14 5 7 7 0 30 22 19 19 -3 -18 -1 30 16 -8 -16 24 -1 2 2 -7 27 -10 20 -1 1 15 -4 18 -5 1 -20 -12 -5 8 18 -10 8 -11 25 8 -19 14 -2 29 29 11 16 25 27 18 26 19 13 30 5 19 -14 0 12 -18 2 -5 7 9 -1 7 8 24 27 13 -7 29 27 -11 30 16 29 7 2 3 30 9 -9 23 24 -9 11 14 23 21 19 11 -16 -3 -2 -16 3 16 19 -19 -8 7 23 13 6 13 4 -17 28 -8 12 -16 -3 30 16 -14 29 20 2 16 -8 -6 29 16 23 -7 -4 28 -16 5 4 21 22 -14 14 23 -3 6 13 25 -7 -8 -13 18 -3 -6 17 15 27 -1 -9 1 15 -3 -3 -18 10 12 4 -4 8 16 24 -13 21 4 5 6 -16 28 -10 -10 18 -12 -8 10 15 26 30 -12 30 26 16 -5 28 -11 30 -4 -5 3 6 -12 -5 -10 2 5 5 -7 -5 14 22 10 -2 15 24 5 26 0 5 -11 -11 -17 -16 -10 10 21 -15 -14 2 -3 25 -10 9 4 18 -11 -11 -6 -11 30 -15 9 23 -20 -15 -9 -19 15 24 29 27 28 -7 14 9 26 21 1 22 6 21 28 -20 2 8 2 -12 -8 -9 -16 24 10 12 0 8 -12 13 -16 -17 17 -20 -19 8 17 -3 -1 28 19 -16 -8 3 -19 10 -17 -3 30 23 -1 0 13 -10 28 5 -12 20 18 -11 18 -1 29 7 15 -9 12 -17 25 14 -14 5 3 23 25 15 19 -18 27 -16 11 -12 -15 0 18 -14 14 26 -11 25 -1 -20 -8 -4 -16 -17 20 -13 20 -13 26 24 -5 -15 0 -14 -4 -7 15 3 18 2 -3 9 -8 15 0 -6 18 -15 0 29 -6 17 11 4 22 6 -4 13 -11 28 26 29 17 22 -12 1 13 25 18 11 0 -2 -20 -4 15 4 13 15 8 26 12 2 -1 29 -2 30 11 -1 27 26 -3 1 22 17 11 -12 -16 18 19 19 -1 -6 -14 -7 8 -2 29 25 16 25 9 -18 14 -6 28 -9 1 3 13 7 -5 17 16 12 -16 9 23 -11 -18 -8 -12 13 19 -9 -7 -11 15 7 -7 -3 28 1 -9 -4 -2 16 -14 18 24 18 21 -15 0 17 -16 13 -16 26 23 -2 -17 -6 27 -7 25 -1 9 -7 1 3 -1 -6 -5 -1 8 23 8 27 29 -16 4 -14 -4 10 24 21 30 -8 29 30 8 5 17 24 -8 -18 6 23 -11 9 16 23 11 25 -14 26 22 24 -2 4 14 6 -10 23 19 -1 -16 26 -15 -10 -1 -8 -10 -7 -16 -12 11 -4 29 21 -9 -14 19 -2 20 16 -1 -16 13 -9 14 7 28 1 4 22 -14 5 1 20 1 -19 -11 25 -7 3 1 13 15 -12 -19 4 25 7 27 -15 -18 2 18 23 -1 21 19 -20 -10 -15 0 -6 -9 30 -15 19 -16 -2 29 28 -15 -13 -18 12 -20 28 4 28 6 15 16 11 -17 -13 3 -16 -18 6 30 5 19 3 -17 11 11 -11 -2 0 5 30 6 -2 -18 -1 4 2 -4 28 -20 3 29 6 -9 7 7 0 14 8 -4 -20 21 22 20 19 4 7 20 15 10 29 27 16 -14 23 17 16 -16 6 9 4 -11 10 -19 29 -8 15 -12 10 6 0 -13 26 5 28 -2 26 28 -5 -2 1 -7 2 -12 27 8 0 -10 -4 -18 7 17 23 -15 29 0 16 -14 -13 -19 -10 -18 13 11 -6 -20 -1 25 -7 -1 -18 -5 25 21 -2 22 0 18 -5 2 27 26 -10 30 -16 18 27 28 -3 9 -20 -19 -3 -20 24 -4 -20 -15 -3 23 -13 -20 9 22 8 12 25 -16 22 2 23 -20 4 23 -16 0 22 -5 -14 1 10 18 1 4 30 15 30 28 21 13 -18 -2 0 -7 -3 11 -4 -20 13 12 26 4 -12 -4 17 -11 19 -7 13 -19 1 -16 30 29 20 5 18 19 29 6 8 -13 -15 -16 -2 -16 -5 11 -2 -17 15 10 29 -15 -10 -14 13 -13 18 28 -16 28 -15 2 -12 -17 -1 17 27 14 29 1 -6 -19 0 10 -4 -17 -8 18 2 -6 -13 0 26 -8 16 21 17 -8 2 15 28 -18 19 -13 12 -4 19 -13 17 -19 25 -6 24 9 30 1 20 -10 17 5 20 29 16 12 17 23 -10 -8 10 16 14 -5 30 -4 7 28 25 -20 27 5 23 12 -7 -17 -11 -8 -9 30 -5 -17 29 13 5 -15 16 -6 8 -1 29 -10 -16 25 15 19 -2 19 20 19 29 -9 22 10 16 -7 -20 -19 30 -6 10 -13 5 -11 8 -13 27 6 -8 16 -10 12 0 4 -8 -8 11 10 29 9 12 28 18 -14 -16 -6 23 14 -19 -16 -2 -5 18 20 4 6 18 20 25 21 6 -13 -2 5 4 24 27 30 16 23 30 1 -6 -4 0 19 18 -18 -9 0 18 15 19 29 25 8 17 -19 9 26 9 19 -5 14 7 6 10 -17 -8 1 -1 20 4 -12 24 0 -7 6 7 25 27 3 22 7 -20 -7 -11 29 1 29 -15 29 7 18 6 4 4 1 23 -11 -13 9 11 18 6 3 10 -3 23 -13 16 18 26 26 20 3 16 27 16 -16 16 30 12 20 16 -11 -17 1 11 -7 1 -10 7 -16 8 -5 10 -4 29 -4 -10 20 9 -18 0 12 14 6 15 -13 13 10 29 14 -9 20 -2 6 15 -4 26 -13 16 12 19 -12 14 29 26 -19 -15 11 16 30 -7 24 0 0 19 -11 3 30 -10 -18 22 22 4 -19 30 -16 -14 10 17 -14 -19 20 9 -4 -3 8 12 15 12 7 16 -12 20 9 3 -5 -16 8 18 -16 25 -13 -15 8 -6 -19 17 11 -8 -4 -11 -20 -4 -6 -9 -3 -12 -18 7 18 1 -20 9 21 30 5 19 16 11 14 -20 -1 -5 19 -2 11 -17'.split()))
    # inp2 = 'ELVVRWELKSSIGLEFIQGDACIPERVPQYHSEYPIGWRWVCIFFGKMVQHVDGAQHSTNDDATFDWDGFGMSFDKGQNSRTFSAHEMQNEGIHIINDKTPYTVFKCAKLMFDIGYTQLIKYHGVSEGFSHETAKPIIYRHWAYCCGCHLHEYWTSSYYHWQVEDSPDFRHLAGWSIWWKSSTLPNIQDGPIMIATPYYCYGRTVPMTVYTAAQYVVCSSSFTDQSWGLVKHKWLYKDQESGYHEMMCTQRSEHSWCDQCRCWRLCCRNGNWHVPNQCFLGHQGHERDIWKNVKFVFVQRVEWIRPQSNQHDDNEFDSSWPEQAVDSSVMGSMTFEECPTQHEFTAMEFREYVTPEKGYSDCVWDEILPMKSIDMQDTSEIHDRLLQQAWYWMAGTHLCPHCVYKYKRQPFIDSQLYCGTDEDYEFYLLWVRGWFYMWWHFINLMQMKDMGNNSTWCDTTADWFALMWDWNISPALNGWREKDPYAETAECPKKCAALWDAWMNEKHDYSKWHEIIHCGIVMFMGCDRMFQCHHKPHGQLWIDAYQTDLTNCVNWIYPQVVKVPLNYITVASKFLDTQSDWNDVDQLAHSEHHAGSENNKGPNFSTFNSPDNDWQNDAWFCVWGNDCDYFCVPCHVRPAEMIQEDLTRRNWHNGFTSWGMFNNFWHTIQQCSVYLFIWLTECELAVQNPEDTNEEPPRLAKKRRGSHSAINPQPCPTKGLMMMHEMIEKTECYLWWYMRDIFDMPQWEMANEINYWSPLIAFMRFDCDDKRLNFMIFRLGFGCQHWTYAYTGDPWTRYWLQVQDRPDILFVYDIYIRMVGFLDMASWDAMLEDPQGDQNEYKAVIYMDAYRCFYIGYTGRCVKYKFVFMEYPWCGVLDFHFMLLKTCSCFWTADPNCFLTENAHSLRRMFSTSQVNYNPDDLNVNRTEADTITEMYGGLDFYSEPSWKCLVHSLGIFFESCTTSLSADNHTPPAMLDWFCMNYHPDFRTLSKMDKIFCVTHKTTSPYKPKHGKQRHLWQQDGDYRWKTEQADDMEPYDDFGKVCEDIPHFGSLVVLQIPEHDGELDRCMLEDVLMSPVLRNYDYRWTRAVPYIRSSCYYEDKMRHDKQWHNGVRCLSGHWAHCYEHMCYNRYDEPKGSYQWVLVGWHTLGNDQHEHRTSVALGVHATWLWTMYGFSDCCGDILPHQHESNFCHCYEGVQGQQVWKRNDPMQMYQESGAFTRKYWRENRGCMSQRFEMWTAIKNACWGERWYVQHENAMCTHFTIMPKVHCYCVCWKGMVVMCYCWLYDREIKGRVQCFVKFHYYGIRVKCCNIMCANDFKEPKKSEWWCDIYKHFDDPDANERKVFQNTALWNIIHCRQSTPPVRNTGKNYQSMYDFGDSFVRTDEAGQCYVEKPFKCCPEYWHTHIMQEHGYPWWKQAIYWRMQPSKEEIHMWPTCFRYMWPPFKNTICVWRSGCWIRCIVLHEAPPLEMGKNCSTCYQAPSWSCAMIIFNERTMVDWPTEQWFMCPLRDNSHQHREYGPSPIYSACECKDTFMSDGKMPGTSDPRDSFNAFMQMMYVKQSNIGQSWQLEDSPNINFVEWLWKHGNRMCYLPDECDTATTYAWSLVPLMATHECCCFSKHYQLPQMPEYIDVRKWDAVFWRGRCYFWDCDIPYNWSYALMVVLPIVKSFPALGLPKHRDKDAVECMDSRLTNITNRYIHNEVPHKTEFLPIRMSGQKCPERAQLSAKESTKYWTQDMSCWMPCMAIIMQIIWQRYPIVDRRRENMMVVAEPQKNGDGACSMRDTSSVCMLKCMFWATTWQDVLGCKLWVHCGKRQALLHHQPNACQWIATNYISSWYTNVSFQVMDRRHKHSQTEWIDRKQFRLGIRDLHEPFFFQFNMCWLWNDYFKMWPHHCITADVDLKDMCLTVPQKGSIYKTSRELCIHYWQDNVTHACHIFIYRFDPLDPVTSIIVGPSKLCYAMKANHIFVHVHIKHWQFKEEQIDGIRTYGENVQHVDGPIRQKSHYYSVNEYRVVKEVMAGLINCTKGEIARYTKPCAPTAWDEITLDNKDRLIVSHTGQKYDPNGIRMWHEKKCNEWQEGQHKVYWEDKQMGFHYNVCNDHWWPETHHARTQQKHIPYNDKNMRVPYSWYMSRFIDVPEITWRAAPRFLEAAYCYHESMCHMTQSIVPITKYWNTVTQPGPVVGRPTMHNGDELWGPNTTQSAEDMRCCCVTMMFHCGTPYITLWSIATGYDQSQQPQALALHWCPQFNGMWMSPIFLQAKFTADMYETCMGRLPQSSHHKAKIIACPHLSVMNNMMRWNCKRHRWCILPWFYYDMISIPQYQWFCKQWSIVMTLETINNADCQCEYRSGLYRWNRKVKKQATNPCMLCYSYDKLVGLVKRNQCYNFWWFCMNKVPPPQCLMEVGYQACAWFDHKRRGGPQGVDVSPTYWKQDAGAYDCVPREGCITARAARVYVSPRHMLASPDHMPWPMADINHDCVIVMDQDKRPLSKWMETYKFANASPAEFDTRKCCRFCIAKVCMLSSIWCWGWHLLQISKMASVPRWSEKRKVPAVHVKNKESAGVADTLRYMENARRMRYPEFPHFDLKHVCNCQDYCHTGRRNKHLYNGGIADENDCCYKCAVEHHWQTNWWNKKFVQIEYCMLFYQGFSLQNHPRRKQRQAFLRQGDIEMKPRCSGWDKKQRIQHSPFDDWCFNQRDCMHWCVERTACFVAQIDEYSHHRVFNQTWVYDMRRNTAFQVMTCFCQDEKRHEMITKSYYGKITNETAMIIMVNWEINIGFRFVKHIMVCHNRDMSDVMKNNRFSAISIAAEDYSTFVYWNTFEVNSIDYGHPKNELNQHEYFPVLAFHPKSFWIPTASYWVFVARMTGYVKAADKHIMGYRMPLFNERMAICRFAFAAIHTANCICNVMGGYYGDNMGWATAEPEDTRRWAPRYVTVNEPCHSCHADKQWNFTVLTLMKVKRTKCTMCQTPQPDCNNIGEGDVYFIEFTMEVKMLPAVFYVSNQVVFIGTDCYMNNNQNHKQQEESWNCCEAITHTLPKRWSARFPIEMGSCMYPLWFISSIAWLDWIYPFETHMLIEPMQPIMMTDSNENQLEMLDRPMRIWCIQCGEEPVPRWTYDDDEVKTGHCETYMCFEQYCHGVSFASRHLKCFNEMYMRMGDMTIWVCEAMEWICRIVHTRPVNYMETNFCSMMHSCRFTGLHGMHTNSQVEKCNYYGTYWKRWCCMANEEKQTFFFTFWSQFVVDEASECKQPKEKIVMKPTQVSFDHYLMLCMLFMMPDFHKNWDMKMSILPPMIHTVPICDQAIGVKQGGFNLPYCMYKVTEVHHYGDDNKWMDPIEPSSIITFANQVGAFKGQLYVSMMQVELVELICIDEEDYMNNGIDSFGVTQTAYFTYGDWGQKYRSPLQWYLWHELTCPEGTDDVCIEQMMYNPAFPQSSLPEITNQKWTVLLYNWYCQYYLNVEEAQAMGNKHAKTELLFLRKKGYHPRNITTPMIVSMLFWLALWCIMSIPFLLPADVNTACMHNTKCRHGDSVNDRIYIERWCPNANTNIIETMVFHYQCGEALAYRAHTWNTHETCWIKYWCIDCWRFIHPVQIWCVEQRYHLMARQKSLSANYASKSWLAFRCYALAKHISWDMNIIDCPGDKAIGVSYDQLALCCWDSWFQMFLIHDSPMRHYFLDWWMSDYSYTLKMVDSYDKNVMHLPLGELDVCISLLLCAFTLCQRYFHINMWMNFLILECCFAVRTVNFACDELSGAGDHENMIMQRVFCYRVKHKWRQLQACQHDKQDDAAMYHGHCQECIHHAWYIKSQNWTWYDAGHPRANTDDNWIIKMDEEEESLGWILDMTCNSSVIEPPECFKRMDHVAIEVHGPIFPTVAQKEDIGAPPGQIRANKIFCWLIFHNFSGAKIDHYCRIDASNWFNTMQLIPSFRTNATNMHEFVHNNKTNREVTTDFIPNPIKRMTGHDAAPYGYALHMSKRVQICKISASESINNFHEACADFDQALWKNALVDNLIFWKTWECAEWEASDQRHWTRLAWIQEALAMAHLAALYEWSDYFFWQFSATYHVQGFVGEWGANEWWDDAMNRWYEGFVCDTMVSKVQEEAEMPSGNGCVPTDGYPVESWGVVIEDRPYKCFFKPCQYRDCCINTLEPDDWHNCMPWMFSWLMGWSWHFNNVIDNCNPSCNRSSLLYMRANQRVDQASKTGPYNCCCCGSMRRPAKWKLPTHRSIMEGRCCTCQTKVRIKNFNEPCYAVSISLKSHFPELYVTCAWMREGMTRWNVRKRQWSKFCEIMSHPWKHDFNLINELLWYKRKWAYDYGFALTFIEYWHGQCWEWKCCYWFGIKFPKGSFHDIMCSGFQYKVFAIHSDTRVFVEQLILRGFKMHLEWWNQDHMHRWIVKPYEFWKQCQWIFHKPQEEMYVQFEWVEHAELGQANTKIRTPPGYGIHHDNFCESGNCFNIYKYFDQKHPHSVICKFSQGANLDFCYDPRQSGTSNLPWGDQFCTWLGDKHQGDMNVENGWCMVYHHQAILCSPDPKFMRHWGMAAMSNDYSAPFLPRPWFLAISKHHPATINKDAENLDVQLTDGCHHSKKYPVQTVQTYWYNDDVDEVPYPKCVFWAQAGMLFAPVRTGIKSPRPAPFYFGWALIMVKWDEDGFSRQITNSTEQGPLTWNGMNGTALMYENSHRAITSNIKFGCDFGVCHSAHINHMWMVQCYADYYYARHYLKSHSGLAFNPQVCPFFNPAKQYMRFGKTNKVNVYVGEWLKQYDQDAGKLVFFHQSQFDFISSNPKQCIMMNESLPDMKIMFPFNWREKTIMCVMMRCIIHGSLQVWSATQWGCLQWFEVITNYYAPCNRVAWYASNLCECHVMGWWDKNNEHCHCAQRDFTDYAYSFEYIDRVIHMKSVQPIRYADLPMTVNGRHYTWHQKRPSGQCMMWWYACTEWNIPHPCYHNDNDGDQLPTGGARFWGWYWTWTNYYPQEVTPHYCHTIWMLHENSWRNIGAATFHFT'
    # peptid_vector = obj.peptide_id(inp2, inp1)
    # print(peptid_vector)

    # spectral_vec = []
    # spectral_vec.append(list(map(int,
    #                              '-10 8 -15 -8 28 29 8 -17 -8 19 6 -9 7 16 -15 -13 -9 29 21 17 -12 28 22 -7 5 -20 -8 13 15 20 -11 21 -5 8 20 21 16 8 -4 4 -20 25 -18 11 15 20 12 -18 -6 -19 -10 -5 10 7 26 -10 -18 18 -8 8 -7 -4 -13 21 -6 3 23 17 24 -10 -13 7 -8 13 -11 13 -12 5 9 -7 18 3 14 25 -20 8 -19 -15 28 14 -3 26 21 23 -18 2 -15 23 -4 0 8 4 10 15 27 1 1 -8 19 10 15 18 -15 22 -5 3 1 4 6 24 16 19 25 -15 23 10 24 23 13 0 -8 -8 28 23 -20 15 -13 13 25 24 -4 20 30 -6 4 28 26 27 1 -20 5 -19 22 -7 -9 10 3 30 13 9 28 4 -7 -16 18 -15 -5 -9 7 29 24 18 8 27 29 8 11 -18 3 2 18 2 0 16 -4 1 -10 -4 18 27 26 -5 28 1 -17 -6 -2 3 -4 10 13 6 29 8 -20 4 16 18 29 9 -8 -17 21 21 -1 2 27 -7 15 27 20 -19 -13 16 12 -19 -20 -11 18 17 19 30 4 -4 9 -4 -9 -13 -6 6 28 2 -11 -2 30 -3 15 19 3 14 21 -14 -1 -17 9 0 7 -3 2 -10 -20 -3 -17 -10 14 8 1 28 24 -6 -15 6 12 27 13 25 26 11 1 -12 16 -14 11 5 -17 21 28 -4 14 13 -11 2 24 28 -7 1 -2 2 14 1 7 17 7 26 5 -18 20 23 6 22 29 13 1 -18 27 21 -20 -6 -7 -12 -6 7 12 17 15 30 11 19 9 7 -10 23 -8 26 15 26 19 -18 -9 12 -5 -10 -4 23 29 11 -7 20 -5 -14 -16 -8 -16 10 9 -13 -4 -13 0 -7 1 4 22 24 4 24 9 15 23 24 17 -10 27 14 13 -3 -12 17 13 1 18 -17 -6 1 15 30 -14 13 27 -18 3 5 20 13 17 26 11 -8 8 25 -9 1 17 -18 -15 -12 -11 16 9 20 19 -2 15 17 -14 2 -4 -14 -17 -19 -12 8 -14 22 -13 1 30 -20 5 28 9 -4 -18 -16 -20 8 24 3 -2 21 27 22 -17 -15 22 20 0 0 8 2 9 -5 -2 -9 16 -8 -17 8 23 8 -17 6 -4 27 -9 -9 -5 -16 -6 -3 -4 16 20 14 30 5 -14 3 23 -3 -14 29 -4 -15 20 -10 13 19 -15 3 5 23 10 -10 -19 8 -17 17 1 -18 4 30 20 -4 -7 14 28 6 27 -11 12 16 4 25 -19 7 -1 13 19 -1 18 -9 15 2 -20 0 15 -1 8 2 11 17 7 -3 -2 -12 -17 -2 -15 22 23 17 -13 21 12 30 7 7 -12 -19 25 23 -1 1 24 20 -16 -13 23 19 14 18 7 -9 10 1 23 27 3 19 12 -4 5 -2 -7 -1 23 -5 -2 25 -20 -16 22 4 -17 -1 14 26 -16 29 -15 3 -5 19 11 1 30 13 -19 4 -15 2 -14 19 -11 -11 1 -16 3 -5 -5 0 23 -3 -10 -3 20 11 24 17 26 11 8 14 -10 -4 -13 -16 25 22 5 22 18 -10 -10 16 0 22 -19 12 26 15 -12 2 5 8 8 -5 -16 9 -19 8 10 -16 -9 -16 -10 -3 -3 -15 1 25 19 -10 21 2 13 9 30 9 -10 25 -16 12 19 6 -12 -9 15 12 -12 0 3 2 15 18 -12 2 7 20 -10 19 14 8 16 0 4 18 0 -5 23 14 -17 6 15 -15 -5 25 25 14 -2 16 -19 -3 13 16 -7 24 10 22 -18 25 2 28 -16 -16 21 4 -2 -16 -20 29 -3 8 9 30 11 6 13 19 26 -1 -7 25 -11 -9 7 16 22 -7 -7 21 0 23 24 -14 26 3 -5 -6 -18 5 16 14 13 19 6 23 1 -1 -12 -18 -5 21 19 26 -5 -8 -19 -8 24 15 11 18 -15 -18 -14 -7 22 -5 18 -4 15 19 4 28 2 -19 1 10 27 -10 -19 27 -10 0 -17 -5 -3 22 -5 30 -1 2 26 -13 -7 -12 -4 19 -8 19 25 15 -1 9 2 -2 27 27 -19 19 14 -10 22 -14 -20 22 23 28 11 -6 -12 26 30 1 27 26 -17 26 -2 8 -20 25 27 -13 14 24 0 -7 1 -5 12 -14 12 21 28 -1 12 19 2 27 -1 8 26 -7 10 30 -6 -18 4 -14 8 27 29 10 -3 9 6 -1 -8 -10 -8 -9 -16 5 26 -13 -16 24 19 -20 -11 4 -12 20 25 4 30 -9 25 -13 18 -6 11 -3 18 29 24 -19 28 18 -14 10 27 27 2 26 1 28 -11 28 24 5 24 6 12 -13 21 -14 17 -6 27 -14 22 20 -16 -12 10 24 25 -10 25 3 -1 -6 -8 -5 -10 -6 -2 -9 29 1 23 12 19 26 -5 -8 -12 -3 15 21 30 -14 -18 11 -2 -13 -20 -19 5 28 -17 8 11 26 -12 7 9 -11 25 11 -11 -18 10 1 -18 12 25 12 -19 -8 23 27 7 23 -10 -12 -15 -6 -9 19 15 14 -11 12 17 -20 9 27 24 -9 -6 -10 15 25 -11 16 -8 26 19 12 13 -4 -6 -6 20 -4 8 1 3 15 23 -10 29 13 -12 -16 -9 14 23 25 16 8 28 25 -20 -8 23 25 26 9 -4 -8 25 11 -12 -11 0 11 3 -5 -18 6 19 -18 18 -6 26 -3 15 19 4 2 -6 3 28 8 22 -2 19 -9 4 8 22 -16 4 -20 -14 -4 28 15 4 23 -15 15 18 -10 -7 19 -18 16 -13 24 -11 -19 8 28 24 -14 -15 11 15 -8 4 -13 3 -4 23 -17 6 6 -7 -8 -15 8 18 -17 13 6 14 17 26 -18 -2 -4 -19 19 9 -9 -2 -1 -9 24 30 18 8 6 20 -10 -8 20 -12 -13 -19 2 -20 -15 11 16 -11 18 11 -20 20 19 -5 22 -2 14 18 10 26 5 26 9 18 30 -8 -5 29 -13 29 19 28 -14 -8 -11 3 -19 17 9 25 7 -18 14 29 -13 4 2 5 -15 -19 -6 15 16 18 18 -3 9 26 9 2 4 -13 6 -9 21 12 14 17 11 25 -11 -18 17 -11 3 16 13 -19 0 -7 7 10 -10 -3 -10 -8 3 -11 -16 -1 18 2 -17 26 16 -10 -18 30 9 24 -14 19 6 -16 -17 -6 10 13 -5 8 16 -5 -17 -4 26 14 -12 4 -4 18 14 7 -7 -15 8 -1 -10 -17 17 -11 -9 -15 10 1 29 -3 20 5 -7 -10 1 30 23 23 -13 5 -7 3 7 2 -8 -6 20 -11 21 0 -17 30 28 17 25 30 14 -5 16 -19 23 18 12 24 8 7 5 3 12 1 -18 -4 -16 27 29 14 11 9 -15 4 -18 -10 22 -18 6 7 -19 -17 -18 26 14 9 20 -6 -6 -6 -6 11 29 -5 19 22 -6 -3 29 1 23 7 -9 16 27 -11 17 -12 -2 -11 -14 15 20 -5 -1 17 -3 27 30 25 -11 23 13 -15 -16 24 -15 6 -13 -18 -9 -10 -8 5 -1 -16 19 -17 30 -20 -12 5 27 28 -1 21 -11 1 -18 19 -2 7 -12 26 24 5 20 20 -10 21 -13 24 19 1 3 27 -8 20 10 -3 4 -8 15 2 1 -16 11 29 8 -2 -20 10 -9 23 -9 30 -11 4 26 17 -2 26 28 20 -16 -9 6 28 11 -15 -9 -3 13 25 13 9 18 9 9 -7 -18 3 26 17 -11 -16 18 -7 3 -1 7 -18 4 0 2 1 9 10 21 4 -16 21 27 -20 -12 28 8 22 15 -4 -7 20 23 23 9 -12 -15 -12 -4 26 4 -5 -15 14 30 13 16 30 12 6 -12 -1 5 19 -13 21 -6 21 30 2 2 30 6 19 -8 25 -16 21 11 -12 14 6 23 20 -19 -15 1 15 16 7 -5 9 28 6 -10 -16 28 -13 8 24 -15 -6 8 -7 -5 -16 -10 24 2 -6 2 -17 19 0 10'.split())))
    # spectral_vec.append(list(map(int, '-4 2 -2 -4 4 -5 -1 4 -1 2 5 -3 -1 3 2 -3'.split())))
    # proteome = 'XXXZXZXXZXZXXXZXXZX'
    # threshold = 5
    # print(obj.psm_search(spectral_vec, proteome, threshold))

    inp_vec = '-10 11 3 10 11 12 -6 -5 4 4 -2 9 6 -8 9 -6 -1 10 -6 14 4 13 1 -6 5 -7 13 0 -1 12 -2 11 7 -10 9 13 14 -7 7 -9 -6 4 14 2 -9 1 12 13 15 6 15 13 -6 -10 -10 -8 -8 -7 -10 -7 -6 -4 6 9 -6 7 11 -1 -8 1 9 -5 6 7 -3 -10 -9 -1 4 7 7 -6 14 -6 12 15 7 8 11 -5 8 -8 12 -3 -1 -7 -6 9 13 12 -3 7 7 6 3 1 2 4 10 11 -10 -3 14 9 6 8 -9 1 5 -6 -8 5 -7 6 -6 -7 4 1 -3 7 5 10 11 12 0 -10 12 13 11 3 9 8 -10 9 -8 0 15 4 1 1 -4 12 2 4 0 15 -10 4 -10 -10 6 -5 -5 0 10 -5 8 1 14 6 -3 12 9 -7 -4 -9 -9 7 2 6 4 -10 -9 8 -4 -5 0 7 -4 -3 5 12 -10 3 -6 -10 6 10 -6 3 -5 15 4 14 -1 10 -9 13 11 -7 -5 -3 14 15 6 -3 -8 -5 0 12 0 12 2 8 -1 6 2 4 -6 3 11 -4 -10 1 -5 0 14 -5 -6 -1 15 13 12 -10 6 4 0 14 -1 5 15 13 4 -6 13 12 7 14 6 15 10 -9 1 -8 10 9 6 6 2 9 -2 5 11 -4 -6 -10 -7 10 9 8 -6 1 -8 2 -1 -1 -4 -2 0 9 11 -6 9 11 5 5 14 7 -10 14 -4 7 4 14 14 14 8 2 5 14 -4 13 7 10 14 -7 -6 11 -7 -2 -6 -3 1 -7 7 10 15 -6 -2 0 14 1 9 -7 5 -3 -5 5 -5 0 -4 1 3 11 9 -4 -3 -4 0 1 -4 15 -8 -3 0 0 11 -9 11 5 -9 1 -1 -7 -3 8 -9 11 5 4 4 -7 11 -1 -4 -5 7 -7 7 3 6 13 -1 11 -3 13 11 4 3 2 3 0 12 -6 3 12 -10 -8 -9 12 -2 12 5 -3 5 11 5 1 -2 3 5 1 11 6 -6 -2 0 -7 15 14 15 -10 0 6 13 9 10 -2 10 2 8 6 -6 5 -2 1 13 8 14 1 -4 11 11 -8 0 8 5 5 9 -1 -7 3 15 -7 -8 -3 11 9 0 10 2 1 13 4 0 -6 15 15 -1 10 3 1 2'
    spec_vec_out = list(map(int, inp_vec.split(' ')))
    threshold = 30
    max_score_out = 200
    print(obj.spectral_dict_size(spec_vec_out, threshold, max_score_out))


