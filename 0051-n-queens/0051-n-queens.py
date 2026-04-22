class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #first create the matrix of nxn with all the cells "."
        #check row by row each column choose one column and recursively choose the next column in the next row 
        #if the number of rows == len(curr) add it to the answer array (base case)

        board=[["." for _ in range(n)] for _ in range(n)]
        ans=[]

        def backtrack(row):
            if row == n: 
                ans.append([''.join(r) for r in board])
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
            for i in range(1, min(row, n-col-1)+1):
                if board[row-i][col+i] == "Q": 
                    return False
            return True 
        backtrack(0)
        return ans 