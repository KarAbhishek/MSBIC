def load_integer_mass_table():
    keys = []
    values = []
    file = open('../data/integer_mass_table')
    lines = file.read().splitlines()
    for line in lines:
        k, v = line.split(' ')
        keys.append(k)
        values.append(int(v))
    return keys, values


def cyclo_spectrum(peptide, amino_acid, amino_acid_mass):
    prefix_mass = [0]
    for i in range(0, len(peptide)):
        for j in range(20):
            if amino_acid[j] == peptide[i]:
                prefix_mass.append(prefix_mass[len(prefix_mass)-1]+amino_acid_mass[j])
    peptide_mass = prefix_mass[-1]
    cyclic_spec = [0]
    for i in range(len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            cyclic_spec.append(prefix_mass[j] - prefix_mass[i])

            if i>0 and j<len(peptide):
                cyclic_spec.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(cyclic_spec)

if __name__ == '__main__':
    peptide_out = 'LEQN'
    amino_acid_out, amino_acid_mass_out = load_integer_mass_table()
    output = cyclo_spectrum(peptide_out, amino_acid_out, amino_acid_mass_out)
    print(' '.join(map(str, output)))
