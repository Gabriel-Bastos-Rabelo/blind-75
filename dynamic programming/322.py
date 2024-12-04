#first solution
#time complexity O(k * n)
#space complexity O(n)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        coins.sort()

        for i in range(1, amount + 1):
            dp[i] = float('inf')

            for c in coins:
                if c > i:
                    break

                dp[i] = min(dp[i], 1 + dp[i - c])

        if dp[amount] != float('inf'):
            return dp[amount]

        return -1
    
#second sulution with recursion
#time complexity O(2 ** n)
#space complexity O(n)
class Solution:
    def findLowestCoins(self, cur, amount, coins):
        if amount == 0:
            return 0
        if cur >= len(coins) or amount < 0:
            return float('inf')

        return min(self.findLowestCoins(cur, amount - coins[cur], coins) + 1, self.findLowestCoins(cur + 1, amount - coins[cur], coins) + 1, self.findLowestCoins(cur +1, amount, coins))

    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self.findLowestCoins(0, amount, coins)
        if res != float('inf'):
            return res
        return -1
    


#third solution with memoization
#time complexity O(n*m)
#space complexity O(n * m)
class Solution:
    dp = {}
    def findLowestCoins(self, cur, amount, coins):
        if amount == 0:
            return 0
        if cur >= len(coins) or amount < 0:
            return float('inf')
        if (cur, amount) in self.dp:
            return self.dp[(cur, amount)]

        res =  min(self.findLowestCoins(cur, amount - coins[cur], coins) + 1, self.findLowestCoins(cur + 1, amount - coins[cur], coins) + 1, self.findLowestCoins(cur +1, amount, coins))
        self.dp[(cur, amount)] = res
        return res

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = {}
        res = self.findLowestCoins(0, amount, coins)
        if res != float('inf'):
            return res
        return -1

#fourth solution
#time complexity O(n * m)
#space complexity O(n * m)

class Solution:
    dp = {}
    def findLowestCoins(self, cur, amount, coins):
        for i in range(len(coins) + 1):
            for j in range(amount + 1):
                if i == 0 or j == 0:
                    if j == 0:
                        self.dp[i][j] = 0

                    else:
                        self.dp[i][j] = float('inf')
        
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i-1] > j:
                    self.dp[i][j] = 0 + self.dp[i - 1][j]

                else:
                    self.dp[i][j] = min(0 + self.dp[i - 1][j], 1 + self.dp[i][j - coins[i - 1]])

        return self.dp[len(coins)][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [[float('inf')] * (amount + 1) for _ in range(13)]
        
        res = self.findLowestCoins(0, amount, coins)
        if res != float('inf'):
            return res
        return -1


