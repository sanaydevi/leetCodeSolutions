'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i in range(k):
            last_element = nums.pop()
            nums.insert(0, last_element)

        print(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    obj = Solution()
    obj.rotate(nums, 3)
