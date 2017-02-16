import sys
from BioInformatics.q4_2_4 import load_genetic_code, protein_translation

def load_integer_mass_table():
    hm = {}
    file = open('data/integer_mass_table')
    lines = file.read().splitlines()
    for line in lines:
        k, v = line.split(' ')
        hm[k] = v
    return hm

if __name__ == '__main__':
    file = open("data/4_2_7_data")
    lines = file.read().splitlines()
    dna_string_out = lines[0]
    peptide_string = lines[1]
    genetic_code_out = load_genetic_code()
    output = genome_substring(dna_string_out, peptide_string, genetic_code_out)

    formatted_output = ' '.join(output)

    print(formatted_output)
