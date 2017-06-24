def bwt(strin):
    ls = []
    for idx in range(len(strin)):
        ls.append(strin[idx:] + strin[:idx])
    ret = []
    for elem in sorted(ls):
        ret.append(elem[-1])
    return (''.join(ret))


if __name__ == '__main__':
    print(bwt('CACTTAAAGT$'))