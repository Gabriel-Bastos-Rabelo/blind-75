class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sets(nums)

        best = 0

        for x in nums:
            if x -1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)

        return best

    
#time complexity O(n)
#space complexity O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        res = 0
        for n in nums:
            if n not in map:
                left = 0 if (n-1) not in map else map[(n-1)]
                right = 0 if (n+1) not in map else map[(n+1)]

                sum = left + right + 1
                map[n] = sum

                res = max(res, sum)
                map[(n + right)] = sum
                map[(n - left)] = sum
            else:
                continue

        return res

    


