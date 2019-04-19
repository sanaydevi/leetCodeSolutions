import collections


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        C = collections.Counter
        print(C(nums1) & C(nums2))
        target = list((C(nums1) & C(nums2)).elements())
        return target


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2]
    obj = Solution()
    res = obj.intersection(nums1, nums2)
    print(res)
