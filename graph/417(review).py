#time complexity O(m * n)
#space complexity O(n * m)

class Solution:
    def __init__(self):
        # Inicializar as matrizes pacific e atlantic dentro do construtor
        self.pacific = []
        self.atlantic = []

    def dfs(self, row, col, matrix, visited, ans, m, n):
        if visited[row][col]:
            return
        visited[row][col] = True

        # Verifica se o ponto pode alcançar os dois oceanos
        if self.atlantic[row][col] and self.pacific[row][col]:
            ans.append([row, col])

        # Realiza a busca em profundidade nas quatro direções
        if row + 1 < m and matrix[row + 1][col] >= matrix[row][col]:
            self.dfs(row + 1, col, matrix, visited, ans, m, n)

        if row - 1 >= 0 and matrix[row - 1][col] >= matrix[row][col]:
            self.dfs(row - 1, col, matrix, visited, ans, m, n)

        if col + 1 < n and matrix[row][col + 1] >= matrix[row][col]:
            self.dfs(row, col + 1, matrix, visited, ans, m, n)

        if col - 1 >= 0 and matrix[row][col - 1] >= matrix[row][col]:
            self.dfs(row, col - 1, matrix, visited, ans, m, n)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        self.pacific = [[False] * n for _ in range(m)]
        self.atlantic = [[False] * n for _ in range(m)]
        ans = []

        # Iniciar a DFS para as bordas que tocam os oceanos
        for i in range(m):
            # Oceano Atlântico (coluna direita)
            self.dfs(i, n - 1, heights, self.atlantic, ans, m, n)
            # Oceano Pacífico (coluna esquerda)
            self.dfs(i, 0, heights, self.pacific, ans, m, n)

        for i in range(n):
            # Oceano Pacífico (linha superior)
            self.dfs(0, i, heights, self.pacific, ans, m, n)
            # Oceano Atlântico (linha inferior)
            self.dfs(m - 1, i, heights, self.atlantic, ans, m, n)

        return ans
