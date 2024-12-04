#time complexity O(n**2)
#space complexity O(n * n)

class Solution:
    def checkAnagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        map = {}

        for i in str1:
            map[i] = map.get(i, 0) + 1

        for i in str2:
            if i not in map or map[i] == 0:
                return False

            map[i] -= 1

        return True



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        map = {}
        for index, string in enumerate(strs):
            if string in map:
                continue
            newArray = [string]
            map[string] = True
            for i in range(index + 1, len(strs)):
                if self.checkAnagram(string, strs[i]):

                    newArray.append(strs[i])
                    map[strs[i]] = True

            ans.append(newArray)

        return ans

        


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for string in strs:
            sorted_word = ''.join(sorted(string))
            if sorted_word in map:
                map[sorted_word].append(string)

            else:
                map[sorted_word] = [string]


        ans = []

        for key in map:
            ans.append(map[key])

        return ans