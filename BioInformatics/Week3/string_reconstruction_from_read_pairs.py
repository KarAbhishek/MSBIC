from BioInformatics.string_reconstruction_orig import string_spelled_by_genome, eulerian_path
#
# def paired_de_bruijn(gapped_patterns, k, d):
#     main_paired_hm = {}
#     for gapped_pattern in gapped_patterns:
#         if gapped_pattern[:-1] in main_paired_hm:
#             main_paired_hm[gapped_pattern[:-1]].append(gapped_pattern[1:])
#         else:
#             main_paired_hm[gapped_pattern[:-1]] = gapped_pattern[1:]
#     paired_e = eulerian_path(main_paired_hm)
#     return string_spelled_by_gapped_patterns(paired_e, k, d)


def paired_de_bruijn(gapped_patterns, k, d):
    main_paired_hm = {}
    for unsplit_gap in gapped_patterns:
        gapped_pattern = unsplit_gap.split('|')
        if (gapped_pattern[0][:-1], gapped_pattern[1][:-1]) in main_paired_hm:
            main_paired_hm[(gapped_pattern[0][:-1], gapped_pattern[1][:-1])].append((gapped_pattern[0][1:], gapped_pattern[1][1:]))
        else:
            main_paired_hm[(gapped_pattern[0][:-1], gapped_pattern[1][:-1])] = [(gapped_pattern[0][1:], gapped_pattern[1][1:])]
    paired_e = eulerian_path(main_paired_hm)
    return string_spelled_by_gapped_patterns(paired_e, k, d)


def string_spelled_by_gapped_patterns(gapped_patterns, k, d):
    first_patterns = []
    second_patterns = []
    for gapped_pattern in gapped_patterns:
        #split_gap = gapped_pattern.split('|')
        first_patterns.append(gapped_pattern[0])
        second_patterns.append(gapped_pattern[1])
    prefix_string = string_spelled_by_genome(first_patterns)
    suffix_string = string_spelled_by_genome(second_patterns)
    for i in range(k+d+1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return "there is no string spelled by the gapped patterns"

    prefix_string += suffix_string[-(k+d):]
    return prefix_string


file = open('data/gap')
lines = file.read().splitlines()
place_holder = lines[0].split(' ')
gapped_patterns_out = lines[1:]
k_out = int(place_holder[0])
d_out = int(place_holder[1])
print(paired_de_bruijn(gapped_patterns_out, k_out, d_out))