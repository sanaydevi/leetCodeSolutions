"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

Logic:
Right shift A atmost len(A) times and check if A==B.
because if A is rotated len(A) times, we'll get back original A.
"""


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        lenA = len(A)
        for i in range(lenA):
            if A == B:
                return True
            first_char = A[0]
            A = A[1:] + first_char

        return False
