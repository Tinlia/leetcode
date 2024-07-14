# Runtime 21ms | Beats 99.58% of submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        lst = []
        def go(n):
            if n:
                lst.append(n.val)
                go(n.left)
                go(n.right)
        go(root)
        return lst
