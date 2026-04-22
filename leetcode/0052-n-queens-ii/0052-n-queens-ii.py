class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["." for _ in range(n)] for _ in range(n)]

        counter=0
        def backtrack(row): 
            nonlocal counter
            if row == n: 
                counter += 1
                return 
            
            for col in range(n): 
                if validate(row, col): 
                    board[row][col] = "Q"
                    backtrack(row+1)
                    board[row][col] = "."
        def validate(row, col): 
            for r in range(row): 
                if board[r][col] == "Q": 
                    return False 
            for i in range(1, min(row, col)+1): 
                if board[row-i][col-i] == "Q": 
                    return False 
            for i in range(1, min(row, n-col-1)+1): 
                if board[row-i][col+i] == "Q": 
                    return False
            return True 
        backtrack(0)
        return counter