class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        longest = 0
        left = -1
        for index, letter in enumerate(s):
            if letter not in map or map[letter] < left:
                map[letter] = index
                lenght = index - left
                print(lenght, left, index)
                longest = max(longest, lenght)

            else:
                left = map[letter]
                map[letter] = index




        print(left)
        return longest

            