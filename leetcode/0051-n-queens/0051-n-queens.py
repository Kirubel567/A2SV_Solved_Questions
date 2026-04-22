class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #you have to check every possibility of putting the qweens in the rows
        #that's starting from [0,0] to [0,len(n)] you have to make it the start and then do the same for the next rows too 
        #for each combination (row) you have to check if we can put that specific qween in that specificy possition 
        #use a helper function to check if we can put it or not 

        #create the path matrix 
        mat = [["." for _ in range(n)] for _ in range(n)]
        
        #remember its all about exhausting all the possible combinations
        #you start from the [0,0] by putting a qween there 
        ans = []
        def find_place(row): 
            #base case
            if n == row: 
                ans.append(["".join(r) for r in mat])
                return 
            
            for col in range(n):
                if check_validity(row, col): 
                    #mark the qween
                    mat[row][col] = "Q"
                    find_place(row+1)
                    mat[row][col] = "."
        
        def check_validity(row, col): 
            #check vertical 
            for r in range(row):
                if mat[r][col] == "Q": 
                    return False
            #check diagonal left top
            for i in range(1, min(row, col)+1): 
                if mat[row-i][col-i] == "Q": 
                    return False
            #check diagonal right top
            for i in range(1, min(row, n-col-1)+1): 
                if mat[row-i][col+i] == "Q": 
                    return False
            return True 
        find_place(0)
        return ans 

