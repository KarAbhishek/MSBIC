def BLOSUM62(sl = None):
    file = open('data/BLOSUM62.txt')
    lines = file.read().splitlines()
    matrix_rows = [line[3:].split() for line in lines]
    blasum_map = {i:idx for idx, i in enumerate(matrix_rows[0])}
    if sl is not None:
        ret = blasum_map, [list(map(int, single)) for single in matrix_rows[1:]]
    else:
        import pandas as pd
        ret = pd.DataFrame([list(map(int, single)) for single in matrix_rows[1:]], index=list(blasum_map.keys()), columns = list(blasum_map.keys()))
    return ret


def global_alignment(protein_string_1, protein_string_2, indel_penalty=1, mismatch_penalty=1):
    s = [[0 for x in range(len(protein_string_1)+1)] for y in range(len(protein_string_2)+1)]
    for i in range(1, len(protein_string_2)+1):
        #s.append([0])
        for j in range(1, len(protein_string_1)+1):
            s[i][j] = max([s[i-1][j], s[i][j-1], s[i-1][j-1]+1 if protein_string_1[j-1] == protein_string_2[i-1] else s[i-1][j-1]-mismatch_penalty])
    import numpy as np
    return np.array(s)









def helper():
    if protein_string_1 is None:
        return
    if protein_string_1[0] == protein_string_2[0]:
        return


if __name__ == '__main__':
    blasum_mapping, blasum_matrix = BLOSUM62('')
    file = open('data/global_alignment_data.txt')
    lines = file.read().splitlines()
    protein_string_1 = lines[0]
    protein_string_2 = lines[1]
    print (global_alignment(protein_string_1, protein_string_2))
