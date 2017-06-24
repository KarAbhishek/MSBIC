class IdGen:
    id_var = 0

    @staticmethod
    def get_id():
        temp = IdGen.id_var
        IdGen.id_var += 1
        return temp

def ModifiedSuffixTrieConstruction(Text):
    Trie = [{}]  # a graph consisting of a single node root
    for i in range(len(Text)):
        currentNode = 0
        for j in range(i, len(Text)+1):
            currentSymbol = Text[j]
            if currentNode in Trie and Trie[currentNode][0] == currentSymbol:
                currentNode = Trie[currentNode][1]
            else:
                newNode = IdGen.get_id()
                Trie.append({currentNode: [currentSymbol, newNode, j]})
                # add an edge newEdge connecting currentNode to newNode in Trie
                # Symbol(newEdge) = currentSymbol
                # Position(newEdge) = j
                currentNode = newNode
        if currentNode not in Trie:
            currentNode[2] = i
    return Trie


def yield_suffixes(strin):
    for i in range(len(strin)):
        yield strin[i:]

if __name__ == '__main__':
    inp = yield_suffixes('CCACGACGTAGACCGTTGCTAAAAGACCCATCTCCCCTAAACGTAAACGACAAGACGATGAACACCTTGCGCTACTTAATATGCTGCGCAGCTGGCCGGGACCAGGGCCGGGATGCTAAAGCGGCTAACCCATAAGCATACTGTCCACCCGCAGTAATGCAAGTATCTCGCCTATGGCGCTCGACCTAGCGGCATCCGATAGATGGACAGCGCCGACTAAAGTCTCAGTCCGTAGTTTCAAGGTACTACACGTCCTTCGCAAGATGGGGGACCTTCGTCGGAACCACGCAGCTTATGACACTTATCGGCAACAAGGCGGTCAGACATTGACCACCGCATCGAACCGGAAGGAGCCGAAGTAGGGGCGAGCCGCAATATATCTACACGAGCTCGATGTGTGTCTATTCCGTCGTAATACAGTGACGGGTAGTGCTGGATCAAAAGAATCAAGGTGCGAACATGTCCAGCAGCCAACGGGGCAAGAGTAGGTGAGGAGAGCATGGCAGTACAATAGAGACGGTGCCACTGCCACGACGTGTGTAGTCCACCTTTGCAGATGTTTATAATTGTATTAGGCAAGTCGTAAGGTCGTTCTAAAAAATGACCCTCGGTCTACAGCCGCGATTATAATTGAGTAACTCACTAACATGTGCAAACAAATAAGTATCATCAACAGAGTCAGTATGGCTCCTTGATAGAGCACTGAATAAGATCGGTCCTGGGGCAAACGATCGAAAAGCTCGTATATGAACAATTTTTACCAGTTGTTTCTACAGCATTTGTAACCGTACGACTCTGATCAGAGCGATTACAGGTAGCGACACCAAACAGGAAGTGATCGTCTAAGCTCCCCCCAACACAGTAGCGACCAACTGCAGACGCGCTCCTCGAGCCACCAACCCTTAACCAAGAAGTGC$')
    for i in inp:
        ModifiedSuffixTrieConstruction(i)