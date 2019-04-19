"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder_read(self, p, numlist):
        if p:
            self.inorder_read(p.left, numlist)
            numlist.append(p.val)
            self.inorder_read(p.right, numlist)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        values = []
        self.inorder_read(root, values)
        # print(values)

        d = []
        for i in values:
            if i not in d:
                d.append(k - i)
            else:
                return True
        return False
