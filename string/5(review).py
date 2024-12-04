class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[0] * len(s) for i in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1


        longestOne = s[0]
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1] == 1:
                        dp[i][j] = 1

                        if (j - i + 1) > len(longestOne):
                            longestOne = s[i:j+1]


        return longestOne


        