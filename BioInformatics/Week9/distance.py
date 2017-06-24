class Distance:
    def __init__(self):
        file = open('dist_leaves.txt')
        input = file.read().splitlines()
        self.hm = []
        for single_line in input[1:]:
            self.unformat_to_hm(single_line)

        # input = map(self.unformat_to_hm, input)

    def distance(self, start_point=None, hm=None):
        if hm is None:
            hm = self.hm
        if not hm:
            return True

        print(hm)
        outgoing_edges = [i[0] for i in hm]
        for idx, i in enumerate(hm):
            start_point = i[0]
            if i[1][0] in outgoing_edges:
                res = self.distance(start_point, hm[:idx]+hm[idx+1:])
                if res:
                    return res
        return False

    # def recurser(self, path):
    #     if path
    #     self.recurser(path)

    def unformat_to_hm(self, single_line):
        hm_key, hm_unformatted_val = single_line.split('->')
        hm_val = hm_unformatted_val.split(':')
        self.hm.append((int(hm_key), list(map(int, hm_val))))


if __name__ == '__main__':
    dist = Distance()
    print(dist.distance())

