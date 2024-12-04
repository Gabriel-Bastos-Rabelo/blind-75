
#time complexity O(log m + log n)
#space complexity O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearchRow(matrix, target):
            left = 0
            right = len(matrix)-1

            while left < right:
                mid = left + (right - left)//2

                if matrix[mid][0] == target:
                    return mid
                if matrix[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if matrix[left][0] > target:
                return left - 1
            
            return left

        def binarySearchColumn(matrix, target, row):
            left = 0
            right = len(matrix[0]) - 1

            while left <= right:
                mid = left + (right - left)//2

                if matrix[row][mid] == target:
                    return mid
                
                if matrix[row][mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return -1


        row = binarySearchRow(matrix, target)

        if row == -1:
            return False

        col = binarySearchColumn(matrix, target, row)

        if col == -1:
            return False


        return True


        

        

#time complexity O(log(n * m))
#space complexity O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1

        while left <= right:

            mid = left + (right - left)//2
            print(left, right, mid)

            if matrix[mid//len(matrix[0])][mid % len(matrix[0])] == target:
                return True

            elif matrix[mid//len(matrix[0])][mid % len(matrix[0])] > target:
                right = mid - 1

            else:
                left = mid + 1

        return False