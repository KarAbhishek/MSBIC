class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hm = {}
        self.ls = []
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print('GET', key)
        try:
            # print('Before', self.ls, self.hm)
            tmp = self.ls.pop(self.hm[key][1])
            self.ls.append(tmp)
            self.hm[key][1] = len(self.ls) - 1
            # print('After', self.ls, self.hm)
            return self.hm[key][0]
        except KeyError:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print('PUT', key, value)
        if self.capacity == len(self.ls):
            # print(self.ls, self.hm)
            del self.hm[self.ls.pop(0)]
            # print('After', self.ls, self.hm)

        if key not in self.hm:
            self.ls.append(key)
            self.hm[key] = value, len(self.ls) - 1


if __name__ == '__main__':
    substrates = ["LRUCache","get","put","get","put","put","get","get"]
    inputs = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
    for idx in range(len(substrates)):
        if substrates[idx] == "LRUCache":
            obj = LRUCache(inputs[idx][0])
        elif substrates[idx] == "get":
            param_1 = obj.get(inputs[idx][0])
            print(param_1)
        elif substrates[idx] == "put":
            obj.put(inputs[idx][0], inputs[idx][1])
