# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#time complexity O(n)
#space complexity O(n)
class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(root, p, q):
            if not root:
                return False
            if root.val == p.val or root.val == q.val:
                if dfs(root.right, p, q) or dfs(root.left, p, q):
                    self.ans = root
                return True

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if left and right:
                if not self.ans:
                    self.ans = root
                return True

            if left or right:
                return True

            return False

            

        dfs(root, p, q)
        return self.ans





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#time complexity O(n)
#space complexity O(1)

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small = min(q.val, p.val)
        large = max(q.val, p.val)

        while root:
            if small > root.val:
                root = root.right

            elif large < root.val:
                root = root.left

            else:
                return root

        return None

            