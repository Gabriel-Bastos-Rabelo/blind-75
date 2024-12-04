#time complexity O(n⋅m⋅4**k)
#space complexity O(k+n⋅m⋅k)

class Solution:
    def isInLimits(self,m, n, i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return False

        return True
    def back(self, board, word, i, j, memo, index, visited):
        visited.add((i, j))
        if index == len(word)-1:
            return True
        if (i, j, index) in memo:
            return memo[(i, j, index)]

        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]


        for pos in range(4):
            new_x = i + x[pos]
            new_y = j + y[pos]

            if (new_x, new_y) in visited:
                continue
            if not self.isInLimits(len(board), len(board[0]), new_x, new_y):
                continue

            if board[new_x][new_y] == word[index+1]:
                memo[(i, j, index)] = self.back(board, word, new_x, new_y, memo, index+1, visited)
                if memo[(i, j, index)]:
                    return True

        visited.remove((i, j))
        if (i, j, index) in memo:
            memo.pop((i, j, index))

        return False

        

    def exist(self, board: List[List[str]], word: str) -> bool:
        memo = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    if self.back(board, word, i, j,memo, 0, visited):
                        return True

        return False
        

class Solution:

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        tmp = board[i][j]

        board[i][j] = "#"

        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+ 1, word[1:]) or self.dfs(board, i, j -1, word[1:])

        board[i][j] = tmp
        return res
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
            
        return False