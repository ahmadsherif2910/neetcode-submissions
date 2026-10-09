# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)       # 1. Traverse left
            result.append(node.val)  # 2. Visit root
            inorder(node.right)

        inorder(root)
        return result[k-1]