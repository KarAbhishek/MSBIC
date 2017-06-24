

def shared_kmers(k_mer_1, k_mer_2, ls, k):
    # first = set()
    # for i in range(len(kmer_1) - k + 1):
    #     first.add(kmer_1[i:i + k])
    # second = set()
    # for i in range(len(kmer_2) - k + 1):
    #     first.add(kmer_1[i:i + k])
    #     # first.add(findRverseComplement(kmer_1[i:i + k]))
    # return first | second
    first = {}
    for i in range(len(k_mer_1) - k + 1):
        k_mer = k_mer_1[i: i + k]
        if k_mer in first:
            first[k_mer].append(i)
        else:
            first[k_mer] = [i]
    for i in range(len(k_mer_2) - k + 1):
        k_mer = k_mer_2[i: i + k]
        k_mer = k_mer if k_mer in first else findRverseComplement(k_mer)
        if k_mer in first:
            for j in first[k_mer]:
                ls.append((j, i))



def findRverseComplement(text):
    retVar =''
    for i in text[::-1]:
        if i == 'A':
            retVar+='T'
        if i == 'G':
            retVar+='C'
        if i == 'C':
            retVar+='G'
        if i == 'T':
            retVar+='A'
    return retVar

if __name__ == '__main__':
    ls = []
    shared_kmers('', '', ls, 17)
    string = ''
    for i in ls:
        string += str(i) + '\n'

    file=open('sample_ot.txt', 'w+')
    file.write(string)
    file.close()