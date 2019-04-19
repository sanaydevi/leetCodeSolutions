'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictValues = Counter(s).values()
        dictValues = sorted(dictValues)
        dictValues.reverse()

        palindrome_len = 0
        for i in dictValues:
            if i % 2 == 0:
                palindrome_len += i
            elif i == 1:
                palindrome_len += i
                break

        print(palindrome_len)
        return palindrome_len


if __name__ == "__main__":
    s = "abccccdd"
    obj = Solution()
    obj.longestPalindrome(s)
