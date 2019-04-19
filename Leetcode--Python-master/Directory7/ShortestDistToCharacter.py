"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index_listof_C = [i for i, v in enumerate(S) if v == C]
        result_list = []
        for i in range(len(S)):
            temp = [abs(i - j) for j in index_listof_C]
            result_list.append(min(temp))

        # print(result_list)
        return result_list
