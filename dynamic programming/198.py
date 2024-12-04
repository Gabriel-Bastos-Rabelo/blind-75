#time complexity O(n)
#space complexity O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i - 2 < 0:
                dp[i] = max(nums[i], nums[i-1])

            else:
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        
        return max(dp)


#time complexity O(n)
#space complexity O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        prev1 = nums[0]
        prev2 = 0
        for i in range(1, len(nums)):
            if i - 2 < 0:
                prev2 = prev1
                prev1 = max(nums[i], prev1)

            else:
                temp = prev1
                prev1 = max(nums[i] + prev2, prev1)
                prev2 = temp

        
        return prev1