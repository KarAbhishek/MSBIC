from operator import itemgetter
def load_integer_mass_table():
    hm = {}
    file = open('../data/integer_mass_table')
    lines = file.read().splitlines()
    for line in lines:
        k, v = line.split(' ')
        hm[int(v)] = k
    return hm


def spectrum_graph(spectrum):
    retu = []
    spectrum = [0] + spectrum
    for i_idx in range(len(spectrum)):
        for j_idx in range(i_idx, len(spectrum)):
            diff = (spectrum[j_idx] - spectrum[i_idx])
            hm = load_integer_mass_table()
            if diff in hm:
                retu.append([spectrum[i_idx], spectrum[j_idx], hm[diff]])
    return retu

def morph_into_intensity(self, amino_acid_string):
    # self.hm = self.dummy_mass_table()
    summation = 0
    summation_set = []
    for i in amino_acid_string:
        summation += self.rev_hm[i]
        summation_set.append(summation)

    return summation_set

def score(peptide, spec_vec):
    try:
        summation = 0
        for i in morph_into_intensity(peptide):
            summation += spec_vec[i - 1]
        return summation
    except:
        return float('-inf')

def peptide_id(proteome, spec, hm=load_integer_mass_table()):
    min_len = (len(spec) - 1) // max(hm) + 1
    max_len = (len(spec) - 1) // min(hm)

    best = []
    for k in range(min_len, max_len + 1):
        for i in range(len(proteome) - k):
            pep = proteome[i:i + k]
            s = score(pep, spec)
            best.append([s, pep])
    return sorted(best, key=itemgetter(0)).pop()

def psm():
    pass

def psm_search(spectral_vectors, proteome, threshold):
    psm_set = set()
    for spectrum_vector in spectral_vectors:
        peptide = peptide_id(spectrum_vector, proteome)
        if score(peptide, spectrum_vector) >= threshold:
            psm_set.add(psm(peptide, spectrum_vector))
    return psm_set


some_spectrum = '57 71 154 185 301 332 415 429 486'
input_data = list(map(int, some_spectrum.split()))
ret = spectrum_graph(input_data)
print(ret)
print(path(ret, spectrum_end_elem=input_data[-1]))
#decoding_ideal_spectrum()