#first solution
#time complexity O(n)
#space complexity O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        before = [0] * 32
        after = [0] * 32
        for i in range(len(nums) + 1):
            for j in range(32):
                if i & (1 << j):
                    before[j] += 1

        for i in nums:
            for j in range(32):
                if i & (1 << j):
                    after[j] += 1

        print(before)
        print(after)
        potence = 0
        ans = 0
        for i in range(32):
            diff = before[i] - after[i]
            if diff > 0:
                ans += 2 ** potence

            potence += 1
        
        return ans

#second solution
#time complexity O(n)
#space complexity O(1)

def missingNumber(nums):
    n = len(nums)
    ans = 0

    for i in range(1, n + 1):
        ans = ans ^ i

    for num in nums:
        ans = ans ^ num

    return ans