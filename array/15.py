
#first solution
#time complexity O(n2)
#space complexity O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            initPoint = i + 1
            endPoint = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            while initPoint < endPoint:
    
                soma = nums[initPoint] + nums[endPoint]

                if soma > (nums[i] * -1):
                    endPoint -= 1
                elif soma < (nums[i] * -1):
                    initPoint += 1
                else:
                    triplet = [nums[i], nums[initPoint], nums[endPoint]]
                    
                    res.append(triplet)
                    initPoint += 1
                    while nums[initPoint] == nums[initPoint-1] and initPoint < endPoint:
                        initPoint += 1

        return res
    

#