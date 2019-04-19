"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

from collections import Counter


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_num = len(nums)
        missing_nums = Counter(list(range(1, max_num + 1))) - Counter(nums)
        print(list(missing_nums.elements()))
        return missing_nums


if __name__ == "__main__":
    ob = Solution()
    lst = [4, 3, 2, 7, 8, 2, 3, 1]
    ob.findDisappearedNumbers(lst)

"""
test cases:
[4,3,2,7,8,2,3,1]
[1,1]

"""
