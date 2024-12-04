#time complexity O(n + m)
#space complexity (n + m)

class Solution:
    def spiral(self, matrix):
        res = []
        visited = {}
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        res.append(matrix[i][j])
        visited[(i, j)] = 1
        while True:
            if ((i - 1 >= 0 and (i-1, j) in visited) or i - 1 < 0) and ((i+1 < m and (i + 1, j) in visited) or i + 1 >= m) and  ((j -1 >= 0 and (i, j - 1) in visited) or j - 1 < 0) and ((j + 1 < n and (i, j + 1) in visited) or j + 1 >= n):
                break

            while (i, j + 1) not in visited and j + 1 < n:
                j += 1
                res.append(matrix[i][j])
                visited[(i, j)] = 1

            while (i + 1, j) not in visited and i + 1 < m:
                i += 1
                res.append(matrix[i][j])
                visited[(i, j)] = 1

            while (i, j - 1) not in visited and j - 1 >= 0:
                j -= 1
                res.append(matrix[i][j])
                visited[(i, j)] = 1

            while (i - 1, j) not in visited and i - 1 >= 0:
                i -= 1
                res.append(matrix[i][j])
                visited[(i, j)] = 1
        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.spiral(matrix)

#time complexity O(n + m)
#space complexity (1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res

        rowBeg = 0
        rowEnd = len(matrix)-1
        colBeg = 0
        colEnd = len(matrix[0]) -1

        while rowBeg <= rowEnd and colBeg <= colEnd:
            #right
            for i in range(colBeg, colEnd + 1):
                res.append(matrix[rowBeg][i])
                print(matrix[rowBeg][i], rowBeg, colBeg)
            rowBeg += 1

            #down
            for i in range(rowBeg, rowEnd + 1):
                res.append(matrix[i][colEnd])

            colEnd -= 1

            
            #left
            if rowBeg <= rowEnd:
                for i in range(colEnd, colBeg - 1, -1):
                    res.append(matrix[rowEnd][i])
                
            rowEnd -= 1

            #up
            if colBeg <= colEnd:
                for i in range(rowEnd, rowBeg - 1, -1):
                    res.append(matrix[i][colBeg])

            colBeg += 1

        return res


        