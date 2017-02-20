def LCS_backtrack(v, w):
    s = [[-1 for i in range(len(w)+1)] for j in range(len(v)+1)]
    backtrack = [['N' for i in range(len(w)+1)] for j in range(len(v)+1)]
    for i in range(len(v)+1):
        s[i][0] = 0
    for j in range(len(w)+1):
        s[0][j] = 0
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + 1 if v[i-1] == w[j-1] else 0)
            if s[i][j] == s[i-1][j]:
                backtrack[i][j] = 'D'
            elif s[i][j] == s[i][j-1]:
                backtrack[i][j] = 'R'
            elif s[i][j] == s[i-1][j-1]+1 and v[i-1] == w[j-1]:
                backtrack[i][j] = 'C'
    return backtrack

def output_lcs(backtrack, v, i, j):
    if i==0 and j==0:
        return
    if backtrack[i][j] == 'D':
        output_lcs(backtrack, v, i-1, j)
    elif backtrack[i][j] == 'R':
        output_lcs(backtrack, v, i, j-1)
    elif backtrack[i][j] == 'C':
        output_lcs(backtrack, v, i-1, j-1)
        print(v[i-1], end='')

def unformat_to_list(lines):
    hm = {}
    for line in lines:
        linees = line.split(':')
        weights = linees[1]
        src, dest = linees[0].split('->')
        print(src, dest, weights)
        if int(src) in hm:
            hm[int(src)].append([int(dest), int(weights)])
        else:
            hm[int(src)] = [[int(dest), int(weights)]]
    return hm

def link_till_end(hm, source, end, maxTally, currTally):
    # if source hm:
    #     print('Failed')
    # el
    currTally[1].append(source)
    if source == end:
        print('Success')
        if maxTally and maxTally[0]<currTally[0]:
            maxTally[0], maxTally[1] = currTally[0], currTally[1]

        elif not maxTally:
            maxTally.append(currTally[0])
            maxTally.append(currTally[1])
        #currTally[0]
        #currTally[1]
        print(maxTally[0])
        print('->'.join(map(str, maxTally[1])))
        #del currTally[-1]
        return
    elif source not in hm:
        return
    else:
        for i in hm[source]:
            currTally[0] += i[1]
            link_till_end(hm, i[0], end, maxTally, currTally)
            currTally[0] -= i[1]
            del currTally[1][-1]


file = open('DAG')
lines = file.read().splitlines()
source_node = int(lines[0])
end_node = int(lines[1])
hm = unformat_to_list(lines[2:])
link_till_end(hm, source_node, end_node, [], [0,[]])

