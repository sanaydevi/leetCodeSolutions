'''
Array containing integers is given. Do a plus one to it and return the array list.
[1,2,3] is 123. Return 124=>[1,2,4].

Logic:
use python built in reduce function to convert given string list to int.
Again convert back the number after +1 to string list and return it.
'''
from functools import  reduce


class Solution:
    def plusOne(self, digits):
        """

        :param digits: int list
        :return: int list
        """
        num = reduce(lambda a, b: a * 10 + b, digits)
        num = num+1

        res = []
        while num != 0:
            res.append(num % 10)
            num = num // 10
        res.reverse()
        return res


if __name__=="__main__":
    obj = Solution()
    print(obj.plusOne([1, 2, 3]))
