#first solution
#time complexity O(n)

def productExceptSelf(self, nums: List[int]) -> List[int]:
    current = 1
    prefix = []
    suffix = [0] * (len(nums))
    for num in nums:
        prefix.append(current)
        current *= num
    current = 1
    for i in range(len(nums) - 1, -1, -1):
        suffix[i] = current
        current *= nums[i]
    
    ans = []
    for i in range(len(nums)):
        ans.append(prefix[i] * suffix[i])

    return ans