class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = 0

        for i in range(len(nums)):
            if i <= last:
                if i + nums[i] > last:
                    last = i + nums[i]

            else:
                return False

        return True

        