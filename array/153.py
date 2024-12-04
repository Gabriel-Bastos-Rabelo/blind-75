#fist solution
#time complexity O(n)
#space complexity

def binarySearch(self, nums, left, right):
    if left >= right:
        return min(nums[left], nums[left -1])

    middle = (left + right)//2
    meio = nums[middle]
    if meio >= nums[left] and meio >= nums[right]:
        return self.binarySearch(nums, middle + 1, right)
    elif meio <= nums[left] and meio <= nums[right]:
        return self.binarySearch(nums, left, middle)

    elif meio >= nums[left] and meio <= nums[right]:
        return self.binarySearch(nums, left, middle)

    elif meio <= nums[left] and meio >= nums[right]:
        return self.binarySearch(nums, middle+1, right)

        
def findMin(self, nums: List[int]) -> int:
    return self.binarySearch(nums, 0, len(nums) - 1)