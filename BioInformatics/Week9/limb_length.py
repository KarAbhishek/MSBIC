def limb_len(j, dist_mat):
    min_arr = []
    for i in dist_mat:
        for k in dist_mat:
            val = (dist_mat[i][j]+dist_mat[j][k]-dist_mat[i][k])//2
            if val>0:

                min_arr.append(val)

    return min(min_arr)

if __name__ == '__main__':
    file = open('limb.txt')
    lines = file.read().splitlines()
    N = lines[0]
    j = int(lines[1])
    splitter = lambda x:list(map(int, x.split(' ')))
    out = limb_len(j, list(map(splitter, lines[2:])))
    print(out)