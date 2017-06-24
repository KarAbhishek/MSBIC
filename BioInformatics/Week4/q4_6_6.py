from BioInformatics.Week4.q4_4_4 import load_integer_mass_table
from BioInformatics.Week4.c4_11_2_linear import linear_spectrum


def non_consistent(peptide, spectrum, mass_table):
    return mass(peptide, mass_table) not in spectrum

def mass(peptide, mass_table):
    sum = 0
    for amino_acid in peptide:
        sum += int(mass_table[amino_acid])
    return sum

def expand(peptides, mass_table):
    new_peptide = []
    for peptide in peptides:
        for i in init_pep_out:
            new_peptide.append(i+peptide)
    return new_peptide

def parent_mass(spectrum):
    return spectrum[-1]

def cyclopeptide_sequencing(spectrum, mass_table):
    peptides = set([''])
    amino_acid = [i for i in mass_table]
    amino_acid_mass = [int(mass_table[i]) for i in amino_acid]
    while peptides is not None or peptides != [] or peptides or len(peptides) == 0:
        peptides = expand(peptides, mass_table)
        for pep_idx, peptide in enumerate(peptides[:]):
            if mass(peptide, mass_table) == parent_mass(spectrum):

                if set(linear_spectrum(peptide, amino_acid, amino_acid_mass)) == set(spectrum):
                    print(peptide)
                peptides.remove(peptide)
            elif non_consistent(peptide, spectrum, mass_table):
                peptides.remove(peptide)
        init_pep = peptides

if __name__ == '__main__':
    mass_table_out = load_integer_mass_table()
    spectrum_out = '0 113 128 186 241 299 314 427'
    spectrum_out_list=list(map(int, spectrum_out.split(' ')))
    init_pep_out = [i for i in mass_table_out if mass_table_out[i] in spectrum_out_list]
    cyclopeptide_sequencing(spectrum_out_list, mass_table_out)

