'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

Logic:
CDA -> index of c=2,D=1,A=0 so 3*26^2+ 4*26^1 + 1.
'''


class Solution(object):
    def __init__(self):
        self.number_to_alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                                 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                                 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet_list = list(s)
        alphabet_list.reverse() # bcoz we start from right to left.
        final_num = 0
        for index, value in enumerate(alphabet_list):
            if index == 0:
                final_num += self.number_to_alphabet[value]
            else:
                final_num += (26 ** index) * self.number_to_alphabet[value]

        return final_num


if __name__ == "__main__":
    obj = Solution()
    print(obj.titleToNumber("ZY"))
