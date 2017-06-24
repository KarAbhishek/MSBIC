import sys


def BLOSUM62(sl=None):
    file = ''
    if sl == '':
        file = open('data/BLOSUM62.txt')
    elif sl == 'PAM':
        file = open('data/PAM.txt')
    lines = file.read().splitlines()
    matrix_rows = [line[1:].split() for line in lines]
    blasum_map = {i: idx for idx, i in enumerate(matrix_rows[0])}
    if sl is not None:
        ret = blasum_map, [list(map(int, single)) for single in matrix_rows[1:]]
    else:
        import pandas as pd
        ret = pd.DataFrame([list(map(int, single)) for single in matrix_rows[1:]], index=list(blasum_map.keys()),
                           columns=list(blasum_map.keys()))
    return ret


def LCS_backtrack(v, w, indel_pen, blosum):
    s = [[0 for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    backtrack = [['N' for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    max_list = [0, 0, 0]
    min_list = [sys.maxsize, sys.maxsize, sys.maxsize]
    # for i in range(1, len(v) + 1):
    #     s[i][0] = s[i-1][0]-indel_pen
    #     backtrack[i][0] = 'N'
    # for j in range(1, len(w) + 1):
    #     s[0][j] = s[0][j-1]-indel_pen
    #     backtrack[i][0] = 'N'
    blosum_dict, blosum_matrix = blosum
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            if v[i - 1] == w[j - 1]:
                stub = 1
            else:
                stub = -1
            s[i][j] = max(s[i - 1][j] - indel_pen, s[i][j - 1] - indel_pen,
                          s[i - 1][j - 1] +
                          stub)
            if s[i][j] == s[i - 1][j] - indel_pen:
                backtrack[i][j] = 'D'
            elif s[i][j] == s[i][j - 1] - indel_pen:
                backtrack[i][j] = 'R'
            # elif s[i][j] == 0:
            #     backtrack[i][j] = 'Z'
            else:
                backtrack[i][j] = 'C'
            #if s[i][j] > max_list[0]:
    column_list = [s[row][j] for row in range(len(w), len(v))]
    max_list = [s[i][j],  column_list.index(max(column_list))+ len(w), len(w)]
            #if s[i][j] <= min_list[0]:
                #min_list = [s[i][j], i, j]
    return backtrack, s[max_list[1]][j], max_list, min_list


def output_lcs(backtrack, v, w, i, j, first_string_list, second_string_ls, end1, end2):
    # if i == end1 or j == end2:
    #     if i > j:
    #         first_string_list.append(v[:i - j])
    #         second_string_ls.append('-' * (i - j))
    #     if j > i:
    #         second_string_ls.append(w[:j - i])
    #         first_string_list.append('-' * (j - i))
    #     return
    # if backtrack[i][j] == 'Z':
    #     return
    if backtrack[i][j] == 'D':
        output_lcs(backtrack, v, w, i - 1, j, first_string_list, second_string_ls, end1, end2)
        first_string_list.append(v[i - 1])
        second_string_ls.append('-')
    elif backtrack[i][j] == 'R':
        output_lcs(backtrack, v, w, i, j - 1, first_string_list, second_string_ls, end1, end2)
        second_string_ls.append(w[j - 1])
        first_string_list.append('-')
    elif backtrack[i][j] == 'C':
        output_lcs(backtrack, v, w, i - 1, j - 1, first_string_list, second_string_ls, end1, end2)
        first_string_list.append(v[i - 1])
        # if v[i-1] != w[j-1]: print('Smells fishy')
        second_string_ls.append(w[j - 1])


# dp_change(16810,
# list(map(int, '24,21,14,8,5,3,1'.split(','))))
sys.setrecursionlimit(2000)
file = open('data/global_alignment_data.txt')
lines = file.read().splitlines()
str1 = lines[0]
str2 = lines[1]

blosum = BLOSUM62('PAM')
z, score, papa, endo = LCS_backtrack(str1, str2, 1, blosum)

sec_str_ls = []
first_str_ls = []
# if len(str1) > len(str2):
#     sec_str_ls.append('-' * (len(str1) - len(str2)))
# else:
#     first_str_ls.append('-' * (len(str2) - len(str1)))

backtrack = output_lcs(z, str1, str2, papa[1], papa[2], first_str_ls, sec_str_ls, endo[1], endo[2])

print(score)
print(''.join(first_str_ls))
print(''.join(sec_str_ls))
# file = open('man_hat_data')
# lines = file.read().splitlines()
# n = int(lines[0].split(' ')[0])
# m = int(lines[0].split(' ')[1])
# down = [list(map(int,single_line.split(' '))) for single_line in lines[1:n+1]]
# right = [list(map(int,single_line.split(' '))) for single_line in lines[n+2:]]
# print(manhattan_problem(n, m, down, right))
