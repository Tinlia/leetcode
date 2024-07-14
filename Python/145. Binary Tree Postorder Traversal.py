# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        lst = []
        def go(n):
            if n:
                go(n.left)
                go(n.right)
                lst.append(n.val)
        go(root)
        return lst
