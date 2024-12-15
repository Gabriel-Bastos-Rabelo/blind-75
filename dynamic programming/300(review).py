#time complexity O(n2)
#space complexity O(n)

##The longer subsequence that ends with number i. for this we will consider dp[n] where dp[i] represents the longer subsequence 
# that ends with the number at nums[i]. To calculate this we have to consider the previous values. dp[i] will be the maximum value between (dp[0] to dp[i-1]) + 1
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

#

def findIndex(arr: List[int], n: int) -> int:
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left)//2
        if arr[mid] == n:
            return mid

        elif arr[mid] > n:
            right = mid - 1

        else:
            left = mid + 1

    return left




def lengthOfLIS(self, nums: List[int]) -> int:
    sub = []
    for x in nums:
        if len(sub) == 0 or sub[-1] < x:
            sub.append(x)

        else:
            idx = bisect_left(sub, x)

            sub[idx] = x

    return len(sub)


        

    

    

        
