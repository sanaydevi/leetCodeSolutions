'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_zeros = nums.count(0)
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                i = 0
                continue
            i += 1

        for i in range(count_zeros):
            nums.append(0)

        print(nums)


if __name__ == "__main__":
    obj = Solution()
    res = obj.moveZeroes([0, 1, 0, 3, 12])
    print(res)
