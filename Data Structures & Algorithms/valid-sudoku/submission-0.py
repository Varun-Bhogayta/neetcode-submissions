class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ## row check 
        for row in board:
            if self.isDuplicatePresent(row):
                print("exited at:",row)
                return False
        
        ## column check 
        for col_ind in range(len(board)):
            col = []
            for row_ind in range(len(board)):
                col.append(board[row_ind][col_ind])
            if self.isDuplicatePresent(col):
                print("exited at:",col_ind)
                return False 
        
        ## small box check 
        
        for row_box in range(3):
            for col_box in range(3):
                small_box_flat = []
                for small_row in range((row_box*3),(row_box*3) + 3):
                    for small_col in range((col_box*3),(col_box*3) + 3):
                        small_box_flat.append(board[small_row][small_col])
                if self.isDuplicatePresent(small_box_flat):
                    print(f"exited at row:{small_row} and col:{small_col} and box({row_box},{col_box})")
                    return False 

        return True 

        
    @staticmethod
    def isDuplicatePresent(arr: List[str]) -> bool:
        seen = set()
        for ele in arr:
            if ele != ".":
                if ele in seen:
                    return True  # Duplicate found!
                seen.add(ele)
        return False  # No duplicates found after checking the whole array