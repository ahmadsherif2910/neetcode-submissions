# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not sub: return True
        if not root: return False
        if self.isSame(root,sub): return True
        return self.isSubtree(root.left,sub) or self.isSubtree(root.right,sub)

    def isSame(self,root,sub):
        if not root and not sub: return True
        if not root or not sub: return False

        return (root.val == sub.val) and self.isSame(root.left,sub.left) and self.isSame(root.right,sub.right)