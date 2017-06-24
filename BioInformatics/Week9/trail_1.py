def distance_matrix(n, hm):
    dist_matrix = [[0 for y in range(n)] for x in range(n)]
    for i in hm:
        for j in hm:
            if i == j:
                continue
            else:
                #if dist_matrix[i][j] == 0:
                cap = hm.copy()
                find_dist(i, j, cap)
                #print(cap)
                    # dist_matrix[i][j] = dist_matrix[j][i] = find_dist(i, j, hm.copy())


def find_distance(source, sink, hm):
    if not hm:
        return
    if source == sink:
        # Found path
        print("Found")
        return
        pass
    elif source in hm:
        all_sources = hm[source]
        for new_source in all_sources:
            find_distance(new_source[0], sink, hm.copy())
        del hm[source]
    else:
        return
        # Couldnt find path
        print("Not Found")
        pass
    return 1

def find_dist(source, sink, hm, capture=[[]]):
    if source == sink:
        ## Found
        # capture[-1].append([source])
        # capture.append([])
        print(source)
        return
    if not hm or source not in hm:
        ## Not Found
        return

    for dest_idx, dest in enumerate(hm[source]):
        path = hm.copy()
        new_source = dest[0]
        # capture[-1].append([source, dest])
        capture[-1].append(source, dest, end='')
        # remove used indices
        remove(path, source, dest_idx)
        find_dist(new_source, sink, path)



def remove(hm, source, dest_idx):
    del hm[source][dest_idx]
    if not hm[source]:
        del hm[source]


# def itera(hm):
#     key_list = list(hm.keys)
#     for start_idx, start in enumerate(key_list):
#         for j in key_list[start_idx:]:


def add_to_hm(hm, key, val):
    try:
        hm[key].append(val)
    except:
        hm[key] = [val]


file = open('dist_leaves.txt')
input = file.read().splitlines()
hm = {}
for single_line in input[1:]:
    hm_key, hm_unformatted_val = single_line.split('->')
    hm_val = hm_unformatted_val.split(':')
    print(hm_key, list(map(int, hm_val)))
    add_to_hm(hm, int(hm_key), tuple(map(int, hm_val)))
distance_matrix(int(input[0]), hm)