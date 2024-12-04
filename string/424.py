#time complexity O(n)
#space complexity O(n)

from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = 0
        for letter in alphabet:
            times = k
            left = -1
            q = deque()
            firstAppear = -1
            right = 0
            currentValue = 0
            while right < len(s):
                if s[right] != letter:
                    if times > 0:
                        times -= 1
                        q.append(right)
                    else:
                        if q:
                            left = q.popleft()
                            q.append(right)
                        else:
                            left = right
                
                currentValue = max(currentValue, right - left )
                right += 1

                
            res = max(res, currentValue)
        return res
                    


from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        maxLen = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            cur_len = r - l + 1

            if cur_len - max(freq.values()) <= k:
                maxLen = max(maxLen, cur_len)

            else:
                freq[s[l]] -= 1
                l += 1
                
        return maxLen
                    


