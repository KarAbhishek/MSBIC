import sys


def BLOSUM62(sl=None):
    file = open('data/BLOSUM62.txt')
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
    lower = [[0 for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    upper = [[0 for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    middle = [[0 for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    l_lower = [[0 for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    l_upper = [[0 for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    l_middle = [[0 for i in range(len(w) + 1)] for j in range(len(v) + 1)]

    backtrack = [['N' for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    for i in range(1, len(v) + 1):
        lower[i][0] = lower[i-1][0]-indel_pen
        backtrack[i][0] = 'N'
    for j in range(1, len(w) + 1):
        upper[0][j] = upper[0][j-1]-indel_pen
        backtrack[i][0] = 'N'
    for i in range(1, len(v) + 1):
        upper[i][0] = upper[i - 1][0] - indel_pen
        backtrack[i][0] = 'N'


    blosum_dict, blosum_matrix = blosum
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            upper[i][j] = max(upper[i - 1][j] - indel_pen, upper[i][j - 1] - indel_pen,
                          upper[i - 1][j - 1] +
                          blosum_matrix[blosum_dict[v[i - 1]]][
                              blosum_dict[w[j - 1]]])
            if upper[i][j] == upper[i - 1][j] - indel_pen:
                backtrack[i][j] = 'D'
            elif upper[i][j] == upper[i][j - 1] - indel_pen:
                backtrack[i][j] = 'R'
            else:
                backtrack[i][j] = 'C'
    return backtrack, upper[len(v)][len(w)]

def output_lcs(backtrack, v, w, i, j, first_string_list, second_string_ls):
    if i == 0 or j == 0:
        if i > j:
            first_string_list.append(v[:i - j])
            second_string_ls.append('-' * (i - j))
        if j > i:
            second_string_ls.append(w[:j - i])
            first_string_list.append('-' * (j - i))
        return
    if backtrack[i][j] == 'D':
        output_lcs(backtrack, v, w, i - 1, j, first_string_list, second_string_ls)
        first_string_list.append(v[i - 1])
        second_string_ls.append('-')
    elif backtrack[i][j] == 'R':
        output_lcs(backtrack, v, w, i, j - 1, first_string_list, second_string_ls)
        second_string_ls.append(w[j - 1])
        first_string_list.append('-')
    elif backtrack[i][j] == 'C':
        output_lcs(backtrack, v, w, i - 1, j - 1, first_string_list, second_string_ls)
        first_string_list.append(v[i - 1])
        # if v[i-1] != w[j-1]: print('Smells fishy')
        second_string_ls.append(w[j - 1])



def output_lcs(backtrack, v, w, i, j, first_string_list, second_string_ls):
    if i == 0 or j == 0:
        if i > j:
            first_string_list.append(v[:i - j])
            second_string_ls.append('-' * (i - j))
        if j > i:
            second_string_ls.append(w[:j - i])
            first_string_list.append('-' * (j - i))
        return
    if backtrack[i][j] == 'D':
        output_lcs(backtrack, v, w, i - 1, j, first_string_list, second_string_ls)
        first_string_list.append(v[i - 1])
        second_string_ls.append('-')
    elif backtrack[i][j] == 'R':
        output_lcs(backtrack, v, w, i, j - 1, first_string_list, second_string_ls)
        second_string_ls.append(w[j - 1])
        first_string_list.append('-')
    elif backtrack[i][j] == 'C':
        output_lcs(backtrack, v, w, i - 1, j - 1, first_string_list, second_string_ls)
        first_string_list.append(v[i - 1])
        # if v[i-1] != w[j-1]: print('Smells fishy')
        second_string_ls.append(w[j - 1])


# dp_change(16810,
# list(map(int, '24,21,14,8,5,3,1'.split(','))))
sys.setrecursionlimit(10000)
file = open('data/global_alignment_data.txt')
lines = file.read().splitlines()
str1 = lines[0]
str2 = lines[1]

blosum = BLOSUM62('')
z, score = LCS_backtrack(str1, str2, 5, blosum)

sec_str_ls = []
first_str_ls = []
# if len(str1) > len(str2):
#     sec_str_ls.append('-' * (len(str1) - len(str2)))
# else:
#     first_str_ls.append('-' * (len(str2) - len(str1)))

backtrack = output_lcs(z, str1, str2, len(str1), len(str2), first_str_ls, sec_str_ls)

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
