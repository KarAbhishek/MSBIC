import sys
def link_till_end(hm, source, end, maxTally, currTally):
    # if source hm:
    #     print('Failed')
    # el
    currTally[1].append(source)
    if source == end:
        # print('Success')
        if maxTally and maxTally[0]<currTally[0]:
            maxTally[0], maxTally[1] = currTally[0], currTally[1]

        elif not maxTally:
            maxTally.append(currTally[0])
            maxTally.append(currTally[1])
        print(maxTally[0])
        print('->'.join(map(str, maxTally[1])))
        return
    elif source not in hm:
        return
    else:
        for i in hm[source]:
            currTally[0] += i[1]
            link_till_end(hm, i[0], end, maxTally, currTally)
            currTally[0] -= i[1]
            del currTally[1][-1]

def unformat_to_list(lines):
    hm = {}
    for line in lines:
        linees = line.split(':')
        weights = linees[1]
        src, dest = linees[0].split('->')
        # print(src, dest, weights)
        if int(src) in hm:
            hm[int(src)].append([int(dest), int(weights)])
        else:
            hm[int(src)] = [[int(dest), int(weights)]]
    return hm

def distance_matrix(n, hm):
    dist_matrix = [[0 for y in range(n)] for x in range(n)]
    for i in hm:
        for j in hm:
            if i == j:
                continue
            else:
                #if dist_matrix[i][j] == 0:
                cap = hm.copy()
                link_till_end(i, j, cap)
                #print(cap)
                    # dist_matrix[i][j] = dist_matrix[j][i] = find_dist(i, j, hm.copy())

def dist_matrix(n, hm):
    leaves = [i for i in hm if len(hm[i]) == 1]
    dist_mat = [[0 for y in range(n)] for x in range(n)]
    for idx_i, i in enumerate(leaves):
        for idx_j, j in enumerate(leaves):
            if idx_i == idx_j:
                continue
            dist_mat[idx_i][idx_j] = link_till_end(hm, i, j, [], [0,[]])
    print(dist_mat)

sys.setrecursionlimit(10000)
file = open('dist_leaves.txt')
lines = file.read().splitlines()
# source_node = 0
# end_node = 4
hm = unformat_to_list(lines[1:])
#link_till_end(hm, source_node, end_node, [], [0,[]])
dist_matrix(int(lines[0]), hm.copy())