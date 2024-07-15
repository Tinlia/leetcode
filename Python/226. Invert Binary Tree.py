# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(n):
            if n:
                hold = n.left
                n.left = n.right
                n.right = hold
                if n.left:
                    invert(n.left)
                if n.right:
                    invert(n.right)
        
        invert(root)
        return root
