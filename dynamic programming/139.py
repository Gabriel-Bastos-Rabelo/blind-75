#first solution
#time complexity O(n ** 2)
#space complexity O(s + m)

class Solution:
    def wb(self, s, setMap, memo):
        
        if s in memo:
            return memo[s]
        size = len(s)

        if size == 0:
            return True

        for i in range(1, size+1):
            if s[0:i] in setMap and self.wb(s[i:], setMap, memo):
                memo[s] = True
                return True

        memo[s] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        setMap = set(wordDict)
        print(setMap)
        memo = {}
        return self.wb(s, setMap, memo)
    

#second sulution
#time complexity O(n ** 2)
#space complexity O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i-1, -1, -1):
                if dp[j]:
                    word = s[j:i]
                    if word in wordDict:
                        dp[i] = True
                        break

        print(dp)
        return dp[len(s)]

                

                