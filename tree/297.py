# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
            
        vals = []
        doit(root)
        return ' '.join(vals)

    def construir_arvore(self, string, index):
        if index >= len(string):
            return None, index

        valor = string[index]

        if valor == '#':
            return None, index + 1

        node = TreeNode(int(valor))
        index += 1

        node.left, index = self.construir_arvore(string, index)
        node.right, index = self.construir_arvore(string, index)


        return node, index


    def deserialize(self, data):
        string = data.split()
        tree = self.construir_arvore(string, 0)
        return tree[0]
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))