"""
Write a function that will return a list of all positive divisors of a given number n.
"""
from math import sqrt


class Solution(object):
    def findDivisors(self, n):
        divisors = [1]

        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                divisors.extend([i, n // i])
        divisors.append(n)
        divisors = sorted(list(set(divisors)))
        print(divisors)


if __name__ == "__main__":
    ob = Solution()
    ob.findDivisors(28)
