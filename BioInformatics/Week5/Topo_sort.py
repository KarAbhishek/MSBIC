def topo_sort(hm):
    while True:
        key = indegree_is_zero(hm)
        del hm[key]

def get_input(inpt):
    inputs = inpt.split(' -> ')
    return {i[0]:i[1] for i in inputs}

def unformat_to_hm(ls):
    return {input.split(' -> ')[0]: input.split(' -> ')[1].split(',') for input in ls}

file = open('topo_sort_data')
lines = file.read().splitlines()
print(unformat_to_hm(lines))