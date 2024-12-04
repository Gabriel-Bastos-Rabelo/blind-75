#time complexity O(n2)
#space complexity O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums) + 1)
        last = nums[0]

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
       
        return max(dp)
    

#time complexity O(n log n)
#space complexity O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)

            else:
                idx = bisect_left(sub, x)

                sub[idx] = x

        return len(sub)
        

    

    

        
