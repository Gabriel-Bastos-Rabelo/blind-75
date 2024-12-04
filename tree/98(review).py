#time complexity O(n)
#space complexity O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(root, minimo, maximo):
            if not root:
                return True

            if root.val <= minimo or root.val >= maximo:
                return False

            if root.left:
                if root.left.val < root.val:
                    if not isValid(root.left, minimo, root.val):
                        return False

                else:
                    return False

            if root.right:
                if root.right.val > root.val:
                    if not isValid(root.right, root.val, maximo):
                        return False

                else:
                    return False

            return True

        return isValid(root, float('-inf'), float('inf'))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        pre = None
        stack = []
        while (root != None or stack):
            while root != None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pre != None and root.val <= pre.val:
                return False
            
            pre = root
            root = root.right

        return True
