def trie_construction(patterns):
    edges = []
    for pattern in patterns:
        create_tree(pattern, edges)


def create_tree(pattern, edges):
    for char in pattern:
        # if Completely New Edge:
        #    edges with [two new ids:char]
        # elif
        pass


def find_leftmost_1_binary(self, n):
    ret = 1
    while n != 0:
        if n & 1 == 1:
            ret <<= 1
        n >>= 1

    return ret

if __name__ == '__main__':
    file = open('input.txt')
    patterns_out = file.read().splitlines()
    out = trie_construction(patterns_out)
    print(out)
