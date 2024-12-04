#approach: O primeiro elemento na lista em pre ordem vai ser sempre o elemento que vai dividir a arvore em duas quando se olha para a lista em ordem.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode()
        for index, i in enumerate(inorder):
            if i == preorder[0]:
                root.val = preorder[0]
                root.left = self.findTree(preorder[1:index+1], inorder[:index])
                root.right = self.findTree(preorder[index+1:], inorder[index+1:])

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        for index, i in enumerate(inorder):
            if i == preorder[0]:
                root.val = preorder[0]
                root.left = self.findTree(preorder[1:index+1], inorder[:index])
                root.right = self.findTree(preorder[index+1:], inorder[index+1:])

        return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTree(self, preorder, i, j, inorder, m, n, inorder_map):
        # Se não há elementos na faixa, retorna None
        if i >= j or m >= n:
            return None
        
        # A raiz é sempre o primeiro elemento da faixa em preorder
        root_val = preorder[i]
        root = TreeNode(root_val)
        
        # Encontra a posição da raiz no inorder
        index = inorder_map[root_val]
        
        # Calcula o número de elementos na subárvore esquerda
        left_size = index - m
        
        # Subárvore esquerda
        root.left = self.findTree(preorder, i + 1, i + 1 + left_size, inorder, m, index, inorder_map)
        
        # Subárvore direita
        root.right = self.findTree(preorder, i + 1 + left_size, j, inorder, index + 1, n, inorder_map)
        
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Cria um mapa para acessar índices de inorder em O(1)
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Chama a função recursiva para construir a árvore
        return self.findTree(preorder, 0, len(preorder), inorder, 0, len(inorder), inorder_map)
    


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root



