#time complexity O(nodes)
#space complexity O(height)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, level, output):
        if not root:
            return

        if len(output) > level:
            output[level].append(root.val)
        else:
            output.append([])
            output[level].append(root.val)

        self.dfs(root.left, level + 1, output)
        self.dfs(root.right, level + 1, output)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        level = 0
        self.dfs(root, level, output)
        return output
    

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bfs(self, root):
        if not root:
            return []

        q = deque(root)
        output = [[root]]
        temp = deque()

        while q:
            node = q.popleft()
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)

            if not q:
                if temp:
                    output.append([n.val for n in temp])

                q = temp
                temp = deque()

        return output



    def dfs(self, root, level, output):
        if not root:
            return

        if len(output) > level:
            output[level].append(root.val)
        else:
            output.append([])
            output[level].append(root.val)

        self.dfs(root.left, level + 1, output)
        self.dfs(root.right, level + 1, output)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        level = 0
        self.dfs(root, level, output)
        return output

        

        