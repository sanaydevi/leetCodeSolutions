'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Logic:
say a[1,1,2,3,3,4,4] now, sum[1,1,2,3,3,4,4] = 18 , sum[1,2,3,4] = 10*2 = 20  , 20-18 =2 .
sum of a gives total sum.
Remove duplicates and sum*2 gives all elements sum with elements repeated twice.
difference gives that one element that is left out.
'''


class Solution:
    def __init__(self):
        self.buffer = {}

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)) * 2) - sum(nums)


if __name__ == "__main__":
    obj = Solution()
    nums = [2, 2, 1]
    print(obj.singleNumber(nums))

'''
test cases:
[2,2,1]
[4,1,2,1,2]
'''
