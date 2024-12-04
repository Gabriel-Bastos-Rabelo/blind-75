#time complexity O(nm)
#space complexity O(nm)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        larger = max(len(text1), len(text2))
        smaller = min(len(text1), len(text2))
        smallerString = text1 if len(text1) == smaller else text2
        largerString = text2 if len(text2) == larger else text1
        dp = [[0 for i in range(larger + 1)] for j in range(smaller+1)]

        for i in range(1, smaller+1):
            for j in range(1, larger+1):
                #dp[i][j]  =>>> smaller[:i] and larger[:j] ==>> whats the longest substring that ends at i and j
                #smaller[i] == larger[j] ==> dp[i-1][j-1] + 1
                #smaller[i] !== larger[j] ==> max(dp[i-1][j], dp[i][j-1])
                if smallerString[i-1] == largerString[j-1]:

                    dp[i][j] = dp[i-1][j-1] + 1

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[smaller][larger]


