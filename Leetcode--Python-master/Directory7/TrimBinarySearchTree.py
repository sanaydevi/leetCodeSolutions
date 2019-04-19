"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorder(self, p):
        if p:
            self.inorder(p.left)
            print(p.val)
            self.inorder(p.right)

    def levelorder(self, p):
        res, nodes = [], [p] if p else []
        while nodes:
            res.append([i.val for i in nodes])
            nodes = [x for node in nodes for x in (node.left, node.right) if x]
        print(res)
        return res

    def constructBinTree(self, values):
        head = None
        for i in values:
            cur = TreeNode(i)
            # print(cur.val)
            if not head:
                head = cur
            else:
                p = head
                while True:
                    if i > p.val:
                        if not p.right:
                            p.right = cur
                            break
                        else:
                            p = p.right
                    else:
                        if not p.left:
                            p.left = cur
                            break
                        else:
                            p = p.left

        # self.inorder(head)
        return head

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        values = self.levelorder(root)
        values = [j for i in values for j in i if L <= j <= R]
        # print(values)
        return self.constructBinTree(values)
