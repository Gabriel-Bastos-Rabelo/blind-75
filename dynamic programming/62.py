#time complexity O(n * m)
#space complexity O(n * m)

class Solution:
    
    def recursion(self, n, m, dp, i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0

        if dp[i][j] != 0:
            return dp[i][j]

        dp[i][j] = self.recursion(n, m, dp, i - 1, j) + self.recursion(n, m, dp, i, j - 1)
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for i in range(m)]

        return self.recursion(n, m, dp, m-1, n-1)
    

#time complexity O(n * m)
#space complexity O(n * m)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]


        return dp[m-1][n-1]
    
#time complexity O(n * m)
#space complexity O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]
        dp = [1] * n
        prevCol = 1

        for i in range(1, m):
            prevCol = 1
            for j in range(1, n):
                dp[j] = dp[j] + prevCol
                prevCol = dp[j]

            
        return dp[n-1]



        
        

