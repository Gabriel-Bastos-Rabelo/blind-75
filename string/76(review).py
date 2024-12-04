#time complexity O(n + m)
#space complexity O(m)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m  = {}
        for i in t:
            m[i] = m.get(i, 0) + 1

        start = 0
        end = 0
        counter = len(t)
        minStart = 0
        minLen = float('inf')
        size = len(s)

        while end < size:
            if s[end] in m and m[s[end]] > 0:
                counter -= 1

            if s[end] in m:
                m[s[end]] -= 1

            end += 1

            while counter == 0:
                if (end-start < minLen):
                    minStart = start
                    minLen = end - start

                if s[start] in m:
                    m[s[start]] += 1

                    if m[s[start]] > 0:
                        counter += 1

                start += 1


        if minLen != float('inf'):
            return s[minStart: minStart + minLen]

        return ""
