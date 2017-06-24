class Solution(object):
    def is_palindrome(self, st):
        start = 0
        end = len(st) - 1
        while start < end:
            if st[start] != st[end]:
                return False
            start += 1
            end -= 1
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        for siz in range(n, 0, -1):
            for idx in range(n - siz + 1):
                subst = s[idx:idx + siz]
                print(subst)
                if self.is_palindrome(subst):
                    return subst

        return None


print(Solution().longestPalindrome('babad'))
# print(Solution().is_palindrome('badab'))