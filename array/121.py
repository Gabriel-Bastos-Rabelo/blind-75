

#first solution
#time complexity o(n)
def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - minimum)
            minimum = min(minimum, prices[i])

        return res


