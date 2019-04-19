'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_num = max(nums)
        all_nums_till_max = range(0, max_num + 1)

        missingnum = sum(all_nums_till_max) - sum(nums)

        if missingnum == 0:
            if nums[0] != 0:
                return 0

            return max_num + 1
        else:
            return missingnum

if __name__=="__main__":
    obj=Solution()
    nums=[9,6,4,2,3,5,7,0,1]
    res=obj.missingNumber(nums)
    print(res)