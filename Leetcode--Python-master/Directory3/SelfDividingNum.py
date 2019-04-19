"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

logic: first generate the list and use built in filter to check the numbers.

"""


class Solution:
    def check(self, x):
        """

        :param x: int
        :return: bool
        """
        if 0 < x < 10:
            return True
        else:
            digits = list(str(x))       # generate individual digit list.
            for i in digits:            # check.
                if int(i) == 0 or x % int(i) != 0:
                    return False
            return True

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        num_list = list(range(left, right + 1))
        dividing_num = list(filter(self.check, num_list))
        # print(dividing_num)
        return dividing_num
