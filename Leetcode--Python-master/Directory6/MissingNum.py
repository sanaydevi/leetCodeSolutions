"""
Given an array find the missing number.
"""
from collections import Counter


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_number = len(nums)
        all_nums = list(range(1, max_number + 1))

        nums_unique = list(set(nums))
        repeated_num = Counter(nums) - Counter(nums_unique)
        missing_num = Counter(all_nums) - Counter(nums_unique)

        repeated_num = list(repeated_num.elements())[0]
        missing_num = list(missing_num.elements())[0]
        print(repeated_num, missing_num)
        # return [repeated_num, missing_num]


if __name__ == "__main__":
    ob = Solution()
    n = [2, 2]
    ob.findErrorNums(n)

"""
Test case: 
[1,1]
[2,2]
[1,2,2,4]

"""
