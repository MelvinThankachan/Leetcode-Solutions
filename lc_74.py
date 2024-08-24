# 74. Search a 2D Matrix


class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        top_row = 0
        bottom_row = m - 1
        while top_row <= bottom_row:
            row = (top_row + bottom_row) // 2
            if target > matrix[row][-1]:
                top_row = row + 1
            elif target < matrix[row][0]:
                bottom_row = row - 1
            else:
                break
        
        if top_row > bottom_row:
            return False
        
        left = 0
        right = n - 1
        while left <= right:
            column = (left + right) // 2
            if target == matrix[row][column]:
                return True
            elif target > matrix[row][column]:
                left = column + 1
            else:
                right = column - 1
        
        return False



result = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
output = result.searchMatrix(matrix, target)
print(output)
expected = True
if output == expected:
    print("Test passed successfully!")
