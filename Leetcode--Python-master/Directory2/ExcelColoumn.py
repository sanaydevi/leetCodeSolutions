'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''


class Solution:
    def __init__(self):
        self.alphabetToNumber = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
                                 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R',
                                 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
        self.resultlist = []

    def getString(self, l):
        temp = ""
        final = "".join(temp + self.alphabetToNumber[i] for i in l)
        print(final)
        return final

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n > 26 and n % 26 == 0:
            quotient = n // 26
            self.resultlist.append(quotient - 1)
            self.resultlist.append(0)
            return self.getString(self.resultlist)

        while n > 26:
            if n == 26:
                break
            remainder = n % 26
            self.resultlist.append(remainder)
            n = n // 26

        self.resultlist.append(n)
        self.resultlist.reverse()
        if self.resultlist[-1] == 0:
            self.resultlist[-2] = self.resultlist[-2] - 1

        return self.getString(self.resultlist)


if __name__ == "__main__":
    obj = Solution()
    obj.convertToTitle(701)
