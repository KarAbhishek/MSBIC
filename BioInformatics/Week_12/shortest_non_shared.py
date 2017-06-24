from BioInformatics.Week_12.doesnt_work_suffix_tree_trial_9 import get_suffix_tree
from BioInformatics.Week_12.doesnt_work_suffix_tree_const_6 import can_traverse


def shortest_nonshared_substring(str1, str2):
    suffix_tree = get_suffix_tree(str2)
    for k in range(2, len(str1) + 1):
        non_shared = False
        for i in range(len(str1) - k + 1):
            if not can_traverse(str1[i: i + k], suffix_tree):
                non_shared = True
        if non_shared:
            ret = str1[i: i + k]
            break
    return ret


if __name__ == '__main__':
    seq_1 = 'GAGCGATGTGTAAAGACGGGCCTAGTGTGTTATTGGTGAGGATCCGCAAATTCCGCTTTAACATCGCTCAACCGTCCACGAGCAGCTCGCGGCTTGTTTGATTTTGCTCACCCGGAACTAAGCCTTCAATAATTGCGGGACACTTCTACTTTCCATGTATTAAAACCTTATAATTCCGAGAGACTGACATTTTAACCCAGGGATTCTCGGGGCTTGTAGGTCACTGGCGTTAGCTCTGCCAATGTTCTTCATCGCCGAAATTAAACTCGTGACCTTGCCCTACGGTTTGAAACGTTGGATTCCTAGCATTCGGTGCAACGGGAGTTCCATACCAGCAGTTAAGGACCGGGTTGCCCCGTCCCACTACGAGCAGCCGTTAGAAAACAGTTCTACCGGAGGCTATCCCGCACCACGGGTTTTCTTAGTGAAAGGGACTGCGCAGCCATCGAAGAGTAGGGGGAGTCAGAGAGAGGCAGGCTTGTTGGGCTGATACATCTAGTTTACTAAATAGCCTTAATGGCGTCCCCCTCTTCGTTGATGCGCGTGGCCTGTGAAATTAGGCAGGGCCCAATGAGCAAGGCTGATTACTATCTAATTGCAGAGCGCAATGCTCTCATATATTATTATCCATGAATCTCATTTCACTAATCAGAAACGTG'
    seq_2 = 'CACCTCGTCAATACAACAAAAGGCGGCTCGCTTAAAGGGCGCAGCTAGTTCCTCCCCCTCTCATTGGGACATAGTCAACCTGCTAATCCGGATTCGAATGGATTATTCCGTAATTGAACGGTAATTTAGTGAGCTTCGCAGTAAACGATAGATGCGAGCTCTAGCAGGCCACTGACTATATAAACGCCAACACTAGTGCCGTGCATGGACGACTCGATGTACTATAGATTTGCACAGGTATGACCGGAGGAGCGGGACTGCCTAGGCTATAGGGAACGGGGAGTATTGGGAGCCTTTTAGGCCCTCGTCATATCCCTTAACGTTCCCGCGCAGCTAAATTGTGGAACCGGAAAACAATGGATCTGCTTATTTTTGTAGGCTTGGTTAAGCGAAACGGATCAAAATAAACAAAGAATTAATCAATGAACTAACCAACGAAGTAAGCAAGGATATACATAGATTTATTCATTGATCTATCCATCGATGTATGCATGGACACAGACTTACTCACTGACCTACCCACCGACGTACGCACGGAGAGTTAGTCAGTGAGCTAGCCAGCGAGGTAGGCAGGGTTTTCTTTGTTCCTTCGTTGCTTGGTCTCTGTCCCTCCGTCGCTCGGTGTGCCTGCGTGGCTGGGCCCCGCCGGCGCGGGGAAA'

    out = shortest_nonshared_substring(seq_1, seq_2)
    print(out)