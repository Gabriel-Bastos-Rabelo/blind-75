#first solution
#time complexity O(n)

def maxProduct(self, nums: List[int]) -> int:
    #dp[i] = max(dp[i-1] + nums[i], nums[i])
    #dp[i] = [best_solution, smaller negative multiplication]
    #[2,-5,-2,-4,3]
    #dp[0] = [2, 2]
    #dp[1] = [-5, -10]
    #dp[2] = [20, -2]
    #dp[3] = [8, -80]
    #dp[4] = [24, -240]
    dp = [float('-inf')] * len(nums)
    dp[0] = [nums[0], nums[0]]
    for i in range(1, len(nums)):
        dp[i] = [max(nums[i], nums[i] * dp[i-1][0], nums[i] * dp[i-1][1]), min(nums[i], nums[i] * dp[i-1][0], nums[i] * dp[i-1][1])]
    print(dp)
    ans = float('-inf')
    for i in dp:
        ans = max(ans, max(i))

    return ans


#second solution
#time complexity O(n)
#space complexity O
def maxProduct(self, nums: List[int]) -> int:
        imax = float('-inf')
        imin = float('inf')
        ans = float('-inf')

        #[3, -2, -2]
        current = nums[0]
        for i in range(len(nums)):
            if nums[i] < 0:
                imin, imax = imax, imin
            imax = max(nums[i], imax*nums[i])
            imin = min(nums[i], imin*nums[i])

            ans = max(ans, imax)
        print(ans)
        return ans