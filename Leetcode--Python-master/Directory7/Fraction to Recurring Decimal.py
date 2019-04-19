"""
Given a fraction, convert it to decimal.
"""
from collections import OrderedDict
from collections import Counter


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        quo, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(quo), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            quo, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(quo))

        idx = stack.index(remainder)
        result.insert(idx + 2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')


if __name__ == "__main__":
    ob = Solution()
    res = ob.fractionToDecimal(1, 3)
    print(res);
