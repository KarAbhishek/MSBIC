def de_brujin_graph(k, text):
    prefix_hm = {}
    for i in range(len(text)-k+1):
        k_mer = text[i:i+k]
        prefix = k_mer[:-1]
        suffix = k_mer[1:]
        prefix_hm[prefix] = suffix
    ret_hm = {}
    for i in prefix_hm:
        if prefix_hm[i] in prefix_hm:
            add_value_to_key(ret_hm, i, prefix_hm[prefix_hm[i]])
    return ret_hm

def de_brujin_graph(k, text):
    prefix_hm = {}
    for i in range(len(text)-k+1):
        k_mer = text[i:i + k]
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


print(arrow_format(de_brujin_graph(12, '')))