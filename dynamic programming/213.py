#time complexity O(n)
#space complexity O(1)

class Solution:
    def robSolution(self, nums):
        if not nums:
            return 0
        #dp[i] = max(values[i] + dp[i-2], dp[i-1])
        prev1 = nums[0]
        prev2 = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                prev2 = prev1
                prev1 = max(nums[i], nums[i-1])
        
            else:
                temp = prev1
                prev1 = max(nums[i] + prev2, prev1)
                prev2 = temp


        return prev1
        
    def rob(self, nums: List[int]) -> int:
        #do the problem until the last house - 1 --> i will have the best option considering the first house and not considering the last house
        #do the problem starting from the house 2 --> i will have the best option considering the last house and not considering the first house
        if len(nums) == 1:
            return nums[0]
        return max(self.robSolution(nums[:len(nums)-1]), self.robSolution(nums[1:]))

