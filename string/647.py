#time complexity O(n**2)
#space complexity O(n**2)

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for i in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        ans = len(s)

        for i in range(len(s)-1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1] == 1:
                        dp[i][j] = 1
                        ans += 1


        return ans

#time complexity O(n**2)
#space complexity O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(len(s)):
            even = self.palindromeCount(s, i, i+1)
            odd = self.palindromeCount(s, i-1, i+1)
            ans += even + odd + 1

        return ans


    def palindromeCount(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        return count


