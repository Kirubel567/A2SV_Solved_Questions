class Solution:
    def totalNQueens(self, n: int) -> int:
        board=[['.' for _ in range(n)] for _ in range(n)]
        path = []
        count = 0


        def backtrack(row):
            nonlocal count
            if row == n: 
                count+=1
                return 
            
            for col in range(n): 
                if isSafe(row, col): 
                    board[row][col] = "Q"
                    backtrack(row+1)
                    board[row][col] = "."
                
        def isSafe(row, col): 
            for i in range(row): 
                if board[i][col] == "Q": 
                    return False 

            for i in range(1, min(row, col)+1): 
                if board[row-i][col-i] == "Q": 
                    return False 
            for i in range(1, min(row, n-1-col)+1): 
                if board[row-i][col+i] == "Q":
                    return False 
                
            return True 
        backtrack(0)
        return count 