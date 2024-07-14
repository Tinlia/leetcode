# Runtime 38ms | Beats 91.08% of submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getheight(n):
            if n is None: return 0

            leftH = getheight(n.left)
            if leftH == -1: return -1

            rightH = getheight(n.right)
            if rightH == -1: return -1

            if abs(leftH - rightH) > 1: return -1

            return max(leftH, rightH) + 1

        return getheight(root) != -1
