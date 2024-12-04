#first solution (it does not passed)
#time complexity O(n2)

def maxSubArray(self, nums: List[int]) -> int:
    res = nums[0]
    print(nums)
    current = nums[0]
    for i in range(len(nums)):
        current = nums[i]
        res = max(res, current)
        for j in range(i+1, len(nums)):
            current += nums[j]

            res = max(res, current)
        

    return res


#second solution
#time complexity O(n)
def maxSubArray(self, nums: List[int]) -> int:
    dp = [float('-inf')] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])


    return max(dp)

