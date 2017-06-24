def de_brujin_graph(list_of_k_mers):
    prefix_hm = {}
    for k_mer in list_of_k_mers:
        prefix = k_mer[:-1]
        suffix = k_mer[1:]
        add_value_to_key(prefix_hm, prefix, suffix)
    return prefix_hm

def add_value_to_key(hm, key, value):
    try:
        hm[key] += [value]
    except:
        hm[key] = [value]

def arrow_format(hm):
    return '\n'.join(['%s -> %s' % (key, ','.join(value)) for (key, value) in hm.items()])


list_of_k_mers = []
print(arrow_format(de_brujin_graph(list_of_k_mers)))