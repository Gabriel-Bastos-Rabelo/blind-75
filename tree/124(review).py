#time complexity O(n)
#space complexity O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxValue = float('-inf')
    def pathSum(self, root):
        if not root:
            return float('-inf')

        left = max(self.pathSum(root.left), 0)
        right = max(self.pathSum(root.right), 0)
        current = root.val + left + right
        self.maxValue = max(self.maxValue, current)
        res = root.val + max(left, right)
        return res
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #root -> max(root.left, root.left + root.val, root.right, root.right + root.val, root.right + root.left + root.val)
        self.pathSum(root)
        return self.maxValue


