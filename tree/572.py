#time complexity O(n)
#space complexity O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqual(self, p, q):
        if (p and not q) or (not p and q):
            return False

        if p and q:
            if p.val != q.val:
                return False
            return self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right)

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if self.isEqual(root, subRoot):
            return True

        if not root:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        