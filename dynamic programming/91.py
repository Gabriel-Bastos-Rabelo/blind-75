#time complexity O(n)
#space complexity O(n)


class Solution:
    def numDecodings(self, s: str) -> int:
        #dp[i] = dp[i-2] + 1 + dp[i-1] + 1
        #s[i-1] + s[i] <= 27 and s[i-1] != 0
        #s[i] != 0

        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        map = {}

        for index, i in enumerate(alfabeto):
            map[str(index+1)] = i


        dp = [0] * (len(s))


        if s[0] == '0':
            return 0

        dp[0] = 1
        if len(s) == 1:
            return 1

        if s[1] != '0':
            if int(s[0]) > 2:
                dp[1] = 1
            else:
                if int(s[0]) == 2 and int(s[1]) >= 7:
                    dp[1] = 1
                else:
                    dp[1] = 2

        else:
            if int(s[0]) > 2:
                return 0
            else:
                dp[1] = 1

        for i in range(2, len(s)):
            if int(s[i-1]) < 2 and int(s[i-1]) != 0:
                dp[i] = dp[i-2]
            elif int(s[i-1]) == 2:
                if int(s[i]) < 7:
                    dp[i] = dp[i-2]

            

            if int(s[i]) != 0:
                dp[i] += dp[i-1]

        return dp[len(s)-1]

            

            
