import sys
from BioInformatics.q4_2_4 import load_genetic_code, protein_translation


def findRverseComplement(text):
    retVar =''
    for i in text[::-1]:
        if i == 'A':
            retVar+='T'
        if i == 'G':
            retVar+='C'
        if i == 'C':
            retVar+='G'
        if i == 'T':
            retVar+='A'
    return retVar


def genome_substring_single_side(dna_string, peptide, genetic_code, flag = True):
    ls = []
    string = ''
    peptide_length = len(peptide)
    for i in range(len(dna_string)-(peptide_length*3)+1):
        peptide_k_mer = dna_string.replace('T', 'U')[i:i+peptide_length*3]
        if ''.join(protein_translation(peptide_k_mer, genetic_code)) == peptide:
            #if flag:
            ret = dna_string[i:i+peptide_length*3]
            #else:
            #    ret = dna_string[i:i + peptide_length * 3][::-1]
            if not flag:
                ret = findRverseComplement(ret)
            ls.append(ret)
    return ls


def genome_substring(dna_string, peptide, genetic_code):
    return genome_substring_single_side(dna_string, peptide, genetic_code) \
    + genome_substring_single_side(findRverseComplement(dna_string), peptide, genetic_code, False)


if __name__ == '__main__':
    file = open("data/4_2_7_data")
    lines = file.read().splitlines()
    dna_string_out = lines[0]
    peptide_string = lines[1]
    genetic_code_out = load_genetic_code()
    output = genome_substring(dna_string_out, peptide_string, genetic_code_out)

    formatted_output = ' '.join(output)

    print(formatted_output)
