# Runtime: 229ms | Beat 78.48% of submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Recursively traverse BT, returning minimum depth +1
        if root is None: return 0
        def go(n):
            if n.left is None and n.right is None:
                return 1
            else:
                if n.left is None: return go(n.right) + 1
                elif n.right is None: return go(n.left) + 1
                else: return min(go(n.left), go(n.right)) + 1
        return go(root)
