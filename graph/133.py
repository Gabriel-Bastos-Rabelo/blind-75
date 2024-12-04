#first solution with dfs
#time complexity O(m), where m is # of edges in graph.
#space complexity O(n), where n is # of nodes in the graph. Since we are storing all the cloned node in the map.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, cur, map):
        clone = Node(cur.val)
        map[cur] = clone
        neighbors = []
        for it in cur.neighbors:
            if it not in map:
                neighbors.append(self.dfs(it, map))
            else:
                neighbors.append(map[it])

        clone.neighbors = neighbors
        return clone

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        map = {}
        return self.dfs(node, map)
    
#second solution with bfs
#time complexity O(v + e).
#space complexity O(v), where v is # of nodes in the graph. Since we are storing all the cloned node in the map.

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        fila = deque([node])
        map = {node: Node(node.val)}

        while fila:
            cur = fila.popleft()
            cur_clone = map[cur]
            for neighbor in cur.neighbors:
                if neighbor not in map:
                    map[neighbor] = Node(neighbor.val)
                    fila.append(neighbor)

                cur_clone.neighbors.append(map[neighbor])

        return map[node]