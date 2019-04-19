'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: [1,2,3,1], k = 3
Output: true
Example 2:

Input: [1,0,1,1], k = 1
Output: true
Example 3:

Input: [1,2,1], k = 0
Output: false

Logic:
use dictionary and checktime duplicate num found, check for condition.
'''


class Solution(object):

    def checkdiff(self, lst, k):
        for i in range(0, len(lst) - 1):
            if abs(lst[i] - lst[i + 1]) == k:
                return True
        return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}

        for i, v in enumerate(nums):
            if v not in d:
                d[v] = [i]
            else:
                d[v].append(i)
                if self.checkdiff(d[v], k):
                    return True
        return False


if __name__ == "__main__":
    nums = [1, 2, 1]
    obj = Solution()
    res = obj.containsNearbyDuplicate(nums, 0)
    print(res)
