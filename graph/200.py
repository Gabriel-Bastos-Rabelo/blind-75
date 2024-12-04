from collections import deque

class Solution:

    #time complexity O(n2)
    #space complexity O(n2)
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return

        if grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    #time complexity O(n2)
    #space complexity O(n)
    def bfs(self, grid, i, j):
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        q = deque()

        q.append((i, j))

        while q:
            current = q.popleft()
            grid[current[0]][current[1]] = "0"
            for i in range(4):
                new_x = current[0] + x[i]
                new_y = current[1] + y[i]
                if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
                    continue

                if grid[new_x][new_y] == "1":
                    grid[new_x][new_y] = "0"
                    q.append((new_x, new_y))



    def numIslands(self, grid: List[List[str]]) -> int: 
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    self.bfs(grid, i, j)


        return ans
