#first solution
#time complexity O(logn)
#space complexity O(logn)
def binarySearch(nums, left, right, target):
    
    middle = (left + right)//2
    meio = nums[middle]
    if meio == target:
        return middle
    if left >= right:
        return -1
    if meio >= nums[right]:
        if target >= meio:
            return binarySearch(nums, middle + 1, right, target)
        else:
            if target >= nums[left]:
                return binarySearch(nums, left, middle, target)
            else:
                return binarySearch(nums, middle + 1, right, target)

    else:
        if target <= meio:
            return binarySearch(nums, left, middle, target)

        else:
            if target == nums[right]:
                return right
            if target > nums[right]:
                return binarySearch(nums, left, middle, target)
            else:
                return binarySearch(nums, middle + 1, right, target)
            

#second solution
#time complexity O(logn)
#space complexity O(1)
def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    l = 0
    r = n - 1

    while(l <= r):
        mid = (l + r)//2
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if target >= nums[l] and target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        elif target >= nums[mid] and target <= nums[r]:
            l = mid + 1
        else:
            r = mid - 1

    return -1