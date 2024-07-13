# Runtime: 33ms | Beats 72.09% of submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node):
            if node:
                return [node.val] + traverse(node.left) + traverse(node.right)
            else:
                return [None]
        return traverse(p) == traverse(q)
