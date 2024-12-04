#time complexity O(n)
#space complexity O(1) only 26 letters

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        map = {}
        for i in s:
            map[i] = map.get(i, 0) + 1

        for i in t:
            if i not in map or map[i] == 0:
                return False

            map[i] -= 1

        return True
