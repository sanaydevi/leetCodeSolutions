'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Logic:
1.convert each time digit to digit list.
2.compute sum of squares of each digit.
3.check if it 1 or not and repeat the steps if necessary.
keep track of each number bcoz if you get back the same number it is cyclic and solution
doesn't exist.
'''


class Solutuion:
    def __init__(self):
        self.visited = []        # to keep track of all numbers.

    def convertToList(self, n):
        """

        :param n: int
        :return: list
        """
        n_string = str(n)
        digits_list = [int(i) for i in n_string]
        return digits_list

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n not in self.visited:
            self.visited.append(n)
            digits = self.convertToList(n)  # list of individual digits.
            sum_of_square = 0
            for digit in digits:
                sum_of_square += digit ** 2
            n = sum_of_square

            if sum_of_square == 1:
                return True

        return False     # if you get back n, which means it is cyclic and solu doesn't exist.


if __name__ == "__main__":
    obj = Solutuion()
    res = obj.isHappy(19)
    print(res)
