"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""


class Solutuion:
    def threeclosestsum(self, nums, target):
        nums.sort()
        result = sum(nums[0:3])

        for i in range(0, len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == target:
                    return cur_sum

                # update the global result.
                if abs(cur_sum - target) < abs(result - target):
                    result = cur_sum

                # based on cur_sum adjust the pointers.
                if cur_sum < target:
                    j += 1
                else:
                    k -= 1
        return result


if __name__ == "__main__":
    ob = Solutuion()
    nums = [-1, 1, 2, -4]
    target = 1
    res = ob.threeclosestsum(nums, target)
    print(res)
