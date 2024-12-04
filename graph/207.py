#first solution
#time complexity O(v + e)
#space complexity O(v + e)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = {}
        for i in range(numCourses):
            self.graph[i] = []

        for i in prerequisites:
            self.graph[i[0]].append(i[1])

        visited = set()
        onPath = set()

        def dfs(node):
            if node in onPath:
                return False

            if node in visited:
                return True

            onPath.add(node)
            visited.add(node)
            for neighbor in self.graph[node]:
                if not dfs(neighbor):
                    return False

            onPath.remove(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

    

#second sulution
#time complexity O(v + e)
#space complexity O(v + e)
from collections import deque
class Solution:

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = {}
        self.indegree = [0] * (numCourses + 1)
        for i in range(numCourses):
            self.graph[i] = []

        for i in prerequisites:
            self.graph[i[1]].append(i[0])
            self.indegree[i[0]] += 1


        def bfs():
            q = deque([i for i in range(numCourses) if self.indegree[i] == 0])
            completedCourses = 0
            while q:
                current = q.popleft()
                completedCourses += 1
                for neighbor in self.graph[current]:
                    self.indegree[neighbor] -= 1
                    if self.indegree[neighbor] == 0:
                        q.append(neighbor)

            
                
                        
            return completedCourses == numCourses

        return bfs()

    