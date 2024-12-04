#time complexity O(n)
#space complexity O(n)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0  # Declare ans within the method

        def dfs(root, position, target):
            if not root:
                return position

            pos = dfs(root.left, position, target)

            if pos == target:
                self.ans = root.val

            pos = dfs(root.right, pos + 1, target)

            return pos + 1

        dfs(root, 1, k)
        return self.ans