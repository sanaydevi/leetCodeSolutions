from math import sqrt


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        d = {}
        for i in range(1, int(sqrt(c)) + 1):
            d[i * i] = None
            if c - i * i in d:
                return True
        return False


if __name__ == "__main__":
    ob = Solution()
    res = ob.judgeSquareSum(6)
    print(res)
