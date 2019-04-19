class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        final_list = []
        flag = False
        for i in nums1:
            flag = False
            index2 = nums2.index(i)
            for j in range(index2, len(nums2)):
                if nums2[j] > i:
                    final_list.append(nums2[j])
                    flag = True
                    break

            if flag:
                continue
            else:
                final_list.append(-1)

        print(final_list)


if __name__ == "__main__":
    ob = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    ob.nextGreaterElement(nums1, nums2)
