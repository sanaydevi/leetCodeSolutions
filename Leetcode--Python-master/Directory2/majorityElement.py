'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 times. You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        threshold = num_len // 2

        # for very large inputs count only unique elements.
        nums_unique = list(set(nums))

        for i in nums_unique:
            if nums.count(i) > threshold:
                return i


if __name__ == "__main__":
    obj = Solution()
    nums = [3, 2, 3]
    print(obj.majorityElement(nums))

'''
test case:
[2,2,1,1,1,2,2]
[3,2,3]

'''
