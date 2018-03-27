from TreeNode import *


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_deep = self.maxDepth(root.left)
        right_deep = self.maxDepth(root.right)

        return max(left_deep, right_deep) + 1
