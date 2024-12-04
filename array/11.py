#time complexity O(n)
#space complexity O(1)

class Solution:
    def area(self, a, b, distance):
        return min(a, b) * distance
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maior = float('-inf')
        while l < r:
            current = self.area(height[l], height[r], r - l)
            maior = max(maior, current)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return maior