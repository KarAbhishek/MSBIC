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


def linear_spectrum(peptide, amino_acid, amino_acid_mass):
    prefix_mass = [0]
    for i in range(1, len(peptide)):
        for j in range(1, 20):
            if amino_acid[j] == peptide[i]:
                prefix_mass.append(prefix_mass[len(prefix_mass)-1]+amino_acid_mass[j])
    linear_spec = [0]
    for i in range(len(peptide)-1):
        for j in range(i+1, len(peptide)):
            linear_spec.append(prefix_mass[j] - prefix_mass[i])
    return sorted(linear_spec)

if __name__ == '__main__':
    peptide_out = 'FTPLPWIATEMPTM'
    amino_acid_out, amino_acid_mass_out = load_integer_mass_table()
    output = linear_spectrum(peptide_out, amino_acid_out, amino_acid_mass_out)
    print(' '.join(map(str, output)))
