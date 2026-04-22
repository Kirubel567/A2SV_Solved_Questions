class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #directions
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
    
        #check bound using this helper function
        def inbound(row, col): 
            return 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col] == "1"

        #do the dfs
        visited =set()
        def dfs(row, col): 
            visited.add((row, col))

            for x, y in directions: 
                newr, newc = row+x, col+y
                if inbound(newr, newc) and (newr, newc) not in visited: 
                    dfs(newr, newc)
                
        islands = 0
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == "1" and (i, j) not in visited: 
                    islands += 1
                    dfs(i,j)
                
        return islands 