from BioInformatics.Week_4.q4_4_3 import find_subpeptides

def load_integer_mass_table():
    hm = {}
    file = open('../data/integer_mass_table')
    lines = file.read().splitlines()
    for line in lines:
        k, v = line.split(' ')
        hm[k] = int(v)
    return hm

def theoretical_spectrum(sub_pep_list, mass_table):
    ls=[0]
    ls1=[' ']
    for sub_pep in sub_pep_list:
        sum= 0
        for i in sub_pep:
            sum+=int(mass_table[i])
        ls.append(sum)
        ls1.append([sub_pep])
    return sorted(ls)


if __name__ == '__main__':
    peptide_string_out = 'FTPLPWIATEMPTM'
    sub_pep_list_out = find_subpeptides(peptide_string_out)
    mass_table_out = load_integer_mass_table()
    output = theoretical_spectrum(sub_pep_list_out, mass_table_out)

    formatted_output = ' '.join(map(str,output))

    print(formatted_output)
