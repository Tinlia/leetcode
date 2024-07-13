# Runtime: 29ms | Beats89.76% of submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        def traverse(n):
            if n:
                traverse(n.left)
                inorder.append(n.val)
                traverse(n.right)
        
        traverse(root)
        return inorder
            
