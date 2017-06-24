class motif_enumeration():
    def hamming_distance(str1, str2):
        count = 0
        for idx, elem in enumerate(str1):
            if str2[idx] != elem:
                count += 1
        return count

    def neighbours(self, pattern, d):
        if d == 0:
            return pattern
        if len(pattern) == 1:
            return {'A', 'G', 'C', 'T'}
        neighbourhood = set()
        for i in self.neighbours(pattern[1:], d):
            if self.hamming_distance(pattern[1:], i) < d:
                for nucleotide in 'AGCT':
                    neighbourhood = neighbourhood.union([nucleotide + i])
            else:
                neighbourhood = neighbourhood.union([pattern[0] + i])
        return neighbourhood

    def immediate_neighbors(pattern_compl):

        return

    def iter_neighbours(self, pattern, d):
        neighbourhood = set([pattern])
        for j in range(1, d+1):
            for pattern_compl in neighbourhood:
                neighbourhood.union(self.immediate_neighbors(pattern_compl))

        return neighbourhood

    def containedIn(self, dna, pat, d):
        for neigh_pat in self.neighbours(pat, d):
            if neigh_pat in dna:
                return True
        return False

    def motif_enum1(self, dna, k, d):
        patterns = set()
        for i in range(len(dna)-k+1):
            pattern = dna[:i]
            for pat_neighbor in self.neighbours(pattern, d):
                if self.containedIn(dna, pat_neighbor, d):
                    patterns.add(pat_neighbor)
        return patterns


    def contains_this(self, rest_of_dna_strings, neighbour_string, k, d):
        flagger = [False for i in range(len(rest_of_dna_strings))]
        for dna_enum in range(len(rest_of_dna_strings)):
            single_dna_string = rest_of_dna_strings[dna_enum]
            for i in range(len(single_dna_string)-k+1):
                k_mer_pattern = single_dna_string[i:i+k]
                if self.hamming_distance(neighbour_string, k_mer_pattern) <= d:
                    flagger[dna_enum] = True
                    if False not in flagger:
                        return True
        return False


    def motif_enum(self, dna, k, d):
        pattern_set = set()
        for i in range(len(dna[0])-k+1):
            pattern = dna[0][i:i+k]
            for neighbor in self.neighbours(pattern, d):
                if self.contains_this(dna[1:], neighbor, k, d):
                    pattern_set.add(neighbor)

        return pattern_set

    if __name__ == '__main__':
        dna = ['TGGTACCAGCCTTGCCGCCATACCA',
    'CGACACTTATCCCGGGCTTTTGGTC',
    'CTGGCAGGTCAGTTATCCCTCGTCA',
    'CGACACCCTGACAGGCCACATTTCC',
    'CGCCATTCGGGGTAGGGCGAAGCTT',
    'CGCCAGACGATCGTTATTGACGATA']
        motif_e = motif_enum(dna, 5, 1)
        print(' '.join(motif_e))
