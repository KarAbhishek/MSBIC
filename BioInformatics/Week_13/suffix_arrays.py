from operator import itemgetter


def suffix_arrays(strin):
    ls = []
    for i in range(len(strin)):
        ls.append(strin[i:])
    return [i[0] for i in sorted(enumerate(ls), key=itemgetter(1))]