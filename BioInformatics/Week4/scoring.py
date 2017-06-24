from BioInformatics.Week4.c4_11_2_cyclic import cyclo_spectrum, load_integer_mass_table


def score(peptide, spectrum):
    spectrum = list(map(int, spectrum.split(' ')))
    ans = 0
    init_spec = cyclo_spectrum(peptide,k,v)
    init_spec.sort()
    i = 0
    j = 0
    while i<len(init_spec) and j<len(spectrum):
        if init_spec[i] == spectrum[j]:
            ans += 1
            i += 1
            j += 1
        else:
            if init_spec[i]<spectrum[j]:
                i += 1
            else:
                j += 1
    return ans

k,v = load_integer_mass_table()
print(score('NQEL', '0 99 113 114 128 227 257 299 355 356 370 371 484'))