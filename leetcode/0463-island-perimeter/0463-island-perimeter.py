class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #directions
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
    
        #check bound using this helper function
        def inbound(row, col): 
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        #do the dfs
        visited =set()
        perimeter = 0
        def dfs(row, col): 
            nonlocal perimeter

            visited.add((row, col))

            for x, y in directions: 
                newr, newc = row+x, col+y

                if not inbound(newr, newc) or grid[newr][newc] == 0: 
                    perimeter+=1
                elif grid[newr][newc] == 1 and (newr, newc) not in visited: 
                    dfs(newr, newc)
            
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 1 and (i, j) not in visited: 
                    dfs(i,j)
                
        return perimeter 
