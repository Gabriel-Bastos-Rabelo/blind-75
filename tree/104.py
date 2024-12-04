#first solution
#time complexity O(n)
#space complexity O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.left == None and root.right == None:
                return 1

            if root.left == None:
                return self.maxDepth(root.right) + 1

            if root.right == None:
                return self.maxDepth(root.left) + 1

            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return 0