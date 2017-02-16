import sys


def paired_composition(k, d, text):
    k_d_mer_list = []
    for idx in range(len(text)-k-k-d+1):
        k_d_mer_1 = text[idx:idx+k]
        k_d_mer_2 = text[idx+k+d:idx+k+k+d]
        k_d_mer_list.append('('+k_d_mer_1+'|'+k_d_mer_2+')')
    return sorted(k_d_mer_list)


if __name__ == '__main__':

    k_out = 3
    d_out = 2
    text_out = 'TAATGCCATGGGATGTT'

    output = paired_composition(k_out, d_out, text_out)

    formatted_output = ''.join(output)

    print(formatted_output)
