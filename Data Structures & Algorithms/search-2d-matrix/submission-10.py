class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, (len(matrix) * len(matrix[0])) - 1
        while start <= end:
            mid = int(start + (end - start)/2) 
            row = int(mid/len(matrix[0]))
            col = int(mid % len(matrix[0])) 
            print(row,col,mid)
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                end = mid - 1
            else:
                start = mid + 1
        return False