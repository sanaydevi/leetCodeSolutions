"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].


"""


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        is_neg = False

        if num < 0:
            is_neg = True
            num = abs(num)

        final_str = ''
        while num >= 7:
            final_str += str(num % 7)
            num = num // 7
        final_str += str(num)

        final_str = final_str[::-1]

        if is_neg:
            final_str = '-' + final_str

        print(final_str)


if __name__ == "__main__":
    ob = Solution()
    ob.convertToBase7(-7)
