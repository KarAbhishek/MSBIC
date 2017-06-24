import sys

def affine_directors_cut(v, w, gap_open_penalty, gap_extend_penalty):
    lower_d = [[0 for x in range(len(w)+1)] for y in range(len(v)+1)]
    middle_d = [[0 for x in range(len(w) + 1)] for y in range(len(v) + 1)]
    upper_d = [[0 for x in range(len(w) + 1)] for y in range(len(v) + 1)]
    lower_backtrack = [['N' for x in range(len(w) + 1)] for y in range(len(v) + 1)]
    middle_backtrack = [['N' for x in range(len(w) + 1)] for y in range(len(v) + 1)]
    upper_backtrack = [['N' for x in range(len(w) + 1)] for y in range(len(v) + 1)]

    for i in range(1, len(v)+1):
        lower_d[i][0] = -gap_open_penalty - gap_extend_penalty * (i-1)
        middle_d[i][0] = -gap_open_penalty - gap_extend_penalty * (i - 1)
        upper_d[i][0] = -gap_open_penalty - gap_extend_penalty * (i - 1)

    for j in range(1, len(w)+1):
        lower_d[0][j] = sys.int#-gap_open_penalty - gap_extend_penalty * (j-1)
        middle_d[0][j] = -gap_open_penalty - gap_extend_penalty * (j - 1)
        upper_d[0][j] = -gap_open_penalty - gap_extend_penalty * (j - 1)

