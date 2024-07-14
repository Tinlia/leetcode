# Runtime: 38ms | Beats 76.06% of submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False

        def go(n, sum):
            if n is None: return False
            if sum + n.val == targetSum and n.left is None and n.right is None: return True

            return go(n.left, sum+n.val) or go(n.right, sum+n.val)

        return go(root, 0)
