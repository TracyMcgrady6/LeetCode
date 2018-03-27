from TreeNode import *


class Solution:
    def mergeTrees(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        ans = TreeNode((t1.data if t1 else 0) + (t2.data if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)

        return ans