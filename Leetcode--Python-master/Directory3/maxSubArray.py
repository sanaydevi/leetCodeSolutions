'''
Problem: find maxSubArray.
solution: kadane's algorithm
'''


class Solution:

    def __init__(self):
        self.maxSoFar = 0
        self.currentMax = 0

    def maxSubArray(self, nums):
        for i in nums:
            self.currentMax = max(self.currentMax + i, i)
            self.maxSoFar = max(self.currentMax, self.maxSoFar)

        print(self.maxSoFar)


if __name__ == "__main__":
    nums = [-2, -1, 2, -3, -4, -5]
    obj = Solution()
    obj.maxSubArray(nums)

'''
test cases
[2, -5, 6, -2, -3, 1, 5, -6]
[-2,-3,4,-1,-2,1,5,-3]
[2, 3, 4, 5, 7]
[2 -1 2 3 4 -5]
'''
