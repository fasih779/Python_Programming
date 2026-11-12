class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix[0]) - 1
        row = 0

        while row < len(matrix):

            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True

            elif target > matrix[row][right]:
                row += 1

            elif target < matrix[row][left]:
                    return False

            elif target > matrix[row][mid]:
                left = mid + 1

            else:
                right = mid - 1
        return False        