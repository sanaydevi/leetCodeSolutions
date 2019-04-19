"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Logic:
keep removing 0 or 10, 11 from the list.
when list len becomes <=2, chances are [1,0] or [0,0]. Remove duplicates.
finally if len =1 ret true , if not false.
"""


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        while len(bits) > 2:
            # print(bits)
            if bits[0] == 0:
                bits = bits[1:]
            elif bits[0] == 1:
                bits = bits[2:]

        print(bits)
        bits = list(set(bits))
        if len(bits) == 1:
            return True
        else:
            return False
