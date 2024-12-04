#time complexity O(n)
#space complexity O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root):
        if not root:
            return None
        if root.left == None and root.right == None:
            return root

        root.left, root.right = self.dfs(root.right), self.dfs(root.left)


        return root

        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)
    
#time complexity O(n)
#space complexity O(n)

def bfs(self, root):
        if root == None:
            return None

        q = deque()

        q.append(root)

        while q:
            node = q.popleft()
            left = node.left
            node.left = node.right
            node.right = left

            if node.left != None:
                q.append(node.left)

            if node.right != None:
                q.append(node.right)

        return root