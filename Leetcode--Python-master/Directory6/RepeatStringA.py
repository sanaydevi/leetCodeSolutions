class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        C = ""
        for i in range(len(B) // len(A) + 3):
            if B in C:
                return i
            C += A
        return -1



if __name__ == "__main__":
    a = "bb"
    b = "bbbbbbb"
    ob = Solution()
    ob.repeatedStringMatch(a,b)