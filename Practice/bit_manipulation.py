class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # mult = 1.0

        left_most = self.find_leftmost_1_binary(n)
        # print(left_most)
        truncated_n = (n & (left_most - 1))
        print(truncated_n)
        counter = left_most
        place_holder = x
        while counter != 0:
            if truncated_n & counter > 0:
                place_holder = place_holder * place_holder * n
                print('/Here')
            else:
                place_holder = place_holder * place_holder
                print('Here')
            counter >>= 1
        return place_holder
        # for i in range(n):
        #     mult *= x
        # return mult

    def find_leftmost_1_binary(self, n):
        ret = 1
        # print(n)
        # print(bin(n))
        while n != 0:
            # print('n', n)
            # if n & 1 == 1:
            ret <<= 1
            n >>= 1

        # print(ret >> 1)
        return ret >> 1

print(Solution().myPow(12, 9))