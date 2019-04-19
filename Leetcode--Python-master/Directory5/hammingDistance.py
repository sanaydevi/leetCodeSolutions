"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        and_result = x & y
        or_result = x | y

        and_result = str(bin(and_result)[2:])
        or_result = str(bin(or_result)[2:])

        pos_diff = or_result.count("1") - and_result.count("1")
        print(pos_diff)


if __name__ == "__main__":
    ob = Solution()
    ob.hammingDistance(1, 5)
